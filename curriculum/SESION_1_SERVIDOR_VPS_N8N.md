# GUÍA DEL INSTRUCTOR · SESIÓN 1 (90 MINUTOS)
## "Tu Propio Servidor de Automatización n8n en VPS por $5/mes"
### Laboratorio: Crea tu Asistente Personal IA · GC2 Legal Solutions

---

## ⏱️ CRONOGRAMA MINUTO A MINUTO (90 MIN)

```text
[00:00 - 00:10] Bienvenida, Presentación del Laboratorio y Reglas de la Cohorte (10 min)
[00:10 - 00:30] Creación y Configuración del Servidor VPS en Hetzner / DigitalOcean (20 min)
[00:30 - 00:50] Despliegue de Docker y n8n con SSL/Dominio (20 min)
[00:50 - 00:70] Conexión de Credenciales de IA (Claude 3.5 Sonnet / OpenAI) (20 min)
[00:70 - 00:85] Micro-Victoria: Tu Primer Flujo de Razonamiento Ejecutado (15 min)
[00:85 - 00:90] Asignación de Tarea y Cierre (5 min)
```

---

## 🛠️ DESARROLLO PASO A PASO PARA EL INSTRUCTOR

### 1. [00:00 - 00:10] Apertura
* Explicar por qué self-hosting: *"En Make o Zapier pagarías $100-$300 USD al mes si tu bot atiende 5,000 mensajes. En tu propio servidor n8n pagas €4.50 EUR ($5 USD) fijos y tienes ejecuciones ilimitadas."*

### 2. [00:10 - 00:30] Setup del Servidor VPS
* Guiar la creación en **Hetzner Cloud** (Plan CX22 · Ubuntu 22.04 LTS).
* Mostrar cómo conectarse vía SSH:
  ```bash
  ssh root@TU_IP_PUBLICA
  ```

### 3. [00:30 - 00:50] Instalación de Docker y n8n
* Comando de ejecución para el alumno:
  ```bash
  docker run -d --name n8n -p 5678:5678 -v ~/.n8n:/home/node/.n8n --restart unless-stopped n8nio/n8n
  ```
* Acceso en navegador: `http://TU_IP:5678`.

### 4. [00:50 - 00:70] Vinculación de APIs de IA
* Obtener y pegar la API Key de **Anthropic (Claude 3.5 Sonnet)**.
* Obtener y pegar la API Key de **OpenAI (GPT-4o)**.

### 5. [00:70 - 00:85] Micro-Victoria de la Sesión
* Crear un nodo `Manual Trigger` conectado a un nodo `Anthropic Chat Model`.
* Ejecutar el prompt: *"Actúa como consultor de negocios y dame 3 ideas de automatización para un despacho contable"*.
* Ver la respuesta en pantalla en menos de 2 segundos.

---

## 🏆 ENTREGABLE DE LA SESIÓN 1:
* Captura de pantalla del n8n del alumno activo con su primera ejecución exitosa.
