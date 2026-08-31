"""Persistencia SQLite mínima para trazabilidad e idempotencia."""

from contextlib import closing
import json
from pathlib import Path
import sqlite3
from typing import Any


class EventStore:
    def __init__(self, database_path: str):
        self.database_path = database_path
        if database_path != ":memory:":
            Path(database_path).parent.mkdir(parents=True, exist_ok=True)
        self._initialize()

    def _connect(self) -> sqlite3.Connection:
        connection = sqlite3.connect(self.database_path, timeout=10)
        connection.row_factory = sqlite3.Row
        return connection

    def _initialize(self) -> None:
        with closing(self._connect()) as connection:
            connection.executescript(
                """
                CREATE TABLE IF NOT EXISTS webhook_events (
                    event_id TEXT PRIMARY KEY,
                    event_type TEXT NOT NULL,
                    object_id TEXT,
                    received_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                );
                CREATE TABLE IF NOT EXISTS payments (
                    payment_id TEXT PRIMARY KEY,
                    event_id TEXT NOT NULL,
                    customer_email TEXT,
                    tier TEXT NOT NULL,
                    amount_minor INTEGER NOT NULL,
                    currency TEXT NOT NULL,
                    payload_json TEXT NOT NULL,
                    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                );
                CREATE TABLE IF NOT EXISTS leads (
                    lead_id TEXT PRIMARY KEY,
                    source TEXT NOT NULL,
                    full_name TEXT NOT NULL,
                    payload_json TEXT NOT NULL,
                    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                );
                """
            )
            connection.commit()

    def record_lead(self, lead_id: str, payload: dict[str, Any]) -> None:
        with closing(self._connect()) as connection:
            connection.execute(
                "INSERT INTO leads (lead_id, source, full_name, payload_json) VALUES (?, ?, ?, ?)",
                (
                    lead_id,
                    payload["source"],
                    payload["full_name"],
                    json.dumps(payload, ensure_ascii=False),
                ),
            )
            connection.commit()

    def record_payment_once(
        self,
        *,
        event_id: str,
        event_type: str,
        object_id: str,
        payment: dict[str, Any],
    ) -> bool:
        """Registra evento y pago atómicamente; False indica entrega duplicada."""
        with closing(self._connect()) as connection:
            try:
                connection.execute("BEGIN IMMEDIATE")
                cursor = connection.execute(
                    "INSERT OR IGNORE INTO webhook_events (event_id, event_type, object_id) VALUES (?, ?, ?)",
                    (event_id, event_type, object_id),
                )
                if cursor.rowcount == 0:
                    connection.rollback()
                    return False
                connection.execute(
                    """
                    INSERT OR REPLACE INTO payments
                    (payment_id, event_id, customer_email, tier, amount_minor, currency, payload_json)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        payment["payment_id"],
                        event_id,
                        payment.get("customer_email"),
                        payment["tier"],
                        payment["amount_minor"],
                        payment["currency"],
                        json.dumps(payment, ensure_ascii=False),
                    ),
                )
                connection.commit()
                return True
            except Exception:
                connection.rollback()
                raise
