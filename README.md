# ⚡ Laboratorio Asistente IA — Academia AAA

[![n8n](https://img.shields.io/badge/n8n-self--hosted-14b8a6?style=flat-square&logo=n8n)](https://n8n.io)
[![Gemini](https://img.shields.io/badge/Google%20Gemini-2.5%20Pro%2FFlash-8b5cf6?style=flat-square&logo=google)](https://ai.google.dev)
[![Telegram](https://img.shields.io/badge/Bot-@AcademiaIA__Bot-2CA5E0?style=flat-square&logo=telegram)](https://t.me/AcademiaIA_Bot)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)

> **"Sin código. Sin suscripciones de $300. A coste $0."**

Sistema completo de enjambre de 8 agentes autónomos construido con n8n + Google Gemini 2.5. Incluye bot SDR de Telegram, calificación BANT, gestión de comunidad Discord y generación de contenido viral.

---

## 📐 Arquitectura del Enjambre (8 Agentes)

```
┌─────────────────────────────────────────────────────────────┐
│                    ORQUESTADOR (Gemini 2.5 Pro)              │
│                    Agente 0 — Director de Operaciones        │
└──────────────┬──────────────────────────────────────────────┘
               │
    ┌──────────┼──────────┐───────────┬──────────┐
    ▼          ▼          ▼           ▼          ▼
 Agente 1   Agente 2   Agente 3   Agente 4   Agente 5
 Scraper   Pedagógico  Creativo    Growth      SDR
(Gemini    (Gemini    (Gemini    (Gemini    (Gemini
 2.5 Pro)   2.5 Pro)   2.5 Flash) 2.5 Flash) 2.5 Flash)
    │                                          │
    │              ┌──────────┐               │
    │              ▼          ▼               │
    │           Agente 6   Agente 7           │
    │             B2B      Retención          │
    │           (Gemini    (Gemini            │
    └──────────► 2.5 Pro)  2.5 Flash) ◄──────┘
                  │          │
                  ▼          ▼
             Consultoría  Discord
             High-Ticket  Community
```

---

## 🚀 Quick Start

### Requisitos
- [n8n](https://n8n.io) (self-hosted en VPS ~$6/mes, o Docker local)
- [Google AI Studio API Key](https://aistudio.google.com) (gratuita)
- Bot de Telegram creado con [@BotFather](https://t.me/BotFather)
- Google Sheets o cualquier base de datos soportada por n8n

### 1. Clonar el repositorio
```bash
git clone https://github.com/ponchogf88/laboratorio-asistente-ia.git
cd laboratorio-asistente-ia
```

### 2. Configurar variables de entorno
```bash
cp .env.example .env
# Edita .env con tu editor favorito y rellena tus credenciales
```

### 3. Importar workflows en n8n
1. Abre tu instancia de n8n
2. Ve a **Workflows → Import from File**
3. Importa `workflows/01_telegram_gemini_sdr_bot.json`
4. Importa `workflows/02_lead_scraper_gemini_enricher.json`
5. Activa los workflows (toggle ON)

### 4. Abrir el dashboard
```bash
open index.html
# O simplemente arrastra index.html a tu navegador
```

---

## 📁 Estructura del Proyecto

```
laboratorio-asistente-ia/
├── index.html                          # Dashboard interactivo (4 tabs)
├── .env.example                        # Variables de entorno documentadas
├── .gitignore                          # Exclusiones de Git
├── subir-a-github.bat                  # Script de deploy a GitHub (Windows)
│
├── agents/
│   └── AGENTES_CONFIG_Y_PROMPTS.md    # System prompts de los 8 agentes
│
├── curriculum/
│   └── CURSO_MAESTRO_TEMARIO.md       # Temario 5 módulos / 30 días
│
├── funnels/
│   ├── EMBUDO_TELEGRAM_Y_DISCORD.md   # Stack moderno $0
│   └── EMBUDO_MANYCHAT_Y_SKOOL.md     # Stack histórico (referencia)
│
├── marketing_studio/
│   └── GUIONES_VIRALES_Y_ANUNCIOS.md  # Guiones, Meta Ads, Broadcasts
│
├── workflows/
│   ├── README.md                       # Guía de configuración de n8n
│   ├── 01_telegram_gemini_sdr_bot.json # Bot SDR de Telegram
│   └── 02_lead_scraper_gemini_enricher.json # Scraper B2B
│
└── docs/
    └── HISTORICO_STACK_PAGO_MANYCHAT_SKOOL.md
```

---

## 📊 Dashboard — 5 Tabs

| Tab | Funcionalidad |
|-----|--------------|
| 🤖 **Enjambre Chat** | Simula interacción con los 8 agentes en tiempo real |
| 📊 **Funnel** | Visualiza el embudo + Calculadora de ingresos con sliders |
| ⚙️ **Workflows JSON** | Descarga/copia los JSONs de n8n directamente |
| 📚 **Curriculum** | Temario acordeón expandible (5 módulos) |
| 🗝️ **Bóveda Prompts** | System prompts con búsqueda y copy-to-clipboard |

---

## 🛠 Stack Tecnológico

| Componente | Tecnología | Costo |
|------------|-----------|-------|
| Automatización | n8n (self-hosted) | $0 |
| LLM / Agentes | Google Gemini 2.5 Flash/Pro | $0 (tier gratuito) |
| Canal de captura | Telegram Bot API | $0 |
| Comunidad | Discord | $0 |
| CRM / DB | Google Sheets | $0 |
| VPS (opcional) | Hetzner CX22 | ~$6/mes |
| **TOTAL MENSUAL** | | **~$6–$12 USD** |

---

## 🗺 Roadmap

- [x] Arquitectura de 8 agentes diseñada
- [x] System prompts y configuración completa
- [x] Workflows n8n (SDR Bot + Lead Scraper)
- [x] Curriculum 30 días (5 módulos)
- [x] Dashboard interactivo con 5 tabs
- [x] Arsenal de marketing (guiones, copies, SEO)
- [ ] Bot de Telegram activado (@AcademiaIA_Bot)
- [ ] Servidor Discord creado y configurado
- [ ] Primer cliente B2B cerrado
- [ ] Retainer recurrente activo

---

## 🤝 Comunidad

- **Telegram Bot:** [@AcademiaIA_Bot](https://t.me/AcademiaIA_Bot) *(próximamente)*
- **Discord:** La Guarida | Academia AAA *(próximamente)*
- **GitHub:** [@ponchogf88](https://github.com/ponchogf88)

---

## 📄 Licencia

MIT License — Leo Gutierrez / Academia AAA 2026

> *"Deja de operar, empieza a orquestar."* 🐺
