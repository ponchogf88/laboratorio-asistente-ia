# GUÍA DEL INSTRUCTOR · SESIÓN 3 (90 MINUTOS)
## "Agente de Prospección B2B, Scraper Web y Cold Emails con IA"
### Laboratorio: Crea tu Asistente Personal IA · GC2 Legal Solutions

---

## ⏱️ CRONOGRAMA MINUTO A MINUTO (90 MIN)

```text
[00:00 - 00:10] Revisión de Tareas y Micro-victorias de WhatsApp (10 min)
[00:10 - 00:30] Arquitectura del Flujo de Prospección B2B y Scraper Web (20 min)
[00:30 - 00:55] Importación del Workflow `02_agente_prospeccion_b2b_email.json` (25 min)
[00:55 - 00:75] Configuración de Claude 3.5 para Análisis de Dolores y Cold Emailing (20 min)
[00:75 - 00:85] Prueba en Vivo: Auditoría de 1 Sitio Web Real y Envío de Correo (10 min)
[00:85 - 00:90] Asignación de Tarea y Entrega de Plantilla (5 min)
```

---

## 🛠️ DESARROLLO PASO A PASO PARA EL INSTRUCTOR

### 1. [00:00 - 00:10] Apertura
* El valor de la prospección: *"Un negocio sin prospección muere. Hoy aprenderán a crear un agente que lee el sitio web de cualquier empresa, encuentra sus errores y le manda un correo ofreciendo soluciones personalizadas"*.

### 2. [00:10 - 00:30] La Arquitectura del Agente B2B
* **Nodo 1 (Google Sheets Trigger):** Lee la lista de URLs de empresas objetivo.
* **Nodo 2 (HTTP Request / Scraper):** Extrae el texto HTML del sitio web de la empresa.
* **Nodo 3 (Claude 3.5 Sonnet):** Analiza la propuesta de valor de la empresa, detecta qué servicios le faltan y redacta un correo en 3 párrafos hiper-personalizado.
* **Nodo 4 (Gmail / SMTP):** Envía el borrador o correo directo.

### 3. [00:30 - 00:55] Importación en n8n
* Guiar a los alumnos para importar `02_agente_prospeccion_b2b_email.json`.
* Conectar credenciales de Google Sheets y Gmail.

### 4. [00:55 - 00:75] El Prompt de Hiper-Personalización
* Mostrar cómo evitar el spam: no enviar mensajes genéricos, sino citar textualmente lo que la empresa vende en su página web.

### 5. [00:75 - 00:85] Micro-Victoria de la Sesión
* Cada alumno ingresa la URL de un cliente real o prospecto en su tabla.
* Ejecutan el flujo y ven en su bandeja de Gmail el correo redactado automáticamente con un análisis perfecto de la empresa.

---

## 🏆 ENTREGABLE DE LA SESIÓN 3:
* Captura de pantalla de la tabla de prospectos con 3 correos generados automáticamente por el agente.
