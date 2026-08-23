# GUÍA DEL INSTRUCTOR · SESIÓN 2: AGENTE SDR CONVERSACIONAL DE WHATSAPP
## Duración: 90 Minutos (En Vivo) · Modalidad: Taller 100% Práctico

---

## 📋 FICHA TÉCNICA
* **Objetivo de la sesión:** Construir un agente en WhatsApp que converse fluidamente con prospectos, extraiga datos de calificación BANT (Presupuesto, Urgencia, Necesidad) y agende citas automáticamente en Google Calendar.
* **Herramientas utilizadas:** n8n (VPS), WhatsApp Business Cloud API / Webhook, Claude 3.5 Sonnet (Anthropic API), Google Calendar / Cal.com, Airtable.
* **Entregable del alumno:** Flujo `01_agente_sdr_whatsapp_calendly.json` importado y funcionando con su propio número.

---

## ⏱️ GUION MINUTO A MINUTO PARA EL INSTRUCTOR

### [00:00 - 00:15] Apertura, Contexto y Caso de Negocio (15 min)
* **Bienvenida y objetivo:** Explicar el caso de uso real: *"Hoy construiremos el empleado digital que atiende WhatsApp a las 2:00 AM y agenda citas mientras duermes"*.
* **Contraste clave:** Mostrar la diferencia entre un bot de opciones rígidas ("Marca 1 para ventas") vs. un agente con memoria y razonamiento.

### [00:15 - 00:35] Conexión de WhatsApp Cloud API a n8n (20 min)
* **Paso 1:** Configurar el nodo `Webhook` en n8n para recibir mensajes entrantes de Meta.
* **Paso 2:** Explicar cómo extraer el número de teléfono (`from`), el nombre del contacto (`profile.name`) y el texto del mensaje (`body.text`).
* **Demostración en vivo:** El instructor envía un "Hola" a su número de WhatsApp y muestra el nodo de n8n recibiendo los datos en verde.

### [00:35 - 00:55] System Prompting y Calificación BANT con Claude 3.5 (20 min)
* **Estructura del prompt:** Configurar el nodo de LangChain Agent con Claude 3.5 Sonnet.
* **Inyección de instrucciones:**
  ```text
  Eres Sofía, asistente comercial de la empresa [NOMBRE].
  Tu objetivo es calificar al usuario de forma cálida:
  1. Identifica qué servicio necesita.
  2. Pregunta amablemente su presupuesto estimado.
  3. Si el prospecto califica (presupuesto > $500 USD y urgencia este mes), proporciona el enlace de agendamiento.
  4. Devuelve la salida en JSON: { "respuesta_whatsapp": "...", "score_bant": 1-10 }
  ```

### [00:55 - 00:75] Integración de Google Calendar y Envío de Respuesta (20 min)
* **Paso 3:** Nodo condicional `IF`: Si `score_bant >= 7`, generar evento en Google Calendar o enviar enlace personalizado.
* **Paso 4:** Nodo `HTTP Request` hacia la API de WhatsApp para responderle al usuario en < 3 segundos.
* **Paso 5:** Guardar el registro del lead en Airtable / Google Sheets.

### [00:75 - 00:90] Live Debugging & Micro-Victoria del Alumno (15 min)
* **Ejercicio guiado:** Cada alumno importa la plantilla `.json` en su propio n8n y pone sus API keys.
* **Prueba de fuego (Micro-Victoria):** El alumno le envía un mensaje desde otro celular a su bot y ve cómo le responde y le crea la cita en su calendario.

---

## 🏆 ENTREGABLE Y MICRO-VICTORIA DEL ALUMNO
* **Entregable:** Archivo `.json` del flujo activo en su servidor.
* **Micro-Victoria:** *"Tengo mi propio asistente de ventas 24/7 funcionando en WhatsApp antes de que termine la clase"*.

---

## 📊 RÚBRICA DE EVALUACIÓN (10 PUNTOS)
1. **Webhook y Conectividad (3 pts):** Recibe y procesa el mensaje de WhatsApp sin errores de formato.
2. **Calificación BANT (4 pts):** El agente responde coherentemente y clasifica el lead según el prompt.
3. **Agendamiento y Registro (3 pts):** Genera la cita o guarda los datos correctamente en la base de datos.
