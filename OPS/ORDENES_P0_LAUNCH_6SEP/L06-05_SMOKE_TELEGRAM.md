# ORDEN-L06-05 · Runbook Smoke-Test Bot Telegram
**Orden:** ORDEN-L06-05  
**Prioridad:** P0 (Bloqueante para encender pauta Meta)  
**Dueño:** Jesús (+ Community Manager)  
**Objetivo:** Validar en celular en 8 minutos que `https://t.me/AcademiaIA_Bot` responde, captura nombre, WhatsApp y confirma cupo correctamente antes de gastar pauta.  
**DoD:** Flujo nombre → WhatsApp → confirmación OK o bug documentado con screenshot y texto exacto.  
**Deadline:** Viernes 4 sep 2026 · 20:00 MTY  

---

## ⏱️ Instrucciones Rápidas para Jesús (Ejecución en Celular en 8 Minutos)

No necesitas computadora para este test. Abre Telegram en tu iPhone y sigue estos 4 pasos:

### Paso 1: Abrir el Bot
1. Toca este enlace directo desde tu celular: **[https://t.me/AcademiaIA_Bot](https://t.me/AcademiaIA_Bot)**
2. Presiona el botón inferior **Iniciar** (o escribe `/start`).

### Paso 2: Verificar Mensaje 1 (Bienvenida)
El bot debe responderte de inmediato con el siguiente texto exacto:

```text
¡Hola! Bienvenido/a al Laboratorio Asistente IA 👋

Masterclass gratis
📅 Domingo 6 de septiembre
🕖 7:00 pm (hora Monterrey)
👥 Cupo: 50 lugares

Vas a ver en vivo un asistente con n8n + Gemini (mensaje → decisión → acción) y el mapa del Laboratorio de 30 días.

Para reservar tu lugar, necesito 2 datos. Empezamos:

👉 ¿Cómo te llamas? (nombre completo o como quieres que te anotemos)
```

### Paso 3: Enviar Nombre y Verificar Mensaje 2
1. Responde con tu nombre de prueba (ejemplo: `Jesús Prueba`).
2. El bot debe responderte:

```text
Gracias, Jesús Prueba.

Ahora tu WhatsApp (con lada, ej. 81XXXXXXXX).
Por ahí te confirmamos el cupo y te mandamos el acceso a la sala el día del evento.

👉 Escribe tu número de WhatsApp:
```

### Paso 4: Enviar WhatsApp y Verificar Confirmación (Mensaje 3)
1. Escribe tu número con lada (ejemplo: `8140050088` o `8112345678`).
2. El bot debe devolverte la confirmación con tus datos inyectados:

```text
Listo, Jesús Prueba ✅

Tu lugar queda reservado para la Masterclass:
• Dom 6 sep · 7:00 pm MTY
• Cupo 50 (registro confirmado)
• WhatsApp: 8140050088

Te escribimos por WhatsApp con el acceso a la sala (solo a inscritos).

Si el cupo se llena, te avisamos y te pasamos a lista de espera.

¿Quieres el recordatorio un día antes? Responde SÍ.
```

3. Responde `SÍ` para validar que acepte el opt-in del recordatorio.

---

## 🧪 Matriz de Casos de Prueba (Edge Cases)

| Caso | Acción a probar | Respuesta esperada del Bot |
|---|---|---|
| **1. Cupo Disponible (Happy Path)** | Enviar nombre y WA válido con cupo < 50 | Mensaje 3: "Listo, {nombre} ✅ Tu lugar queda reservado... Cupo 50 (registro confirmado)". |
| **2. Cupo Lleno (Capacidad ≥ 50)** | Registrarse cuando el contador llegue a 50 | Mensaje 4: "El cupo de 50 ya se llenó. Te anoto en lista de espera con: Nombre: {nombre} • WhatsApp: {whatsapp}...". |
| **3. Número Mal Escrito** | Enviar texto ("no tengo", "hola") o menos de 10 dígitos | Mensaje de reintento pidiendo número a 10 dígitos o aceptando la entrada sin tronar el flujo. |
| **4. Bot Mudo / No responde** | Tocar `/start` y no recibir respuesta en > 15s | Falla de conexión webhook/n8n o bot despublicado (ver sección Fixes). |

---

## 📋 Tabla de Resultados (PASS / FAIL)

| Criterio de Aceptación | Estado (PASS / FAIL) | Notas / Comportamiento observado |
|---|:---:|---|
| Comando `/start` responde en < 3 segundos | [ ] | |
| Mensaje 1 tiene fecha (Dom 6 sep), hora (7:00 pm MTY) y cupo (50) | [ ] | |
| Captura de nombre exitosa y personalizada en Mensaje 2 | [ ] | |
| Captura de WhatsApp de 10 dígitos funcional | [ ] | |
| Mensaje 3 confirma cupo y menciona que el acceso a sala va por WhatsApp | [ ] | |
| Registro impactado en base de datos / webhook de salida | [ ] | |

---

## 🚨 Protocolo si Falla (FAIL)

Si el bot no responde, se traba o manda error:

1. **Captura inmediata:**
   - Toma **Screenshot** de la pantalla en Telegram donde se trabó.
   - Copia el **último texto enviado y recibido**.
2. **3 Fixes Rápidos Posibles (Sin tocar credenciales):**
   - **Fix 1 (ManyChat / BotFather Token):** En ManyChat > Settings > Channels > Telegram, verificar que el canal esté en estado `Connected` y presionar `Refresh Connection`.
   - **Fix 2 (Workflow n8n webhook):** Si el bot corre en n8n, verificar que el nodo `Telegram Trigger` esté en modo **Active (Production)** y no solo esperando ejecuciones de prueba manuales.
   - **Fix 3 (Validación de JSON / Payload):** Si el bot pide WhatsApp y falla, verificar en el nodo de formateo que la variable `{{whatsapp}}` acepte formato texto/cadena y no esté forzando entero estricto que rechace ladas con signo `+` o espacios.

---

## 📱 Mensaje de Prueba para WhatsApp (Copia y pégatelo a ti mismo)

Copia este bloque de 5 líneas y mándatelo a tu propio WhatsApp para tener a la mano el texto exacto de confirmación 1:1:

```text
¡Hola Jesús! Confirmado tu lugar para la Masterclass del Laboratorio Asistente IA este domingo 6 a las 7:00 pm MTY.
Tienes 1 de los 50 lugares reservados.
Por aquí te enviaré tu enlace privado de acceso a la sala 1 hora antes de iniciar.
Guarda este número para que te llegue el link sin que WhatsApp lo mande a spam.
¿Alguna duda previa sobre n8n o Gemini que quieras que toquemos en vivo?
```

---

ESTADO: LISTO_PARA_OK · AGY · 4 sep 2026
