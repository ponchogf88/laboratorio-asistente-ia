# ⚙️ NOTION DATABASE: BÓVEDA DE WORKFLOWS N8N
> **Propiedades de la Base de Datos en Notion:**  
> `Workflow (Title)` | `Archivo JSON (File)` | `Nodos Clave (Multi-select)` | `Modelo IA (Select)` | `Caso de Uso (Text)` | `Estado (Status)`

---

## 📑 CATÁLOGO DE WORKFLOWS N8N

| Workflow (Title) | Archivo JSON | Nodos Clave | Modelo IA | Caso de Uso | Estado |
| :--- | :--- | :--- | :--- | :--- | :---: |
| **01. SDR Telegram + Gemini** | `01_telegram_gemini_sdr_bot.json` | Telegram, Gemini Chat, Google Sheets | Gemini 2.5 Flash | Calificación BANT y entrega de recursos en Telegram. | 🟢 Producción |
| **02. Scraper B2B + Cold Email** | `02_lead_scraper_gemini_enricher.json` | HTTP Request, Gemini 2M, Gmail | Gemini 2.5 Pro | Prospección en frío personalizada para empresas. | 🟢 Producción |
| **03. SDR WhatsApp + Calendly** | `01_agente_sdr_whatsapp_calendly.json` | WhatsApp Cloud API, Calendly | Gemini 2.5 Flash | Agendamiento automático de citas en WhatsApp. | 🟢 Producción |
| **04. Prospección B2B Cold Email** | `02_agente_prospeccion_b2b_email.json` | CSV Ingest, Gemini Web, Smartlead | Gemini 2.5 Pro | Enriquecimiento de listas B2B y personalización. | 🟢 Producción |
| **05. Soporte RAG + pgvector** | `03_agente_soporte_rag_pgvector.json` | Discord, pgvector, Embeddings | Gemini 2.5 Flash | Asistente de dudas técnicas para comunidad Discord. | 🟢 Producción |
| **06. Creador de Contenido Viral** | `04_agente_creador_contenido_viral.json` | YouTube Ingest, Whisper, Gemini | Gemini 2.5 Flash | Transforma 1 video largo en 4 piezas multicanal. | 🟢 Producción |
