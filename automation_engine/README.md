# Automation Engine — Piloto simple

El piloto valida una sola experiencia:

```text
Payment Link de Stripe → webhook firmado → pago registrado → success.html → Google Classroom
```

- Producto: `laboratorio-ia-piloto`.
- Cobro: MXN $1,000, pago único.
- Entrega: botón directo al Google Classroom después del checkout.

No requiere n8n, Google Cloud ni OAuth para funcionar.

## Qué valida el motor

- Firma original `Stripe-Signature`.
- Pago con estado `paid`.
- Producto, monto y moneda exactos.
- Un evento duplicado no duplica el registro del pago.
- Eventos Test Mode no pueden operar producción.

## Configuración mínima

```bash
cp automation_engine/.env.example .env
uvicorn automation_engine.orchestrator:app --reload
```

Configura en Stripe Test Mode un endpoint hacia `/webhook/stripe` y suscríbelo a `checkout.session.completed` y `checkout.session.async_payment_succeeded`.

El Payment Link debe cobrar MXN $1,000 y llevar `metadata.product_code=laboratorio-ia-piloto`. Configura su URL de éxito para volver a `landing_portal/success.html` del sitio desplegado.

## Importante

El botón de Classroom entrega el enlace del aula después del checkout; no prueba una membresía ni impide por sí mismo que alguien reenvíe el enlace. El piloto mide pago y llegada al aula. La matrícula automática y la evidencia de aceptación se retoman sólo si las ventas validan la oferta.

## Pruebas

```bash
python -m pytest -q
```
