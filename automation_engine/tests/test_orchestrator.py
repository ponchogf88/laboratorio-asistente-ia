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


def _successful_delivery(job, settings):
    return {"status": "delivered", "external_id": f"invite_{job['payment_id']}"}


def _client(tmp_path, delivery=_successful_delivery, **overrides):
    values = {
        "environment": "development",
        "database_path": str(tmp_path / "events.db"),
        "internal_webhook_secret": INTERNAL_SECRET,
        "stripe_webhook_secret": STRIPE_SECRET,
        "onboarding_webhook_url": "https://n8n.example/webhook/onboarding",
        "alert_webhook_url": "https://n8n.example/webhook/alerts",
        "google_classroom_course_id": "course_123",
    }
    values.update(overrides)
    settings = Settings(**values)
    store = EventStore(settings.database_path)
    return TestClient(create_app(settings, store, delivery)), settings, store


def _stripe_payload(
    event_id="evt_001",
    event_type="checkout.session.completed",
    amount=100000,
    currency="mxn",
    product_code="laboratorio-ia-piloto",
    payment_status="paid",
):
    return {
        "id": event_id,
        "object": "event",
        "type": event_type,
        "data": {
            "object": {
                "id": "cs_test_001",
                "object": "checkout.session",
                "payment_intent": "pi_test_001",
                "payment_status": payment_status,
                "amount_total": amount,
                "currency": currency,
                "metadata": {"product_code": product_code},
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


def _post_stripe(client, payload):
    raw, signature = _signed(payload)
    return client.post(
        "/webhook/stripe",
        content=raw,
        headers={"Stripe-Signature": signature, "Content-Type": "application/json"},
    )


def test_health_exposes_locked_offer_and_readiness(tmp_path):
    client, _, _ = _client(tmp_path)
    body = client.get("/health").json()
    assert body["ready_for_production"] is True
    assert body["offer"] == {
        "product_code": "laboratorio-ia-piloto",
        "amount_minor": 100000,
        "currency": "MXN",
        "delivery": "google_classroom",
    }


def test_lead_webhook_requires_shared_secret_and_persists(tmp_path):
    client, settings, _ = _client(tmp_path)
    lead = {"source": "website_optin", "full_name": "Ada Lovelace"}
    assert client.post("/webhook/leads", json=lead).status_code == 401
    response = client.post(
        "/webhook/leads",
        json=lead,
        headers={"X-Webhook-Secret": INTERNAL_SECRET},
    )
    assert response.status_code == 202
    with sqlite3.connect(settings.database_path) as connection:
        assert connection.execute("SELECT COUNT(*) FROM leads").fetchone()[0] == 1


def test_stripe_rejects_missing_or_invalid_signature(tmp_path):
    client, _, _ = _client(tmp_path)
    assert client.post("/webhook/stripe", json=_stripe_payload()).status_code == 400
    assert (
        client.post(
            "/webhook/stripe",
            json=_stripe_payload(),
            headers={"Stripe-Signature": "t=1,v1=invalid"},
        ).status_code
        == 400
    )


def test_paid_offer_creates_one_invitation_with_evidence(tmp_path):
    client, settings, _ = _client(tmp_path)
    response = _post_stripe(client, _stripe_payload())
    assert response.status_code == 202
    assert response.json()["onboarding"] == "queued"
    with sqlite3.connect(settings.database_path) as connection:
        connection.row_factory = sqlite3.Row
        enrollment = connection.execute("SELECT * FROM enrollments").fetchone()
        assert enrollment["status"] == "invited"
        assert enrollment["product_code"] == "laboratorio-ia-piloto"
        assert connection.execute("SELECT COUNT(*) FROM onboarding_jobs").fetchone()[0] == 1
        assert connection.execute("SELECT COUNT(*) FROM delivery_evidence").fetchone()[0] == 1


def test_duplicate_stripe_event_does_not_duplicate_enrollment(tmp_path):
    client, settings, _ = _client(tmp_path)
    assert _post_stripe(client, _stripe_payload()).status_code == 202
    duplicate = _post_stripe(client, _stripe_payload())
    assert duplicate.json()["status"] == "duplicate"
    with sqlite3.connect(settings.database_path) as connection:
        assert connection.execute("SELECT COUNT(*) FROM enrollments").fetchone()[0] == 1


def test_second_paid_event_does_not_regress_invited_enrollment(tmp_path):
    client, settings, _ = _client(tmp_path)
    assert _post_stripe(client, _stripe_payload()).json()["onboarding"] == "queued"
    second_event = _stripe_payload(event_id="evt_002")
    response = _post_stripe(client, second_event)
    assert response.json()["onboarding"] == "invited"
    with sqlite3.connect(settings.database_path) as connection:
        assert connection.execute("SELECT status FROM enrollments").fetchone()[0] == "invited"
        assert connection.execute("SELECT COUNT(*) FROM enrollments").fetchone()[0] == 1


def test_unpaid_checkout_waits_and_creates_no_enrollment(tmp_path):
    client, settings, _ = _client(tmp_path)
    response = _post_stripe(client, _stripe_payload(payment_status="unpaid"))
    assert response.json()["status"] == "awaiting_payment"
    with sqlite3.connect(settings.database_path) as connection:
        assert connection.execute("SELECT COUNT(*) FROM enrollments").fetchone()[0] == 0


def test_async_payment_success_creates_enrollment_after_unpaid_checkout(tmp_path):
    client, settings, _ = _client(tmp_path)
    first = _post_stripe(client, _stripe_payload(payment_status="unpaid"))
    assert first.json()["status"] == "awaiting_payment"
    paid = _stripe_payload(
        event_id="evt_002",
        event_type="checkout.session.async_payment_succeeded",
        payment_status="paid",
    )
    second = _post_stripe(client, paid)
    assert second.json()["onboarding"] == "queued"
    with sqlite3.connect(settings.database_path) as connection:
        assert connection.execute("SELECT COUNT(*) FROM payments").fetchone()[0] == 1
        assert connection.execute("SELECT COUNT(*) FROM enrollments").fetchone()[0] == 1
        payload = json.loads(connection.execute("SELECT payload_json FROM payments").fetchone()[0])
        assert payload["payment_status"] == "paid"


def test_wrong_offer_goes_to_manual_review(tmp_path):
    client, settings, _ = _client(tmp_path)
    response = _post_stripe(client, _stripe_payload(amount=29700))
    assert response.json()["onboarding"] == "manual_review"
    with sqlite3.connect(settings.database_path) as connection:
        assert connection.execute("SELECT COUNT(*) FROM enrollments").fetchone()[0] == 0


def test_invitation_becomes_active_only_after_membership_confirmation(tmp_path):
    client, settings, _ = _client(tmp_path)
    enrollment_id = _post_stripe(client, _stripe_payload()).json()["enrollment_id"]
    invited = client.get(
        "/internal/onboarding/invited",
        headers={"X-Webhook-Secret": INTERNAL_SECRET},
    ).json()["enrollments"]
    assert invited[0]["id"] == enrollment_id

    response = client.post(
        "/webhook/onboarding-membership",
        headers={"X-Webhook-Secret": INTERNAL_SECRET},
        json={
            "enrollment_id": enrollment_id,
            "status": "active",
            "external_reference": "student_test@example.com",
            "course_id": "course_123",
            "email": "test@example.com",
        },
    )
    assert response.json()["status"] == "active"
    with sqlite3.connect(settings.database_path) as connection:
        assert connection.execute("SELECT status FROM enrollments").fetchone()[0] == "active"
        assert connection.execute("SELECT COUNT(*) FROM delivery_evidence").fetchone()[0] == 2


def test_failure_is_scheduled_without_claiming_success(tmp_path):
    def fail_delivery(job, settings):
        raise RuntimeError("classroom unavailable")

    client, settings, _ = _client(tmp_path, delivery=fail_delivery)
    _post_stripe(client, _stripe_payload())
    with sqlite3.connect(settings.database_path) as connection:
        row = connection.execute(
            "SELECT status, attempt_count, next_attempt_at FROM onboarding_jobs"
        ).fetchone()
        assert row[0] == "failed"
        assert row[1] == 1
        assert row[2] is not None
        assert connection.execute("SELECT status FROM enrollments").fetchone()[0] == "onboarding_requested"


def test_production_refuses_payment_without_classroom_course(tmp_path):
    client, _, _ = _client(
        tmp_path,
        environment="production",
        google_classroom_course_id=None,
    )
    response = _post_stripe(client, _stripe_payload())
    assert response.status_code == 503


def test_settings_reject_unknown_environment(tmp_path):
    try:
        _client(tmp_path, environment="prod")
    except ValueError as exc:
        assert "APP_ENV" in str(exc)
    else:
        raise AssertionError("Un entorno desconocido no debe desactivar controles de producción")


def test_production_rejects_stripe_test_event(tmp_path):
    client, _, _ = _client(
        tmp_path,
        environment="production",
        onboarding_webhook_url="https://example.test/onboarding",
        alert_webhook_url="https://example.test/alerts",
        google_classroom_course_id="course-123",
    )
    response = _post_stripe(client, _stripe_payload())
    assert response.status_code == 400
    assert "Test Mode" in response.json()["detail"]
