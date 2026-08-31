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
            )
        )

    def component_status(self) -> dict[str, bool]:
        return {
            "lead_webhook_auth": bool(self.internal_webhook_secret),
            "stripe_signature_verification": bool(self.stripe_webhook_secret),
            "onboarding_delivery": bool(self.onboarding_webhook_url),
            "lead_delivery": bool(self.lead_webhook_url),
        }
