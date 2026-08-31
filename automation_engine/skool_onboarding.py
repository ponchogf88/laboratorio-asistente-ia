"""Entrega eventos verificados al flujo real de onboarding (n8n/Make/Zapier)."""

import logging
from typing import Any

import requests

from automation_engine.config import Settings

logger = logging.getLogger(__name__)


def _deliver(url: str, payload: dict[str, Any], token: str | None) -> None:
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    response = requests.post(url, json=payload, headers=headers, timeout=15)
    response.raise_for_status()


def dispatch_student_onboarding(payment: dict[str, Any], settings: Settings) -> str:
    """Envía el pago validado al integrador; nunca finge una entrega exitosa."""
    if not settings.onboarding_webhook_url:
        logger.warning(
            "Onboarding no enviado: ONBOARDING_WEBHOOK_URL no está configurada "
            "(payment_id=%s)",
            payment["payment_id"],
        )
        return "not_configured"
    _deliver(
        settings.onboarding_webhook_url,
        {"event": "student.onboarding.requested", "payment": payment},
        settings.onboarding_webhook_token,
    )
    logger.info("Onboarding entregado (payment_id=%s)", payment["payment_id"])
    return "delivered"


def dispatch_lead(lead: dict[str, Any], settings: Settings) -> str:
    if not settings.lead_webhook_url:
        logger.info("Lead persistido; entrega externa no configurada (lead_id=%s)", lead["lead_id"])
        return "stored_only"
    _deliver(
        settings.lead_webhook_url,
        {"event": "lead.received", "lead": lead},
        settings.lead_webhook_token,
    )
    return "delivered"
