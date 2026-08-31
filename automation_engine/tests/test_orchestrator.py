import hashlib
import hmac
import json
import sqlite3
import time

from fastapi.testclient import TestClient

from automation_engine.config import Settings
from automation_engine.orchestrator import create_app
from automation_engine.storage import EventStore


STRIPE_SECRET = "whsec_test_secret"


def _client(tmp_path, **overrides):
    values = {
        "environment": "development",
        "database_path": str(tmp_path / "events.db"),
        "internal_webhook_secret": "internal-test-secret",
        "stripe_webhook_secret": STRIPE_SECRET,
    }
    values.update(overrides)
    settings = Settings(**values)
    return TestClient(create_app(settings, EventStore(settings.database_path))), settings


def _stripe_payload(event_id="evt_001", event_type="checkout.session.completed"):
    return {
        "id": event_id,
        "object": "event",
        "type": event_type,
        "data": {
            "object": {
                "id": "cs_test_001",
                "object": "checkout.session",
                "payment_intent": "pi_test_001",
                "amount_total": 29700,
                "currency": "mxn",
                "metadata": {"tier": "bootcamp"},
                "customer_details": {
                    "name": "Persona de Prueba",
                    "email": "test@example.com",
                    "phone": "+5215555555555",
                },
            }
        },
    }


def _signed(payload):
    raw = json.dumps(payload, separators=(",", ":")).encode()
    timestamp = int(time.time())
    digest = hmac.new(
        STRIPE_SECRET.encode(), f"{timestamp}.".encode() + raw, hashlib.sha256
    ).hexdigest()
    return raw, f"t={timestamp},v1={digest}"


def test_health_never_claims_production_ready_without_delivery(tmp_path):
    client, _ = _client(tmp_path)
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["ready_for_production"] is False
    assert response.json()["components"]["stripe_signature_verification"] is True


def test_lead_webhook_requires_shared_secret_and_persists(tmp_path):
    client, settings = _client(tmp_path)
    lead = {"source": "website_optin", "full_name": "Ada Lovelace"}

    assert client.post("/webhook/leads", json=lead).status_code == 401
    response = client.post(
        "/webhook/leads",
        json=lead,
        headers={"X-Webhook-Secret": "internal-test-secret"},
    )
    assert response.status_code == 202
    assert response.json()["lead_id"].startswith("lead_")
    with sqlite3.connect(settings.database_path) as connection:
        assert connection.execute("SELECT COUNT(*) FROM leads").fetchone()[0] == 1


def test_stripe_rejects_missing_or_invalid_signature(tmp_path):
    client, _ = _client(tmp_path)
    assert client.post("/webhook/stripe", json=_stripe_payload()).status_code == 400
    assert (
        client.post(
            "/webhook/stripe",
            json=_stripe_payload(),
            headers={"Stripe-Signature": "t=1,v1=invalid"},
        ).status_code
        == 400
    )


def test_stripe_accepts_verified_event_and_deduplicates(tmp_path):
    client, settings = _client(tmp_path)
    raw, signature = _signed(_stripe_payload())
    headers = {"Stripe-Signature": signature, "Content-Type": "application/json"}

    first = client.post("/webhook/stripe", content=raw, headers=headers)
    second = client.post("/webhook/stripe", content=raw, headers=headers)

    assert first.status_code == 202
    assert first.json()["status"] == "accepted"
    assert second.status_code == 202
    assert second.json()["status"] == "duplicate"
    with sqlite3.connect(settings.database_path) as connection:
        assert connection.execute("SELECT COUNT(*) FROM payments").fetchone()[0] == 1


def test_irrelevant_stripe_event_is_ignored(tmp_path):
    client, _ = _client(tmp_path)
    raw, signature = _signed(_stripe_payload(event_type="customer.created"))
    response = client.post(
        "/webhook/stripe",
        content=raw,
        headers={"Stripe-Signature": signature, "Content-Type": "application/json"},
    )
    assert response.status_code == 202
    assert response.json() == {"status": "ignored", "event_type": "customer.created"}


def test_production_refuses_payments_without_onboarding_destination(tmp_path):
    client, _ = _client(tmp_path, environment="production")
    raw, signature = _signed(_stripe_payload())
    response = client.post(
        "/webhook/stripe",
        content=raw,
        headers={"Stripe-Signature": signature, "Content-Type": "application/json"},
    )
    assert response.status_code == 503
