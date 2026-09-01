# Fase 1B - Activación de Google Classroom

Los workflows se entregan **inactivos** y sin credenciales. Importarlos no debe activar ningún webhook ni enviar invitaciones.

## 1. Preparar Google Classroom

1. Crea el curso `Laboratorio IA - Piloto` con la cuenta que será profesora.
2. Conserva el ID numérico del curso.
3. En Google Cloud habilita Google Classroom API.
4. Configura OAuth 2.0 en n8n usando la cuenta profesora.
5. Autoriza el scope mínimo `https://www.googleapis.com/auth/classroom.rosters`.

Google exige autorización OAuth y `invitations.create` crea una invitación única por usuario/curso. Una invitación todavía no prueba que el alumno la aceptó.

Fuentes: [Google Classroom invitations.create](https://developers.google.com/workspace/classroom/reference/rest/v1/invitations/create) y [scopes oficiales](https://developers.google.com/workspace/classroom/guides/auth).

## 2. Importar workflows

Importa, en este orden:

1. `03_google_classroom_onboarding.json`
2. `04_google_classroom_membership_reconciliation.json`
3. `05_operational_alerts_telegram.json`

Después de importar, reemplaza las referencias `REPLACE_ON_IMPORT` seleccionando credenciales reales desde la interfaz de n8n.

## 3. Credenciales

| Nombre sugerido | Tipo n8n | Uso |
| --- | --- | --- |
| Google Classroom OAuth2 | Google OAuth2 API genérica | Consultar alumnos y crear invitaciones |
| Laboratorio Onboarding Bearer | Header Auth | Proteger workflow 03 |
| Laboratorio Internal Secret | Header Auth | Llamar endpoints internos de FastAPI |
| Laboratorio Alert Bearer | Header Auth | Proteger workflow 05 |
| Laboratorio Telegram Bot | Telegram API | Alertar al administrador |

Para los Header Auth que llaman FastAPI usa:

```text
Name: X-Webhook-Secret
Value: el mismo INTERNAL_WEBHOOK_SECRET del motor
```

Para los webhooks receptores usa `Authorization: Bearer ...` y conserva el token correspondiente en el motor.

## 4. Variables n8n

Configura:

```text
AUTOMATION_ENGINE_URL=https://api.tu-dominio.example
ADMIN_CHAT_ID=tu_chat_id_de_telegram
```

## 5. Activación segura

1. Activa workflow 05 y copia su Production URL a `ALERT_WEBHOOK_URL`.
2. Activa workflow 03 y copia su Production URL a `ONBOARDING_WEBHOOK_URL`.
3. Despliega/reinicia FastAPI con todas las variables.
4. Comprueba `/health`: debe mostrar la oferta correcta y `ready_for_production=true`.
5. Activa workflow 04.

## 6. Criterio de salida

La Fase 1B sólo termina cuando una compra en Stripe Test Mode produce:

1. Firma válida.
2. Pago `paid` de MXN $1,000.
3. Una sola matrícula.
4. Una invitación de Classroom con referencia externa.
5. Evidencia `google_classroom_invitation_created`.
6. Tras aceptar la invitación, estado `active`.
7. Evidencia `google_classroom_membership_confirmed`.
8. Repetir el evento no crea una segunda matrícula ni invitación.

Si el alumno no acepta la invitación, el estado correcto es `invited`, no `active`.
