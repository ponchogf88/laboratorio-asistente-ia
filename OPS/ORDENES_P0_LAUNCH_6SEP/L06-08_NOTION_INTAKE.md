# ORDEN-L06-08 · SOP Inbound → Notion (Salir de 0 Inscritos) & Segmentación Triple
**Orden:** ORDEN-L06-08  
**Prioridad:** P0 (Salud y viabilidad del lanzamiento)  
**Dueño:** WhatsApp Launch (+ Jesús)  
**Objetivo:** Procedimiento operativo estándar para capturar cada lead entrante (Telegram, WhatsApp inbound, IG, LinkedIn, Ads), clasificar su origen por público (`P1_DISCORD`, `P2_LIQUID`, `P3_XAI`) y vaciarlo de inmediato a Notion sin perder ningún contacto.  
**Estado Actual Real:** **0 INSCRITOS** (Tablero en cero. Prohibido inventar registros).  
**Metas de Conversión:**  
- **Viernes 4 sep 23:59:** ≥ 1 inscrito confirmado.  
- **Sábado 5 sep 12:00 (Checkpoint):** ≥ 10 inscritos confirmados.  
- **Domingo 6 sep 18:00:** Cupo lleno (50 inscritos + lista de espera).  
**DoD:** SOP documentado, regla de inferencia de público, script de 30 segundos pegable y plantilla de vaciado en Notion estandarizada.  

---

## 📥 1. SOP Operativo y Campos Obligatorios en Notion

Cada persona interesada que interactúe con el ecosistema debe quedar registrada en Notion en menos de 5 minutos.

### Campos Oficiales de la Base de Datos:
1. **Nombre:** Nombre y apellido o cómo se identificó.
2. **WhatsApp:** Número con lada a 10 dígitos (ej. `81XXXXXXXX`).
3. **Público (Segmento Triple):** Campo Select obligatorio:
   - `P1_DISCORD` (Joven, Gen Z, perfil técnico junior, comunidad).
   - `P2_LIQUID` (Profesional 15–30, perfil tech/startup general, interés en n8n/Gemini).
   - `P3_XAI` (Profesional 30+, director, consultor, abogado, dueño de negocio).
4. **Fuente:** Origen del lead: `Telegram Bot` | `WhatsApp Directo` | `LinkedIn` | `Instagram Story/Feed` | `Meta Ads`.
5. **Estado:** `Nuevo` (pidió info o en proceso) | `Confirmado` (dio WA y reservó cupo) | `Lista de Espera` (si rebasa 50).
6. **Timestamp MTY:** Fecha y hora exacta de registro en Monterrey (ej. `04/09/2026 19:30`).
7. **Notas / Interés:** Perfil rápido (Giro del negocio, proceso a automatizar, dudas de acceso).

---

## 🔍 2. Protocolo de Inferencia del Campo "Público" (Cómo deducir P1 / P2 / P3)

Para clasificar al lead sin tener que hacerle un cuestionario engorroso, aplica estas 3 reglas de inferencia deterministas:

### Regla A: Por el Parámetro UTM de Entrada (100% Determinista)
Cuando el bot de Telegram o el webhook recibe el contacto, verifica el parámetro `utm_content`:
- Si contiene `p1_discord` → Asignar **`P1_DISCORD`**.
- Si contiene `p2_liquid` → Asignar **`P2_LIQUID`**.
- Si contiene `p3_xai` → Asignar **`P3_XAI`**.

### Regla B: Por el Canal de Entrada y el Creativo
Si el lead entra directamente por mensaje privado o WhatsApp sin UTM legible:
- **Llegó por LinkedIn:** Asignar automáticamente **`P3_XAI`**.
- **Llegó por Discord o TikTok:** Asignar automáticamente **`P1_DISCORD`**.
- **Llegó por Instagram Story Countdown / Feed Meta general:** Asignar **`P2_LIQUID`**.
- **Llegó por respuesta a Story con arte xAI (`STORY_V_XAI_preview.png`):** Asignar **`P3_XAI`**.
- **Llegó por respuesta a Story con arte Discord (`STORY_V_DISCORD_preview.png`):** Asignar **`P1_DISCORD`**.

