# 🚀 Guía de Despliegue de Workflows n8n con Telegram y Google Gemini AI

Bienvenido a la bóveda de automatización del **Laboratorio de Asistente IA**. En esta carpeta encontrarás los workflows profesionales listos para importar y ejecutar en cualquier instancia de **n8n** (n8n Cloud, Docker local, Railway, Render o VPS).

---

## 📦 Contenido del Paquete

| Archivo | Nombre del Flujo | Descripción | Nivel |
| :--- | :--- | :--- | :--- |
| [`01_telegram_gemini_sdr_bot.json`](file:///C:/Users/USUARIO/laboratorio-asistente-ia/workflows/01_telegram_gemini_sdr_bot.json) | **Telegram Gemini SDR Bot** | Bot conversacional en Telegram que escucha `/start`, entrega el Lead Magnet, califica prospectos con marco **BANT** usando Gemini 2.5 Flash, filtra leads de alto valor y los registra en Google Sheets enviando alertas al admin. | Producción |
| [`02_lead_scraper_gemini_enricher.json`](file:///C:/Users/USUARIO/laboratorio-asistente-ia/workflows/02_lead_scraper_gemini_enricher.json) | **Lead Scraper & Gemini Pro Enricher** | Motor de enriquecimiento B2B que recibe datos de empresas por Webhook o trigger manual, analiza puntos de dolor con Gemini Pro, redacta Cold Emails con marco PAS y genera propuestas personalizadas. | Producción |

---

## 🛠️ Requisitos Previos

1. **Instancia de n8n** (v1.0 o superior).
2. **Cuenta de Telegram** (para crear el bot con `@BotFather`).
3. **Cuenta de Google** (para Google AI Studio y Google Sheets).

---

## 📥 Paso 1: Cómo importar los Workflows en n8n

Tienes dos métodos rápidos para importar los archivos JSON a tu n8n:

### Método A: Importar desde Archivo (Recomendado)
1. Abre tu panel de control de n8n.
2. En la barra lateral izquierda, haz clic en **Workflows** y luego en **+ Add workflow** (o abre un canvas nuevo).
3. Haz clic en el menú de los tres puntos `⋮` (arriba a la derecha del canvas).
4. Selecciona **Import from File**.
5. Elige el archivo `01_telegram_gemini_sdr_bot.json` o `02_lead_scraper_gemini_enricher.json`.
6. ¡Listo! El diagrama completo aparecerá en tu pantalla.

### Método B: Copiar y Pegar directo al Canvas
1. Abre el archivo JSON en cualquier editor de texto (VS Code, Bloc de notas) o desde GitHub.
2. Copia todo el contenido (`Ctrl + A` y luego `Ctrl + C`).
3. Haz clic en el lienzo en blanco de n8n y presiona `Ctrl + V`.

---

## 🤖 Paso 2: Obtener el Token Gratuito de Telegram con @BotFather

1. Abre la aplicación de Telegram en tu celular o PC.
2. En el buscador escribe `@BotFather` (asegúrate de que tenga el check azul de verificación).
3. Inicia el chat y envía el comando:
   ```text
   /newbot
   ```
4. Elige un **nombre visible** para tu bot (ejemplo: `Mi Asistente SDR IA`).
5. Elige un **nombre de usuario único** que termine obligatoriamente en `bot` (ejemplo: `mi_agente_sdr_ia_bot`).
6. BotFather te responderá con tu **Token HTTP API**. Tendrá un formato similar a:
   ```text
   7182938491:AAFd83j91_kL29XmN82PqL0ZxyW71abCdEf
   ```
7. *(Opcional)* Configura la descripción de tu bot con:
   ```text
   /setdescription
   /setabouttext
   ```

### Obtener tu Chat ID de Administrador (para recibir alertas):
1. En Telegram busca el bot `@userinfobot` o `@RawDataBot`.
2. Dale a `/start` y te responderá con tu **Id** numérico (ejemplo: `123456789`).
3. Guarda este ID para colocarlo en el nodo de alerta de n8n.

---

## 🧠 Paso 3: Obtener la API Key Gratuita de Google AI Studio (Gemini)

1. Ingresa a **[Google AI Studio](https://aistudio.google.com/)**.
2. Inicia sesión con tu cuenta de Google.
3. Haz clic en el botón azul **Get API key** (arriba a la izquierda).
4. Haz clic en **Create API key in new project** (o selecciona un proyecto de Google Cloud existente).
5. Copia tu clave API (empieza con `AIzaSy...`).
6. *Nota:* Google AI Studio ofrece un nivel gratuito generoso para Gemini 2.5 Flash y Gemini 1.5 Pro sin costo mensual.

---

## ⚙️ Paso 4: Configuración de Credenciales en n8n

### 1. Credencial de Telegram
1. En n8n, ve a **Credentials** > **Add Credential** > busca **Telegram API**.
2. En el campo **Access Token**, pega el Token que te dio `@BotFather`.
3. Haz clic en **Save**.
4. En el nodo `Telegram Trigger` y en los nodos `Telegram Send Message`, selecciona esta credencial.

### 2. API Key de Google Gemini
Puedes configurarla de dos formas:
* **Opción A (Recomendada):** En el nodo `Google Gemini API` (HTTP Request), reemplaza `AIzaSy_TU_API_KEY_AQUI` en la URL por tu API Key real de Google AI Studio.
* **Opción B (Segura para producción):** Declara la variable de entorno `GEMINI_API_KEY` en tu servidor de n8n. El nodo la tomará automáticamente con `{{ $env.GEMINI_API_KEY }}`.

### 3. Credencial de Google Sheets (CRM de Leads)
1. En n8n, ve a **Credentials** > **Add Credential** > **Google Sheets OAuth2 API**.
2. Conecta tu cuenta de Google Drive / Sheets.
3. Crea una hoja de cálculo en Google Drive con las siguientes pestañas y encabezados:

#### Pestaña 1: `Leads_Calificados` (para el Workflow 01)
| Fecha | Chat_ID | Nombre | Usuario_Telegram | Ultimo_Mensaje | Necesidad_Detectada | Presupuesto | Autoridad | Timeline | Lead_Score | Estado |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

#### Pestaña 2: `Leads_Enriquecidos_B2B` (para el Workflow 02)
| Fecha | Empresa | Contacto | Cargo | Email | Industria | Sitio_Web | Desafio_Inicial | Diagnostico | Puntos_Dolor | Solucion_IA | Icebreaker_LinkedIn | Asunto_Principal | Cold_Email_Copy | Score_Fit | Tier_ICP |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

4. En los nodos de Google Sheets, selecciona tu Spreadsheet y la pestaña correspondiente.

---

## 🧪 Paso 5: Pruebas y Activación en Vivo

### Probar el Workflow 01 (Telegram SDR Bot):
1. Abre el workflow en n8n y haz clic en **Test step** en el nodo `Telegram Trigger`.
2. Ve a Telegram y escribe `/start` a tu bot.
3. Observa cómo se ejecuta la rama de bienvenida con el botón de selección y el enlace al recurso.
4. Escribe un mensaje respondiendo con tu tipo de negocio y necesidad (ej: *"Tengo una agencia y quiero automatizar la prospección"*).
5. Gemini analizará el mensaje, responderá en segundos con tono consultivo y registrará el lead si califica.
6. Cuando estés satisfecho con las pruebas, activa el interruptor **Active** (arriba a la derecha) para dejarlo funcionando 24/7.

### Probar el Workflow 02 (Lead Enricher B2B):
1. Abre el workflow y haz clic en **Test step** en el nodo `Al presionar 'Test step'`.
2. Gemini Pro procesará los datos de prueba de la empresa inmobiliaria, generará el diagnóstico de fugas de capital, los 3 puntos de dolor y el Cold Email optimizado.
3. Revisa cómo se guarda la fila en Google Sheets y se responde al Webhook.
4. Para enviarle datos reales desde tu scraper, formulario o CRM, envía una petición POST a la URL del webhook:
   ```bash
   curl -X POST "https://tu-instancia-n8n.com/webhook/enrich-lead" \
     -H "Content-Type: application/json" \
     -d '{
       "company_name": "Clínica Dental Sonrisas",
       "website": "https://clinicasonrisas.com",
       "industry": "Salud y Odontología",
       "contact_name": "Dra. Laura Gómez",
       "contact_role": "Directora Médica",
       "contact_email": "laura@clinicasonrisas.com",
       "company_size": "15 empleados",
       "current_challenge": "Muchos pacientes agendan cita por WhatsApp pero el 35% no asiste porque no hay confirmación automática."
     }'
   ```

---

## 🎯 Personalización del System Prompt BANT

Puedes ajustar las preguntas y criterios de calificación editando el nodo **Preparar Contexto BANT**:
* **Budget:** Modifica los rangos de precios para ajustarlos a tu oferta (ejemplo: High-Ticket > $2,000 USD).
* **Oferta:** Cambia el enlace del Lead Magnet o link de Calendly / Cal.com para agendamiento directo.
* **Tono:** Cambia las directrices de personalidad (formal, informal, consultor técnico, etc.).
