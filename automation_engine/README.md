# Automation Engine - Fase 1B

Motor auditable para una sola oferta:

- **Producto:** Laboratorio en vivo + plantillas.
- **Código:** `laboratorio-ia-piloto`.
- **Precio:** MXN $1,000, pago único.
- **Entrega:** invitación a Google Classroom.

## Garantías del flujo

- Verifica `Stripe-Signature` sobre el cuerpo original.
- Sólo crea matrícula cuando Stripe reporta `payment_status=paid`.
- Exige producto, monto y moneda exactos.
- Un `payment_id` produce como máximo una matrícula y un job.
- Reintenta onboarding a los 5 minutos, 30 minutos y 2 horas.
- Después de cuatro fallos marca la matrícula `failed` y emite una alerta.
- Registra evidencia separada de invitación y membresía activa.
- Nunca considera una invitación de Classroom como acceso ya aceptado.

## Estados

`enrollments.status`:

```text
pending -> onboarding_requested -> invited -> active
                              \-> failed
```

`onboarding_jobs.status`:

```text
received -> processing -> delivered
                      \-> failed -> retry
```

## Inicio local

Requiere Python 3.10 o superior.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r automation_engine/requirements-dev.txt
cp automation_engine/.env.example .env
uvicorn automation_engine.orchestrator:app --reload
```

Abre `http://localhost:8000/health` para confirmar la oferta y la preparación por componente.

## Pruebas

```bash
python -m pytest -q
```

## Contrato Stripe

El Payment Link de prueba debe:

1. Cobrar exactamente `100000` centavos de MXN.
2. Ser de pago único.
3. Recopilar correo electrónico.
4. Incluir `metadata.product_code=laboratorio-ia-piloto`.
5. Enviar `checkout.session.completed` y `checkout.session.async_payment_succeeded` al endpoint `/webhook/stripe`.

Stripe copia la metadata del Payment Link a la Checkout Session. Consulta la [documentación oficial de metadata](https://docs.stripe.com/metadata) y la [verificación de firmas](https://docs.stripe.com/webhooks/signature).

## Contrato n8n

El motor envía al workflow 03:

```json
{
  "event": "student.onboarding.requested",
  "event_key": "student.onboarding.requested:pi_123",
  "enrollment_id": "enr_123",
  "payment_id": "pi_123",
  "email": "alumno@example.com",
  "product_code": "laboratorio-ia-piloto",
  "course_id": "123456789"
}
```

Respuesta aceptada:

```json
{
  "status": "delivered",
  "delivery_state": "invited",
  "external_id": "invitation_123"
}
```

Si el usuario ya era miembro, `delivery_state` será `active`. Cualquier respuesta sin `external_id` se trata como fallo y se reintenta.

## Procesamiento y reconciliación

- `POST /internal/onboarding/process`: procesa jobs vencidos; debe ejecutarse periódicamente.
- `GET /internal/onboarding/invited`: lista invitaciones aún no confirmadas.
- `POST /webhook/onboarding-membership`: registra evidencia de membresía activa.

Los tres endpoints requieren `X-Webhook-Secret`.

## Workflows incluidos

- `03_google_classroom_onboarding.json`: comprueba membresía/invitación antes de crear otra.
- `04_google_classroom_membership_reconciliation.json`: confirma cada cinco minutos quién ya aceptó.
- `05_operational_alerts_telegram.json`: notifica fallos terminales.

Consulta [PHASE_1B_SETUP.md](../workflows/PHASE_1B_SETUP.md) para importación, credenciales y prueba de salida.
