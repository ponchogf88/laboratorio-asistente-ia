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
    lead_webhook_url: str | None = None
    lead_webhook_token: str | None = None
    product_code: str = "laboratorio-ia-piloto"
    product_amount_minor: int = 100_000
    product_currency: str = "MXN"
    stripe_payment_link_id: str | None = None
    classroom_join_url: str | None = None

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
            lead_webhook_url=_clean(os.getenv("LEAD_WEBHOOK_URL")),
            lead_webhook_token=_clean(os.getenv("LEAD_WEBHOOK_TOKEN")),
            product_code=os.getenv("PRODUCT_CODE", "laboratorio-ia-piloto").strip(),
            product_amount_minor=int(os.getenv("PRODUCT_AMOUNT_MINOR", "100000")),
            product_currency=os.getenv("PRODUCT_CURRENCY", "MXN").strip().upper(),
            stripe_payment_link_id=_clean(os.getenv("STRIPE_PAYMENT_LINK_ID")),
            classroom_join_url=_clean(os.getenv("CLASSROOM_JOIN_URL")),
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
                self.stripe_payment_link_id,
                self.classroom_join_url,
            )
        )

    def component_status(self) -> dict[str, bool]:
        return {
            "lead_webhook_auth": bool(self.internal_webhook_secret),
            "stripe_signature_verification": bool(self.stripe_webhook_secret),
            "payment_link_allowlist": bool(self.stripe_payment_link_id),
            "lead_delivery": bool(self.lead_webhook_url),
            "classroom_link": bool(self.classroom_join_url),
        }
