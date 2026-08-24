# FUNNEL, EMAIL Y NURTURING B2B — ACADEMIA AAA

---

## 1. MAPA COMPLETO DEL FUNNEL

```
[ TIKTOK / INSTAGRAM REELS ]  ← Alcance Masivo (Top of Funnel)
       │ CTA: "Comenta LOBO" / "Link en mi bio"
       ▼
[ TELEGRAM BOT — n8n + Gemini 2.5 ]  ← Captura & Cualificación
       │
       ├── Lead No B2B / Estudiante → [ DISCORD COMUNIDAD ]
       │                                      ↓
       │                             Nurturing → Curso ($297)
       │
       └── Lead B2B Calificado (Hot) → [ CALENDLY/CAL.COM ]
                                              ↓
                                    [ LLAMADA 20 MIN (Zoom) ]
                                              ↓
                                    [ CIERRE $1,500–$3,000 ]
                                              ↓
                                    [ RETAINER $300–$800/mes ]
```

### Tiempos y Tasas de Conversión Objetivo
| Etapa | Métrica | Objetivo |
|-------|---------|----------|
| TikTok View → Clic en link | CTR | 2.5% |
| Clic → Inicio chat Telegram | Conversión | 85% |
| Chat → Completitud del BANT | Tasa | 40% |
| Calificado → Llamada agendada | Conversión | 25% |
| Llamada → Venta cerrada | Close rate | 20% |
| Tiempo del ciclo de venta | Sales cycle | 7–14 días |

---

## 2. SISTEMA DE CALIFICACIÓN BANT AUTOMATIZADO

### Preguntas del Bot (Conversacional, no cuestionario)

**Pregunta de Need (Necesidad):**
> "¡Qué tal! Soy el asistente de Leo. Para no hacerte perder tiempo, ¿qué proceso te quita más horas en tu negocio ahora mismo? (Ej: agendar citas, responder dudas, captar leads...)"

**Pregunta de Authority (Autoridad):**
> "Entendido, eso se puede automatizar con n8n + Gemini. Para saber cómo plantear la solución: ¿tú eres el dueño del negocio o estás investigando para presentarlo a tu equipo?"

**Pregunta de Timeframe (Tiempo):**
> "Montar un agente autónomo para eso toma unos días. ¿Para cuándo te gustaría tener este sistema funcionando? ¿Lo antes posible, en un mes, o solo estás explorando?"

**Pregunta de Budget (Presupuesto):**
> "Última pregunta para pasarte con Leo. Nuestros sistemas inician en $1,500 USD e incluyen integraciones con tus sistemas actuales y soporte. ¿Cuentas con un presupuesto en ese rango?"

### Árbol de Decisión y Scoring

| Factor | Respuesta | Puntos |
|--------|-----------|--------|
| **Need** | Dolor claro y automatizable | +25 |
| **Need** | Dolor vago / exploratorio | +10 |
| **Authority** | Dueño / Tomador de decisión | +25 |
| **Authority** | Empleado / Investigador | +0 |
| **Timeframe** | < 15 días | +25 |
| **Timeframe** | ~1 mes | +15 |
| **Timeframe** | Solo explorando | +5 |
| **Budget** | Sí, lo tengo | +25 |
| **Budget** | Depende del ROI | +15 |
| **Budget** | No, es muy caro | +0 |

**Segmentación:**
- **🔴 Hot Lead (80–100 pts):** Bot envía link de Calendly inmediatamente → "¡Cumples el perfil exacto! Te dejo el calendario privado de Leo para agendar 20 minutos de viabilidad."
- **🟡 Warm Lead (50–79 pts):** Bot avisa a Leo manualmente → "Voy a pasarle tu perfil a Leo. Él te escribirá aquí en las próximas 24 horas."
- **🟢 Cold Lead (<50 pts):** Redirige a Discord → "Genial que explores. El mejor primer paso es nuestra comunidad gratuita de Lobos Automatizadores [Discord Link]."

### Template de Notificación Para Leo
```
🚨 NUEVO LEAD HOT B2B 🚨
Usuario: @[TelegramUser]
Empresa/Nicho: [Extraído por Gemini del contexto]
Dolor principal: [Resumen del Need]
Presupuesto: Confirmado ($1,500+)
Puntaje: [Score]/100
Acción del bot: Se envió link de Calendly.
Sugerencia: Prepara un caso de éxito del mismo nicho para la llamada.
```

---

## 3. PROPUESTAS COMERCIALES B2B — 3 TEMPLATES COMPLETOS

### Template 1: CLÍNICA MÉDICA / ODONTOLÓGICA

**DIAGNÓSTICO:**
El personal de recepción pierde el 60% de su tiempo respondiendo mensajes repetitivos de WhatsApp sobre horarios, precios y disponibilidad. Esto genera retrasos en la atención presencial y pérdida de pacientes fuera del horario laboral.

**LA SOLUCIÓN — "Recepcionista IA 24/7":**
Agente autónomo conectado al WhatsApp Business de la clínica. Interroga síntomas básicos, responde FAQs, verifica disponibilidad en el calendario (Google Calendar/Acuity) y agenda citas automáticamente. Motor: n8n + Gemini 2.5 Flash (costo operativo mensual casi nulo).

**ROI ESTIMADO:**
- Ahorro de 120 horas/mes de staff administrativo (~$1,200 USD)
- Captura de 15% más de citas al responder inmediatamente en noches y fines de semana
- Retorno de inversión en el mes 2

**PRECIO:** $1,800 USD (50% inicio, 50% entrega)
**RETAINER:** $300 USD/mes
**PLAZO:** 14 días hábiles
**INCLUYE:** 1 mes de ajustes finos de prompts post-entrega

