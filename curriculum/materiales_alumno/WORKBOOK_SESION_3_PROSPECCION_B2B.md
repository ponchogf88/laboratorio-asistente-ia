# CUADERNO DE TRABAJO DEL ALUMNO · SESIÓN 3
## "Agente de Prospección B2B, Scraper Web y Cold Emails Personalizados"
### Laboratorio: Crea tu Asistente Personal IA · GC2 Legal Solutions

---

## 🎯 OBJETIVO DE LA SESIÓN:
Automatizar la prospección comercial saliente (Outbound B2B): crear un flujo que lea una lista de sitios web de clientes potenciales, extraiga su contenido mediante scraping, identifique dolores de negocio con **Claude 3.5 Sonnet** y genere correos electrónicos de prospección hiper-personalizados en tu bandeja de salida.

---

## 🛠️ PASO 1: IMPORTAR EL WORKFLOW EN TU N8N
1. Abre tu panel de n8n.
2. Ve a **`Workflows` ➔ `Import from File`**.
3. Selecciona el archivo: [`02_agente_prospeccion_b2b_email.json`](file:///C:/Users/USUARIO/ai-academy-enterprise/curriculum/workflows_json/02_agente_prospeccion_b2b_email.json).

---

## 📊 PASO 2: CONFIGURAR TU TABLA DE PROSPECCIÓN (GOOGLE SHEETS)
Crea una hoja de cálculo en Google Sheets con las siguientes columnas:
1. `Empresa`
2. `Sitio_Web`
3. `Correo_Contacto`
4. `Estado_Envio` (Pendiente / Generado / Enviado)
5. `Borrador_IA_Generado`

---

## 📝 EJERCICIO PRÁCTICO: AJUSTAR EL PROMPT DE AUDITORÍA
En el nodo de Claude 3.5, define tu ángulo de ataque comercial:
```markdown
Analiza el siguiente texto extraído del sitio web de la empresa: {{ $json.html_content }}
Identifica:
1. Qué vende exactamente la empresa.
2. Qué problema evidente tienen en su proceso de ventas o atención.
3. Redacta un Cold Email de 3 párrafos cortos ofreciendo [TU_SOLUCION_O_SERVICIO] demostrando que leíste su sitio web.
```

---

## 🧪 PRUEBA DE FUEGO (MICRO-VICTORIA):
1. Coloca la URL de 1 empresa real en tu Google Sheets.
2. Ejecuta el flujo en n8n.
3. Abre tu Gmail o Google Sheets y comprueba que el correo generado cite textualmente aspectos reales de la empresa analizada, evitando sonar como spam genérico.

---

## 📊 RÚBRICA DE EVALUACIÓN (10 PUNTOS):
* [ ] **Conexión exitosa con Google Sheets (Lectura y Escritura):** (3 Puntos)
* [ ] **Extracción y limpieza de contenido HTML (Scraping):** (2 Puntos)
* [ ] **Calidad y personalización del Cold Email generado por Claude 3.5:** (3 Puntos)
* [ ] **Envío automático o creación de borrador en Gmail:** (2 Puntos)
