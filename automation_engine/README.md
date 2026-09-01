# Automation Engine — Reservado para automatización futura

El piloto actual no usa este servicio ni Stripe. La validación comercial se hace de forma manual:

```text
Landing → WhatsApp → transferencia SPEI → comprobante → confirmación manual → acceso privado a Classroom
```

- Producto: Laboratorio en Vivo + Plantillas.
- Cobro: MXN $1,000, pago único por transferencia.
- Acceso: se entrega manualmente después de confirmar el comprobante.

No despliegues este servicio, no configures webhooks y no guardes secretos Stripe para esta etapa. El código se conserva como base para una futura automatización cuando el volumen de alumnos la justifique.
