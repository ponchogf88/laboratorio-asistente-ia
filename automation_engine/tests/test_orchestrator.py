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
INTERNAL_SECRET = "internal-test-secret"


def _client(tmp_path, **overrides):
    values = {"environment": "development", "database_path": str(tmp_path / "events.db"), "internal_webhook_secret": INTERNAL_SECRET, "stripe_webhook_secret": STRIPE_SECRET, "stripe_payment_link_id": "plink_live_laboratorio", "classroom_join_url": "https://classroom.google.com/c/example"}
    values.update(overrides)
    settings = Settings(**values)
    return TestClient(create_app(settings, EventStore(settings.database_path))), settings


def _stripe_payload(event_id="evt_001", event_type="checkout.session.completed", **changes):
    session = {"id": "cs_test_001", "payment_intent": "pi_test_001", "payment_link": "plink_live_laboratorio", "payment_status": "paid", "amount_total": 100000, "currency": "mxn", "metadata": {}, "customer_details": {"name": "Persona de Prueba", "email": "test@example.com"}}
    session.update(changes)
    return {"id": event_id, "type": event_type, "data": {"object": session}}


def _post_stripe(client, payload):
    raw = json.dumps(payload, separators=(",", ":")).encode()
    timestamp = int(time.time())
    digest = hmac.new(STRIPE_SECRET.encode(), f"{timestamp}.".encode() + raw, hashlib.sha256).hexdigest()
    return client.post("/webhook/stripe", content=raw, headers={"Stripe-Signature": f"t={timestamp},v1={digest}", "Content-Type": "application/json"})


def test_health_reports_simple_classroom_delivery(tmp_path):
    client, _ = _client(tmp_path)
    assert client.get("/health").json()["offer"]["delivery"] == "classroom_join_link"


def test_leads_require_shared_secret(tmp_path):
    client, settings = _client(tmp_path)
    assert client.post("/webhook/leads", json={"source": "website_optin", "full_name": "Ada"}).status_code == 401
    assert client.post("/webhook/leads", json={"source": "website_optin", "full_name": "Ada"}, headers={"X-Webhook-Secret": INTERNAL_SECRET}).status_code == 202
    with sqlite3.connect(settings.database_path) as connection:
        assert connection.execute("SELECT COUNT(*) FROM leads").fetchone()[0] == 1


def test_stripe_requires_valid_signature(tmp_path):
    client, _ = _client(tmp_path)
    assert client.post("/webhook/stripe", json=_stripe_payload()).status_code == 400


def test_paid_offer_registers_payment_once_and_returns_success_access(tmp_path):
    client, settings = _client(tmp_path)
    assert _post_stripe(client, _stripe_payload()).json()["access"] == "success_page"
    assert _post_stripe(client, _stripe_payload()).json()["status"] == "duplicate"
    with sqlite3.connect(settings.database_path) as connection:
        assert connection.execute("SELECT COUNT(*) FROM payments").fetchone()[0] == 1


def test_unpaid_checkout_waits(tmp_path):
    client, settings = _client(tmp_path)
    assert _post_stripe(client, _stripe_payload(payment_status="unpaid")).json()["status"] == "awaiting_payment"
    with sqlite3.connect(settings.database_path) as connection:
        assert connection.execute("SELECT COUNT(*) FROM payments").fetchone()[0] == 1


def test_wrong_offer_requires_manual_review(tmp_path):
    client, _ = _client(tmp_path)
    assert _post_stripe(client, _stripe_payload(amount_total=29700)).json()["onboarding"] == "manual_review"


def test_production_rejects_test_mode_event(tmp_path):
    client, _ = _client(tmp_path, environment="production")
    assert _post_stripe(client, _stripe_payload()).status_code == 400


def test_unknown_environment_is_rejected(tmp_path):
    try:
        _client(tmp_path, environment="prod")
    except ValueError:
        pass
    else:
        raise AssertionError("APP_ENV ambiguo no debe ser permitido")
