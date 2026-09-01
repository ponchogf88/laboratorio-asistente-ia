"""Entrega idempotente de invitaciones y alertas mediante webhooks n8n."""

import logging
from typing import Any, Callable

import requests

from automation_engine.config import Settings
from automation_engine.storage import EventStore

logger = logging.getLogger(__name__)
DeliveryFunction = Callable[[dict[str, Any], Settings], dict[str, Any]]


def _headers(token: str | None) -> dict[str, str]:
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def deliver_onboarding(job: dict[str, Any], settings: Settings) -> dict[str, Any]:
    if not settings.onboarding_webhook_url:
        raise RuntimeError("ONBOARDING_WEBHOOK_URL no está configurada")
    payload = {
        "event": "student.onboarding.requested",
        "event_key": job["event_key"],
        "enrollment_id": job["enrollment_id"],
        "payment_id": job["payment_id"],
        "email": job["email"],
        "product_code": job["product_code"],
        "course_id": settings.google_classroom_course_id,
    }
    response = requests.post(
        settings.onboarding_webhook_url,
        json=payload,
        headers=_headers(settings.onboarding_webhook_token),
        timeout=20,
    )
    response.raise_for_status()
    result = response.json()
    if result.get("status") != "delivered" or not result.get("external_id"):
        raise RuntimeError(f"Respuesta de onboarding inválida: {result}")
    return result


def send_alert(payload: dict[str, Any], settings: Settings) -> None:
    if not settings.alert_webhook_url:
        logger.error("Alerta no entregada; ALERT_WEBHOOK_URL ausente: %s", payload)
        return
    response = requests.post(
        settings.alert_webhook_url,
        json=payload,
        headers=_headers(settings.alert_webhook_token),
        timeout=15,
    )
    response.raise_for_status()


def process_one_job(
    store: EventStore,
    settings: Settings,
    enrollment_id: str | None = None,
    delivery: DeliveryFunction = deliver_onboarding,
) -> dict[str, Any]:
    job = store.claim_job(enrollment_id)
    if not job:
        return {"status": "idle"}
    try:
        result = delivery(job, settings)
        store.mark_job_delivered(job, str(result["external_id"]), result)
        return {
            "status": "delivered",
            "enrollment_id": job["enrollment_id"],
            "external_id": result["external_id"],
        }
    except Exception as exc:
        error = f"{type(exc).__name__}: {exc}"
        terminal = store.mark_job_failed(job, error)
        if terminal:
            try:
                send_alert(
                    {
                        "event": "student.onboarding.failed",
                        "severity": "critical",
                        "enrollment_id": job["enrollment_id"],
                        "payment_id": job["payment_id"],
                        "attempts": job["attempt_count"],
                        "error": error,
                    },
                    settings,
                )
            except Exception:
                logger.exception("No se pudo entregar la alerta terminal")
        return {
            "status": "failed",
            "terminal": terminal,
            "enrollment_id": job["enrollment_id"],
        }


def dispatch_lead(lead: dict[str, Any], settings: Settings) -> str:
    if not settings.lead_webhook_url:
        logger.info("Lead persistido; entrega externa no configurada (lead_id=%s)", lead["lead_id"])
        return "stored_only"
    response = requests.post(
        settings.lead_webhook_url,
        json={"event": "lead.received", "lead": lead},
        headers=_headers(settings.lead_webhook_token),
        timeout=15,
    )
    response.raise_for_status()
    return "delivered"
