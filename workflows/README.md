# Workflows n8n (no usados en el piloto actual)

Esta carpeta contiene automatizaciones del Laboratorio Asistente IA. Los archivos JSON se entregan **inactivos**: importar un workflow no equivale a ponerlo en producción.

| Flujo | Propósito | Estado actual |
| --- | --- | --- |
| `01_telegram_gemini_sdr_bot.json` | Captura y calificación BANT por Telegram | Plantilla; requiere credenciales e IDs reales |
| `02_lead_scraper_gemini_enricher.json` | Enriquecimiento B2B | Plantilla; el webhook debe autenticarse antes de exponerlo |
| `03_google_classroom_onboarding.json` | Crea o recupera una invitación de Classroom | Fase 1B; listo para importar, inactivo |
| `04_google_classroom_membership_reconciliation.json` | Reintenta onboarding y confirma membresías | Fase 1B; listo para importar, inactivo |
| `05_operational_alerts_telegram.json` | Alerta fallos terminales | Fase 1B; listo para importar, inactivo |

## Estado del piloto actual

El piloto opera con transferencia SPEI y confirmación manual por WhatsApp. No actives estos workflows, no configures Google OAuth ni n8n como parte de la inscripción inicial.

## Activación futura

1. Configura Stripe Test Mode y el motor FastAPI.
2. Importa los workflows 03, 04 y 05.
3. Asigna credenciales reales, sin editar tokens dentro de los archivos JSON.
4. Realiza una compra de prueba de MXN $1,000.
5. Verifica invitación, aceptación y evidencia de membresía.
6. Activa los workflows sólo después de la prueba completa.

La guía exacta de credenciales, variables y criterio de salida está en [PHASE_1B_SETUP.md](PHASE_1B_SETUP.md).

## Precisión importante

Google Classroom crea una invitación y el alumno debe aceptarla. Por eso el sistema distingue `invited` de `active`; no reporta un acceso como activo hasta comprobar la membresía.
