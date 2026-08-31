# Automation Engine

Base segura y comprobable para recibir leads, verificar pagos de Stripe y disparar el onboarding mediante n8n, Make o Zapier.

## Qué cambia

- Verifica la firma `Stripe-Signature` sobre el cuerpo original de la solicitud.
- Procesa únicamente `checkout.session.completed`.
- Evita onboarding duplicado con un registro idempotente en SQLite.
- Protege el webhook de leads con `X-Webhook-Secret`.
- Persiste leads, pagos y eventos para auditoría.
- Reporta `ready_for_production=false` hasta que la configuración mínima exista.
- Deja de simular invitaciones o mensajes exitosos.

## Inicio local

Requiere Python 3.10 o superior.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r automation_engine/requirements-dev.txt
cp automation_engine/.env.example .env
uvicorn automation_engine.orchestrator:app --reload
```

Abre `http://localhost:8000/docs` para probar la API y `http://localhost:8000/health` para revisar el estado de configuración.

## Pruebas

```bash
python -m pytest -q
```

## Configurar Stripe

1. Crea un endpoint de webhook que apunte a `https://TU_DOMINIO/webhook/stripe`.
2. Suscríbelo solamente a `checkout.session.completed`.
3. Copia su signing secret en `STRIPE_WEBHOOK_SECRET`.
4. Agrega `metadata[tier]` con `tripwire`, `bootcamp` o `accelerator` a cada Checkout Session/Payment Link.
5. Usa Stripe CLI para reenviar eventos durante desarrollo:

```bash
stripe listen --forward-to localhost:8000/webhook/stripe
stripe trigger checkout.session.completed
```

Stripe puede reenviar un evento, por eso el `event.id` se registra antes de programar el onboarding. Consulta la [guía oficial de firmas](https://docs.stripe.com/webhooks/signature) y las [buenas prácticas de webhooks](https://docs.stripe.com/webhooks).

## Conectar onboarding

`ONBOARDING_WEBHOOK_URL` debe ser un webhook autenticado de n8n, Make o Zapier. Recibirá:

```json
{
  "event": "student.onboarding.requested",
  "payment": {
    "payment_id": "pi_...",
    "customer_email": "alumno@example.com",
    "tier": "bootcamp",
    "amount_minor": 29700,
    "currency": "MXN"
  }
}
```

Configura `ONBOARDING_WEBHOOK_TOKEN` si el destino acepta `Authorization: Bearer ...`. En producción, la API rechaza pagos temporalmente si el destino de onboarding no está configurado, de modo que Stripe pueda reintentar el evento.

## Estado real

Esta base deja listo el ingreso seguro de eventos. Todavía faltan para un lanzamiento completo: desplegar la API, crear el flujo receptor de onboarding, configurar Payment Links reales, ejecutar una compra de prueba y definir monitoreo/alertas.
