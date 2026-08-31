"""API de eventos para leads, pagos verificados y onboarding."""

import hmac
import logging
import os
from typing import Literal
from uuid import uuid4

from dotenv import load_dotenv
from fastapi import BackgroundTasks, FastAPI, Header, HTTPException, Request, status
from pydantic import BaseModel, Field
import stripe
import uvicorn

from automation_engine.config import Settings
from automation_engine.skool_onboarding import dispatch_lead, dispatch_student_onboarding
from automation_engine.storage import EventStore

load_dotenv()
logger = logging.getLogger(__name__)

SUPPORTED_STRIPE_EVENTS = {"checkout.session.completed"}
TIER_BY_AMOUNT = {2700: "tripwire", 29700: "bootcamp", 199700: "accelerator"}
ALLOWED_TIERS = set(TIER_BY_AMOUNT.values())


class LeadInbound(BaseModel):
    source: Literal["instagram_dm", "website_optin", "whatsapp", "telegram", "manual"]
    full_name: str = Field(min_length=2, max_length=120)
    email: str | None = Field(default=None, max_length=254)
    phone: str | None = Field(default=None, max_length=40)
    instagram_handle: str | None = Field(default=None, max_length=80)
    interest: str = Field(default="general_ai_course", max_length=120)
    budget: str | None = Field(default=None, max_length=80)


def _authorized(provided: str | None, expected: str | None) -> bool:
    return bool(provided and expected and hmac.compare_digest(provided, expected))


def _payment_from_session(session: dict) -> dict:
    customer = session.get("customer_details") or {}
    amount_minor = int(session.get("amount_total") or 0)
    metadata = session.get("metadata") or {}
    requested_tier = str(metadata.get("tier") or "").strip().lower()
    tier = requested_tier if requested_tier in ALLOWED_TIERS else TIER_BY_AMOUNT.get(amount_minor, "unmapped")
    return {
        "payment_id": str(session.get("payment_intent") or session.get("id") or ""),
        "checkout_session_id": str(session.get("id") or ""),
        "customer_name": customer.get("name"),
        "customer_email": customer.get("email"),
        "customer_phone": customer.get("phone"),
        "tier": tier,
        "amount_minor": amount_minor,
        "currency": str(session.get("currency") or "").upper(),
    }


def create_app(settings: Settings | None = None, store: EventStore | None = None) -> FastAPI:
    settings = settings or Settings.from_env()
    store = store or EventStore(settings.database_path)
    app = FastAPI(
        title="Laboratorio Asistente IA — Automation Engine",
        description="Recepción segura y trazable de leads y pagos para la cohorte.",
        version="1.1.0",
    )

    @app.get("/")
    @app.get("/health")
    def health_check() -> dict:
        return {
            "status": "online",
            "environment": settings.environment,
            "ready_for_production": settings.production_ready,
            "components": settings.component_status(),
        }

    @app.post("/webhook/leads", status_code=status.HTTP_202_ACCEPTED)
    async def receive_lead(
        lead: LeadInbound,
        background_tasks: BackgroundTasks,
        x_webhook_secret: str | None = Header(default=None, alias="X-Webhook-Secret"),
    ) -> dict:
        if settings.internal_webhook_secret and not _authorized(
            x_webhook_secret, settings.internal_webhook_secret
        ):
            raise HTTPException(status_code=401, detail="Webhook no autorizado")
        if settings.is_production and not settings.internal_webhook_secret:
            raise HTTPException(status_code=503, detail="Autenticación del webhook no configurada")

        payload = lead.model_dump()
        payload["lead_id"] = f"lead_{uuid4().hex}"
        store.record_lead(payload["lead_id"], payload)
        background_tasks.add_task(dispatch_lead, payload, settings)
        return {"status": "accepted", "lead_id": payload["lead_id"]}

    @app.post("/webhook/stripe", status_code=status.HTTP_202_ACCEPTED)
    @app.post("/webhook/stripe-payment", status_code=status.HTTP_202_ACCEPTED, include_in_schema=False)
    async def receive_stripe_payment(
        request: Request,
        background_tasks: BackgroundTasks,
        stripe_signature: str | None = Header(default=None, alias="Stripe-Signature"),
    ) -> dict:
        if not settings.stripe_webhook_secret:
            raise HTTPException(status_code=503, detail="Stripe webhook no configurado")
        if settings.is_production and not settings.onboarding_webhook_url:
            raise HTTPException(status_code=503, detail="Onboarding no configurado")
        if not stripe_signature:
            raise HTTPException(status_code=400, detail="Falta Stripe-Signature")

        raw_body = await request.body()
        try:
            event = stripe.Webhook.construct_event(
                raw_body, stripe_signature, settings.stripe_webhook_secret
            )
        except (ValueError, stripe.error.SignatureVerificationError) as exc:
            raise HTTPException(status_code=400, detail="Firma de Stripe inválida") from exc

        event_data = event.to_dict() if hasattr(event, "to_dict") else dict(event)
        event_type = str(event_data.get("type") or "")
        if event_type not in SUPPORTED_STRIPE_EVENTS:
            return {"status": "ignored", "event_type": event_type}

        event_id = str(event_data.get("id") or "")
        session = dict(event_data["data"]["object"])
        object_id = str(session.get("id") or "")
        if not event_id or not object_id:
            raise HTTPException(status_code=400, detail="Evento de Stripe incompleto")

        payment = _payment_from_session(session)
        if payment["amount_minor"] < 0 or not payment["currency"] or not payment["payment_id"]:
            raise HTTPException(status_code=400, detail="Datos de pago incompletos")

        created = store.record_payment_once(
            event_id=event_id,
            event_type=event_type,
            object_id=object_id,
            payment=payment,
        )
        if not created:
            return {"status": "duplicate", "event_id": event_id}

        needs_review = not payment["customer_email"] or payment["tier"] == "unmapped"
        if not needs_review:
            background_tasks.add_task(dispatch_student_onboarding, payment, settings)
        else:
            logger.warning("Pago requiere revisión manual (event_id=%s)", event_id)

        return {
            "status": "accepted",
            "event_id": event_id,
            "onboarding": "manual_review" if needs_review else "queued",
        }

    return app


app = create_app()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", "8000")))
