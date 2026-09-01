"""Persistencia SQLite para pagos, matrículas, onboarding y evidencia."""

from contextlib import closing
import json
from pathlib import Path
import sqlite3
from typing import Any
from uuid import uuid4


RETRY_DELAYS_SECONDS = (300, 1800, 7200)


class EventStore:
    def __init__(self, database_path: str):
        self.database_path = database_path
        if database_path != ":memory:":
            Path(database_path).parent.mkdir(parents=True, exist_ok=True)
        self._initialize()

    def _connect(self) -> sqlite3.Connection:
        connection = sqlite3.connect(self.database_path, timeout=10)
        connection.row_factory = sqlite3.Row
        connection.execute("PRAGMA foreign_keys = ON")
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
                    product_code TEXT NOT NULL,
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
                CREATE TABLE IF NOT EXISTS enrollments (
                    id TEXT PRIMARY KEY,
                    payment_id TEXT NOT NULL UNIQUE,
                    email TEXT NOT NULL,
                    product_code TEXT NOT NULL,
                    status TEXT NOT NULL CHECK(status IN ('pending','onboarding_requested','invited','active','failed')),
                    external_reference TEXT,
                    last_error TEXT,
                    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY(payment_id) REFERENCES payments(payment_id)
                );
                CREATE TABLE IF NOT EXISTS onboarding_jobs (
                    id TEXT PRIMARY KEY,
                    enrollment_id TEXT NOT NULL UNIQUE,
                    event_key TEXT NOT NULL UNIQUE,
                    status TEXT NOT NULL CHECK(status IN ('received','processing','delivered','failed')),
                    attempt_count INTEGER NOT NULL DEFAULT 0,
                    next_attempt_at TEXT,
                    external_reference TEXT,
                    last_error TEXT,
                    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    delivered_at TEXT,
                    FOREIGN KEY(enrollment_id) REFERENCES enrollments(id)
                );
                CREATE TABLE IF NOT EXISTS delivery_evidence (
                    id TEXT PRIMARY KEY,
                    enrollment_id TEXT NOT NULL,
                    evidence_type TEXT NOT NULL,
                    payload_json TEXT NOT NULL,
                    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY(enrollment_id) REFERENCES enrollments(id)
                );
                CREATE INDEX IF NOT EXISTS idx_jobs_due
                ON onboarding_jobs(status, next_attempt_at);
                CREATE INDEX IF NOT EXISTS idx_enrollments_status
                ON enrollments(status);
                """
            )
            self._migrate_phase_1a_payments(connection)
            connection.commit()

    @staticmethod
    def _migrate_phase_1a_payments(connection: sqlite3.Connection) -> None:
        columns = {
            row["name"]
            for row in connection.execute("PRAGMA table_info(payments)").fetchall()
        }
        if "product_code" not in columns:
            connection.execute(
                "ALTER TABLE payments ADD COLUMN product_code TEXT NOT NULL DEFAULT 'unmapped'"
            )

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
                payment_columns = {
                    row["name"]
                    for row in connection.execute("PRAGMA table_info(payments)").fetchall()
                }
                values = (
                    payment["payment_id"],
                    event_id,
                    payment.get("customer_email"),
                    payment["product_code"],
                    payment["amount_minor"],
                    payment["currency"],
                    json.dumps(payment, ensure_ascii=False),
                )
                if "tier" in payment_columns:
                    connection.execute(
                        """
                        INSERT INTO payments
                        (payment_id, event_id, customer_email, tier, product_code,
                         amount_minor, currency, payload_json)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                        ON CONFLICT(payment_id) DO UPDATE SET
                            event_id=excluded.event_id,
                            customer_email=excluded.customer_email,
                            tier=excluded.tier,
                            product_code=excluded.product_code,
                            amount_minor=excluded.amount_minor,
                            currency=excluded.currency,
                            payload_json=excluded.payload_json
                        """,
                        values[:3] + (payment["product_code"],) + values[3:],
                    )
                else:
                    connection.execute(
                        """
                        INSERT INTO payments
                        (payment_id, event_id, customer_email, product_code,
                         amount_minor, currency, payload_json)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                        ON CONFLICT(payment_id) DO UPDATE SET
                            event_id=excluded.event_id,
                            customer_email=excluded.customer_email,
                            product_code=excluded.product_code,
                            amount_minor=excluded.amount_minor,
                            currency=excluded.currency,
                            payload_json=excluded.payload_json
                        """,
                        values,
                    )
                connection.commit()
                return True
            except Exception:
                connection.rollback()
                raise

    def create_enrollment_once(self, payment: dict[str, Any]) -> dict[str, Any]:
        enrollment_id = f"enr_{uuid4().hex}"
        job_id = f"job_{uuid4().hex}"
        event_key = f"student.onboarding.requested:{payment['payment_id']}"
        with closing(self._connect()) as connection:
            try:
                connection.execute("BEGIN IMMEDIATE")
                connection.execute(
                    """
                    INSERT OR IGNORE INTO enrollments
                    (id, payment_id, email, product_code, status)
                    VALUES (?, ?, ?, ?, 'pending')
                    """,
                    (
                        enrollment_id,
                        payment["payment_id"],
                        payment["customer_email"],
                        payment["product_code"],
                    ),
                )
                row = connection.execute(
                    "SELECT * FROM enrollments WHERE payment_id = ?",
                    (payment["payment_id"],),
                ).fetchone()
                connection.execute(
                    """
                    INSERT OR IGNORE INTO onboarding_jobs
                    (id, enrollment_id, event_key, status, next_attempt_at)
                    VALUES (?, ?, ?, 'received', CURRENT_TIMESTAMP)
                    """,
                    (job_id, row["id"], event_key),
                )
                connection.execute(
                    """
                    UPDATE enrollments
                    SET status=CASE WHEN status='pending' THEN 'onboarding_requested' ELSE status END,
                        updated_at=CURRENT_TIMESTAMP
                    WHERE id=?
                    """,
                    (row["id"],),
                )
                connection.commit()
                return dict(
                    connection.execute(
                        "SELECT * FROM enrollments WHERE id=?", (row["id"],)
                    ).fetchone()
                )
            except Exception:
                connection.rollback()
                raise

    def claim_job(self, enrollment_id: str | None = None) -> dict[str, Any] | None:
        with closing(self._connect()) as connection:
            try:
                connection.execute("BEGIN IMMEDIATE")
                connection.execute(
                    """
                    UPDATE onboarding_jobs
                    SET status='failed', next_attempt_at=CURRENT_TIMESTAMP,
                        last_error='worker_timeout_recovered', updated_at=CURRENT_TIMESTAMP
                    WHERE status='processing' AND updated_at <= datetime('now', '-15 minutes')
                    """
                )
                query = """
                    SELECT j.*, e.email, e.product_code, e.payment_id
                    FROM onboarding_jobs j
                    JOIN enrollments e ON e.id = j.enrollment_id
                    WHERE j.status IN ('received','failed')
                      AND j.next_attempt_at IS NOT NULL
                      AND j.next_attempt_at <= CURRENT_TIMESTAMP
                """
                params: tuple[Any, ...] = ()
                if enrollment_id:
                    query += " AND j.enrollment_id = ?"
                    params = (enrollment_id,)
                query += " ORDER BY j.created_at LIMIT 1"
                row = connection.execute(query, params).fetchone()
                if not row:
                    connection.rollback()
                    return None
                connection.execute(
                    """
                    UPDATE onboarding_jobs
                    SET status='processing', attempt_count=attempt_count+1,
                        updated_at=CURRENT_TIMESTAMP
                    WHERE id=?
                    """,
                    (row["id"],),
                )
                connection.commit()
                claimed = connection.execute(
                    """
                    SELECT j.*, e.email, e.product_code, e.payment_id
                    FROM onboarding_jobs j
                    JOIN enrollments e ON e.id = j.enrollment_id
                    WHERE j.id=?
                    """,
                    (row["id"],),
                ).fetchone()
                return dict(claimed)
            except Exception:
                connection.rollback()
                raise

    def mark_job_delivered(
        self, job: dict[str, Any], external_reference: str, response: dict[str, Any]
    ) -> None:
        delivery_state = response.get("delivery_state", "invited")
        enrollment_status = "active" if delivery_state == "active" else "invited"
        evidence_type = (
            "google_classroom_membership_confirmed"
            if enrollment_status == "active"
            else "google_classroom_invitation_created"
        )
        with closing(self._connect()) as connection:
            connection.execute("BEGIN IMMEDIATE")
            connection.execute(
                """
                UPDATE onboarding_jobs
                SET status='delivered', external_reference=?, last_error=NULL,
                    next_attempt_at=NULL, delivered_at=CURRENT_TIMESTAMP,
                    updated_at=CURRENT_TIMESTAMP
                WHERE id=?
                """,
                (external_reference, job["id"]),
            )
            connection.execute(
                """
                UPDATE enrollments
                SET status=?, external_reference=?, last_error=NULL,
                    updated_at=CURRENT_TIMESTAMP
                WHERE id=?
                """,
                (enrollment_status, external_reference, job["enrollment_id"]),
            )
            self._insert_evidence(
                connection,
                job["enrollment_id"],
                evidence_type,
                response,
            )
            connection.commit()

    def mark_job_failed(self, job: dict[str, Any], error: str) -> bool:
        """Devuelve True cuando el fallo ya es terminal."""
        attempt = int(job["attempt_count"])
        terminal = attempt >= 4
        delay = None if terminal else RETRY_DELAYS_SECONDS[attempt - 1]
        with closing(self._connect()) as connection:
            connection.execute("BEGIN IMMEDIATE")
            if delay is None:
                connection.execute(
                    """
                    UPDATE onboarding_jobs
                    SET status='failed', next_attempt_at=NULL, last_error=?, updated_at=CURRENT_TIMESTAMP
                    WHERE id=?
                    """,
                    (error[:1000], job["id"]),
                )
                connection.execute(
                    """
                    UPDATE enrollments SET status='failed', last_error=?, updated_at=CURRENT_TIMESTAMP
                    WHERE id=?
                    """,
                    (error[:1000], job["enrollment_id"]),
                )
            else:
                connection.execute(
                    """
                    UPDATE onboarding_jobs
                    SET status='failed', next_attempt_at=datetime('now', ?),
                        last_error=?, updated_at=CURRENT_TIMESTAMP
                    WHERE id=?
                    """,
                    (f"+{delay} seconds", error[:1000], job["id"]),
                )
            self._insert_evidence(
                connection,
                job["enrollment_id"],
                "onboarding_attempt_failed",
                {"attempt": attempt, "terminal": terminal, "error": error[:1000]},
            )
            connection.commit()
        return terminal

    def confirm_membership(
        self, enrollment_id: str, external_reference: str, evidence: dict[str, Any]
    ) -> bool:
        with closing(self._connect()) as connection:
            connection.execute("BEGIN IMMEDIATE")
            cursor = connection.execute(
                """
                UPDATE enrollments SET status='active', external_reference=?,
                    last_error=NULL, updated_at=CURRENT_TIMESTAMP
                WHERE id=? AND status IN ('invited','active')
                """,
                (external_reference, enrollment_id),
            )
            if cursor.rowcount:
                self._insert_evidence(
                    connection,
                    enrollment_id,
                    "google_classroom_membership_confirmed",
                    evidence,
                )
            connection.commit()
            return bool(cursor.rowcount)

    def invited_enrollments(self, limit: int = 50) -> list[dict[str, Any]]:
        with closing(self._connect()) as connection:
            rows = connection.execute(
                """
                SELECT id, email, product_code, external_reference, updated_at
                FROM enrollments WHERE status='invited'
                ORDER BY updated_at LIMIT ?
                """,
                (limit,),
            ).fetchall()
            return [dict(row) for row in rows]

    def enrollment(self, enrollment_id: str) -> dict[str, Any] | None:
        with closing(self._connect()) as connection:
            row = connection.execute(
                "SELECT * FROM enrollments WHERE id=?", (enrollment_id,)
            ).fetchone()
            return dict(row) if row else None

    @staticmethod
    def _insert_evidence(
        connection: sqlite3.Connection,
        enrollment_id: str,
        evidence_type: str,
        payload: dict[str, Any],
    ) -> None:
        connection.execute(
            """
            INSERT INTO delivery_evidence (id, enrollment_id, evidence_type, payload_json)
            VALUES (?, ?, ?, ?)
            """,
            (
                f"ev_{uuid4().hex}",
                enrollment_id,
                evidence_type,
                json.dumps(payload, ensure_ascii=False),
            ),
        )
