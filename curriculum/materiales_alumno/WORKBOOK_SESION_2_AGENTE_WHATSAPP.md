# CUADERNO DE TRABAJO DEL ALUMNO · SESIÓN 2
## "Agente SDR de WhatsApp + Calificación BANT + Google Calendar"
### Laboratorio: Crea tu Asistente Personal IA · GC2 Legal Solutions

---

## 🎯 OBJETIVO DE LA SESIÓN:
Construir y activar tu propio **Agente SDR en WhatsApp** que responda mensajes en tiempo real, califique el interés de los prospectos mediante el protocolo BANT (Presupuesto, Autoridad, Necesidad y Tiempo) y agende llamadas en Google Calendar de forma autónoma.

---

## 🛠️ PASO 1: IMPORTAR EL WORKFLOW EN TU N8N
1. Abre tu panel de n8n (`http://TU_IP:5678`).
2. Haz clic en **`Workflows` ➔ `Import from File`**.
3. Selecciona el archivo: [`01_agente_sdr_whatsapp_calendly.json`](file:///C:/Users/USUARIO/ai-academy-enterprise/curriculum/workflows_json/01_agente_sdr_whatsapp_calendly.json).

---

## 🔑 PASO 2: VINCULAR CREDENCIALES
* **Meta WhatsApp Cloud API:**
  * Ingresa a *developers.facebook.com* y copia tu `Phone Number ID` y `Access Token`.
  * Configura la URL del Webhook en Meta con la URL que te genera el nodo inicial de n8n.
* **Google Calendar:**
  * Conecta tu cuenta de Google en el nodo de Calendar para permitir agendamiento.
* **Anthropic / Claude 3.5 Sonnet:**
  * Vincula tu API key en el nodo del modelo de lenguaje.

---

## 📝 EJERCICIO PRÁCTICO: PERSONALIZAR EL SYSTEM PROMPT
Abre el nodo de LangChain Agent y personaliza las siguientes variables:
```markdown
Eres el Asistente SDR de [NOMBRE_DE_TU_NEGOCIO].
Tus servicios principales son: [DETALLA TUS SERVICIOS].
Tu objetivo es calificar al usuario con 3 preguntas clave y agendar la cita.
Si el lead califica, envía tu enlace de agendamiento: [TU_LINK_CALENDAR].
```

---

## 🧪 PRUEBA DE FUEGO (MICRO-VICTORIA):
1. Envía un mensaje desde otro celular a tu número de WhatsApp: *"Hola, me interesa información de sus servicios"*.
2. Verifica que el asistente responda en menos de 3 segundos con el saludo personalizado.
3. Sigue la conversación simulando ser un cliente con presupuesto y confirma que te envíe el enlace de agenda.

---

## 📊 RÚBRICA DE EVALUACIÓN (10 PUNTOS):
* [ ] **Flujo importado y sin errores en n8n:** (3 Puntos)
* [ ] **Conexión de WhatsApp Cloud API activa y recibiendo mensajes:** (3 Puntos)
* [ ] **Calificación BANT y enlace de calendario funcionando:** (3 Puntos)
* [ ] **Respeto a los guardrails (cero inventar datos):** (1 Punto)
