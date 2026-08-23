# 🤖 NOTION DATABASE: ENJAMBRE DE 8 AGENTES IA
> **Propiedades de la Base de Datos en Notion:**  
> `Agente (Title)` | `Motor LLM (Select)` | `Ventana Contexto (Select)` | `Rol Operativo (Text)` | `Trigger (Select)` | `Webhook Destino (URL)` | `Estado (Status)`

---

## 📑 MATRIZ DE AGENTES AUTÓNOMOS

| Agente (Title) | Motor LLM | Ventana Contexto | Rol Operativo | Trigger | Webhook / Canal | Estado |
| :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| **0. Orquestador Maestro** | Google Gemini 2.5 Flash | 1M Tokens | Dirección de operaciones y enrutamiento central. | Eventos Globales | `/webhook/orchestrator` | 🟢 Listo |
| **1. Scraper & Intel** | Google Gemini 2.5 Pro | 2M Tokens | Ingesta masiva de transcripciones y tendencias. | Cron Semanal | `/webhook/scraper` | 🟢 Listo |
| **2. Arquitecto Pedagógico** | Google Gemini 2.5 Pro | 2M Tokens | Mantenimiento de temarios y control de JSONs. | On-Demand | `#academia-updates` | 🟢 Listo |
| **3. Estudio Creativo** | Google Gemini 2.5 Flash | 1M Tokens | Redacción de guiones virales y copys persuasivos. | Cron / Manual | `#estudio-creativo` | 🟢 Listo |
| **4. Growth & Tráfico** | Google Gemini 2.5 Flash | 1M Tokens | Supervisión de CTR y métricas de conversión. | Diario | `/webhook/growth` | 🟢 Listo |
| **5. SDR Conversacional** | Google Gemini 2.5 Flash | 1M Tokens | Despacho de JSONs y calificación BANT. | Telegram / WhatsApp | `/webhook/telegram-sdr` | 🟢 Listo |
| **6. Conversión B2B** | Google Gemini 2.5 Pro | 2M Tokens | Diagnóstico de empresas y propuestas $1,500+. | Lead Score >= 70 | `#leads-vip` | 🟢 Listo |
| **7. Soporte Técnico RAG** | Google Gemini 2.5 Flash | 1M Tokens | Mentoría y debugging en Discord con pgvector. | Mensaje en Discord | `#dudas-n8n` | 🟢 Listo |
