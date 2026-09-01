"""Configuración explícita del motor de automatización."""

from dataclasses import dataclass
import os


def _clean(value: str | None) -> str | None:
    value = (value or "").strip()
    return value or None


@dataclass(frozen=True)
class Settings:
    environment: str = "development"
    database_path: str = "automation_engine/data/automation.db"
    internal_webhook_secret: str | None = None
    stripe_webhook_secret: str | None = None
    onboarding_webhook_url: str | None = None
    onboarding_webhook_token: str | None = None
    lead_webhook_url: str | None = None
    lead_webhook_token: str | None = None
    alert_webhook_url: str | None = None
    alert_webhook_token: str | None = None
    product_code: str = "laboratorio-ia-piloto"
    product_amount_minor: int = 100_000
    product_currency: str = "MXN"
    google_classroom_course_id: str | None = None

    def __post_init__(self) -> None:
        if self.environment not in {"development", "production"}:
            raise ValueError("APP_ENV debe ser 'development' o 'production'")

    @classmethod
    def from_env(cls) -> "Settings":
        return cls(
            environment=os.getenv("APP_ENV", "development").strip().lower(),
            database_path=os.getenv(
                "DATABASE_PATH", "automation_engine/data/automation.db"
            ).strip(),
            internal_webhook_secret=_clean(os.getenv("INTERNAL_WEBHOOK_SECRET")),
            stripe_webhook_secret=_clean(os.getenv("STRIPE_WEBHOOK_SECRET")),
            onboarding_webhook_url=_clean(os.getenv("ONBOARDING_WEBHOOK_URL")),
            onboarding_webhook_token=_clean(os.getenv("ONBOARDING_WEBHOOK_TOKEN")),
            lead_webhook_url=_clean(os.getenv("LEAD_WEBHOOK_URL")),
            lead_webhook_token=_clean(os.getenv("LEAD_WEBHOOK_TOKEN")),
            alert_webhook_url=_clean(os.getenv("ALERT_WEBHOOK_URL")),
            alert_webhook_token=_clean(os.getenv("ALERT_WEBHOOK_TOKEN")),
            product_code=os.getenv("PRODUCT_CODE", "laboratorio-ia-piloto").strip(),
            product_amount_minor=int(os.getenv("PRODUCT_AMOUNT_MINOR", "100000")),
            product_currency=os.getenv("PRODUCT_CURRENCY", "MXN").strip().upper(),
            google_classroom_course_id=_clean(os.getenv("GOOGLE_CLASSROOM_COURSE_ID")),
        )

    @property
    def is_production(self) -> bool:
        return self.environment == "production"

    @property
    def production_ready(self) -> bool:
        return all(
            (
                self.internal_webhook_secret,
                self.stripe_webhook_secret,
                self.onboarding_webhook_url,
                self.google_classroom_course_id,
                self.alert_webhook_url,
            )
        )

    def component_status(self) -> dict[str, bool]:
        return {
            "lead_webhook_auth": bool(self.internal_webhook_secret),
            "stripe_signature_verification": bool(self.stripe_webhook_secret),
            "onboarding_delivery": bool(self.onboarding_webhook_url),
            "lead_delivery": bool(self.lead_webhook_url),
            "alerts": bool(self.alert_webhook_url),
            "google_classroom": bool(self.google_classroom_course_id),
        }