### Regla C: Por el Tono y Perfil Expresado (Inbound WhatsApp al 81 4005 0088)
- Si se presenta como "Licenciado", "Director", "Tengo un despacho/empresa de consultoría" o lenguaje corporativo formal → **`P3_XAI`**.
- Si pregunta en tono casual ("Oye bro, ¿cómo entro?", "¿Qué necesito para correr n8n?", slang joven) → **`P1_DISCORD`**.
- Si busca eficiencia general para su trabajo o startup ("Quiero automatizar mis cotizaciones y tareas con IA") → **`P2_LIQUID`**.

---

## ⚡ 3. Script de 30 Segundos para Jesús (Inbound al 81 4005 0088)

Cuando un lead escriba al WhatsApp de soporte (`81 4005 0088`), responder con este texto exacto:

```text
¡Hola! Qué gusto saludarte. Soy Jesús Gutiérrez.

La Masterclass del Laboratorio Asistente IA es este domingo 6 de septiembre a las 7:00 pm (hora Monterrey). Es totalmente en vivo y sin costo.

Vamos a armar un asistente real con n8n + Gemini paso a paso. El cupo está topado a 50 lugares para poder contestar preguntas.

Para apartar tu lugar formalmente, dime por favor:
1. ¿Cuál es tu nombre completo?
2. ¿A qué te dedicas o qué proceso te gustaría automatizar con IA?

Te anoto de inmediato y te aseguro tu acceso.
```

### Respuesta de Cierre de Confirmación:
```text
¡Listo, {Nombre}! Quedas registrado/a con tu número {WhatsApp}. 
Tu lugar es el #{Número} de los 50 disponibles.

El domingo a las 6:00 pm (1 hora antes) te enviaré por aquí tu enlace personal de acceso a la sala de Teams.

Por favor guarda este contacto como "Jesús - AI Academy" para asegurar que te llegue el mensaje sin problemas. ¡Nos vemos el domingo!
```

---

## 📊 4. Plantilla de Registro para Notion (Markdown Mirror)

| # Cupo | Nombre del Lead | WhatsApp (Lada) | Público | Fuente | Estado | Timestamp (MTY) | Notas / Enfoque |
|:---:|---|---|:---:|---|---|---|---|
| 01 | *Pendiente lead 1* | *81XXXXXXXX* | P3_XAI | LinkedIn | Confirmado | 04/09/2026 19:45 | Director despacho legal |
| 02 | | | P2_LIQUID | Telegram Bot | Confirmado | | Consultor pyme cotizaciones |
| 03 | | | P1_DISCORD | Instagram DM | Confirmado | | Estudiante ingeniería / n8n |
| ... | | | | | | | |
| 50 | | | | Telegram Bot | Confirmado | | Cupo límite |
| 51 | | | | Telegram Bot | Lista de Espera | | En espera de vacante |

---

## 🎯 5. Reglas de Salida de Cero Inscritos (Sprint de 24 Horas)
1. **Monitoreo Permanente:** Revisión de Telegram y WhatsApp `81 4005 0088` cada 30 minutos hasta las 23:59.
2. **Cero Fricción:** Solo Nombre, WhatsApp y clasificación de Público.
3. **Cero Inventos:** Si hay 2 inscritos, se reportan 2 inscritos. Prohibido alterar datos.
4. **Checkpoint Sábado 12:00:** Si hay menos de 10 confirmados, disparar de inmediato la segunda ola de historias tri-estilo y mensajes 1:1 a red caliente.

---

ESTADO: LISTO_PARA_OK · AGY · 4 sep 2026
