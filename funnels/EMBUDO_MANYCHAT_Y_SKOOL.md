# ARQUITECTURA DEL EMBUDO: MANYCHAT (COMMENT-TO-DM) + COMUNIDAD EN SKOOL

---

## 1. FLUJO MANYCHAT / INSTAGRAM DM ("COMMENT-TO-DM")

### Disparador:
* Usuario comenta la palabra clave **`AGENTE`** en cualquier Reel, Post o Anuncio de Instagram.

### Árbol de Respuestas Automatizadas:

```text
[COMENTARIO PÚBLICO EN EL POST]
Respuesta aleatoria (para evitar shadowban):
- "¡Te acabo de enviar la plantilla por mensaje directo! 🚀 Revisa tu buzón."
- "¡Listo! Checa tus DMs para descargarlo 📩"
- "Te mandé el acceso al privado 🔥"

[MENSAJE DIRECTO (DM) AUTOMÁTICO]
Mensaje 1 (Inmediato):
"¡Hola {first_name}! 👋 Aquí tienes el acceso directo para descargar la plantilla JSON del Agente Autónomo y el video tutorial paso a paso:

👉 [ENLACE_DE_DESCARGA_SKOOL]

PD: En la comunidad gratuita tienes más de 10 plantillas listas para importar. ¿Ya tienes instalado n8n o estás empezando desde cero?"

[BOTONES DE OPCIÓN RÁPIDA]
🔘 "Ya tengo n8n"
🔘 "Empiezo desde cero"

[RAMIFICACIÓN DE CONVERSACIÓN]
Si elige "Empiezo desde cero":
-> "¡Genial! Dentro de la comunidad dejé un tutorial de 10 minutos para montar tu servidor sin saber programar. ¿Tu objetivo es automatizar tu propio negocio o aprender para ofrecer servicios a clientes?"

Si responde "Ofrecer servicios a clientes":
-> Tag asignado: `lead_agencia_interesado`
-> "Tenemos una masterclass especial sobre cómo cobrar de $1,500 a $3,000 por estos sistemas. ¿Te gustaría que te comparta el enlace?"
```

---

## 2. ESTRUCTURA DE LA COMUNIDAD EN SKOOL

La comunidad se organiza en torno a 3 pilares para maximizar retención y monetización:

### 1. Pestaña "Classroom" (Contenido Formativo Gratuito & De Pago):
* **Nivel 0 (Público / Gratis):**
  * *Bienvenida & Setup de n8n en VPS en 10 min*.
  * *Bóveda de 5 Plantillas Gratuitas (JSONs descargables)*.
  * *Roadmap: Cómo conseguir tu primer cliente B2B*.
* **Nivel VIP (Membresía $49/mes o Alumnos del Bootcamp):**
  * *Acceso completo al Máster en Agentes Autónomos (40+ horas)*.
  * *Grabaciones de las sesiones semanales de Debugging en vivo*.
  * *Librería de Contratos, Propuestas y Scripts de Prospección*.

### 2. Pestaña "Community" (Gamificación y Engagement):
* **Canal #victorias:** Donde los alumnos publican sus primeros flujos funcionando y sus clientes cerrados.
* **Canal #dudas-tecnicas:** Soporte donde el Agente de Éxito o los mentores responden en < 2 horas.
* **Canal #networking:** Alianzas entre alumnos no técnicos y técnicos.

### 3. Pestaña "Calendar" (Eventos Semanales):
* **Martes:** *Live Build & Debug* (Resolviendo errores de flujos en vivo con pantalla compartida).
* **Jueves:** *Estrategia de Ventas & Prospección B2B*.