---

### Template 2: INMOBILIARIA / BIENES RAÍCES

**DIAGNÓSTICO:**
Llegan decenas de leads de Meta Ads pero los asesores se frustran llamando a prospectos no calificados. La velocidad de contacto (Speed to Lead) supera las 2 horas, perdiendo el interés del prospecto.

**LA SOLUCIÓN — "Broker IA Calificador":**
Agente que contacta al lead vía WhatsApp a los 5 segundos de llenar el formulario en Facebook. Determina zona de interés, presupuesto y método de compra (crédito/contado). Cruza con el inventario de propiedades (Google Sheets o CRM) y envía 3 opciones. Agenda visita con asesor humano solo si el lead califica.

**ROI ESTIMADO:**
- Aumento 300% en velocidad de atención
- Asesores cierran 25% más contratos al hablar solo con prospectos depurados

**PRECIO:** $2,500 USD
**RETAINER:** $500 USD/mes (optimización mensual de prompts según conversaciones)
**PLAZO:** 21 días hábiles
**INCLUYE:** Integración con CRM actual + capacitación del equipo de ventas

---

### Template 3: AGENCIA DE MARKETING / SOFTWARE FACTORY

**DIAGNÓSTICO:**
Cuellos de botella en creación de contenido, reportes a clientes y seguimiento de leads. Herramientas fragmentadas que requieren humanos para "copiar y pegar" datos entre sistemas.

**LA SOLUCIÓN — "Enjambre de Agentes (Swarm AI)":**
Servidor n8n self-hosted corporativo con 3 flujos:
1. **Agente Redactor:** Analiza tendencias y genera borradores de posts
2. **Agente de Reportería:** Extrae datos de Meta/Google Ads, redacta PDF mensual y lo envía al cliente
3. **Agente QA de Leads:** Filtra y califica leads antes de pasarlos al equipo de ventas

Todo orquestado con Gemini 2.5 Pro.

**ROI ESTIMADO:**
- Agendar 5 clientes nuevos/mes sin contratar Copywriter Junior ni Asistente de Cuentas
- Ahorro de $2,000 USD mensuales recurrentes en nómina

**PRECIO:** $3,000 USD
**RETAINER:** $800 USD/mes (monitoreo, actualización de nodos, SLA corporativo)
**PLAZO:** 20 días hábiles
**INCLUYE:** Auditoría técnica + despliegue en VPS propio del cliente (DigitalOcean/Hetzner) + transferencia total del código

---

## 4. 5 WORKFLOWS ADICIONALES DE N8N A CONSTRUIR

| # | Workflow | Propósito | Nodos Principales | Prioridad |
|---|---------|-----------|------------------|-----------|
| 1 | **Motor de Contenido Automático** | Automatizar publicaciones en redes sociales | RSS Feed → Gemini 2.5 → Google Sheets (cola de aprobación) → Telegram (botones Aprobación/Rechazar) → Buffer/Instagram API | 🔴 Alta |
| 2 | **Onboarding VIP post-pago** | Automatizar entrega del servicio tras pago | Stripe Trigger → Google Drive (crear carpeta cliente) → Gmail (bienvenida + recursos) → Discord (asignar rol VIP) | 🟡 Media |
| 3 | **Recuperador de Citas Fantasma** | Rescatar leads que no asisten al Zoom | Calendly Trigger (no-show) → Wait 15 min → WhatsApp API → Gemini 2.5 (mensaje empático de reagendamiento) | 🔴 Alta |
| 4 | **Escáner de Leads en Discord** | Detectar miembros listos para comprar | Discord Trigger (mensaje en canales) → Gemini 2.5 (análisis de intención de compra) → Telegram (alerta a Leo) | 🟢 Baja |
| 5 | **Auditor de Costos API** | Monitorear consumo de Gemini para evitar sorpresas | Cron Node (diario) → HTTP Request (GCP API) → Switch (¿Costo > Umbral?) → Telegram (alerta de gasto excesivo) | 🟡 Media |

---

## 5. SISTEMA DE RETENCIÓN DE CLIENTES B2B

### Onboarding (Primeras 2 Semanas)
- **Día 1:** Llamada Kick-off 45 min. Definición de alcances, entrega de roadmap
- **Día 3:** Correo automático con acceso a dashboard de seguimiento (Notion compartido)
- **Día 7:** Video Loom de 3 minutos mostrando los nodos corriendo en pruebas
- **Día 14:** Llamada de Entrega y Capacitación. Pruebas en vivo.

### Template de Reporte Mensual (Automatizado via n8n)
```
Hola [Nombre del Cliente] 👋

Este es el impacto de tu Agente IA este mes:

📊 Conversaciones manejadas: [Variable A]
⏰ Horas de staff ahorradas estimadas: [Variable B] hrs
🎯 Citas/Leads procesados: [Variable C]
🔐 Actualizaciones de seguridad: n8n v[X], modelo Gemini [Y]

Todo sigue operando a costo de infraestructura $0 gracias
a nuestra arquitectura. Seguimos a tus órdenes.

Leo Gutierrez | Laboratorio Asistente IA
```

### Estrategia de Upsell/Cross-sell
- **Mes 3:** Ofrecer Mantenimiento Proactivo (Retainer $300–$500/mes) para monitoreo de servidores, actualización de nodos y optimización mensual de prompts
- **Mes 6:** Cross-sell "Agente Interno" — Bot conectado al conocimiento de la empresa (RAG con PDFs) para entrenar nuevos empleados o buscar documentos rápidamente

---

*Funnel y nurturing generados por el Enjambre de Marketing de Academia AAA*
