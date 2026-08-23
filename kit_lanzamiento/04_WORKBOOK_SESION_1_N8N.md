# CUADERNO DE TRABAJO DEL ALUMNO · SESIÓN 1
## "Tu Propio Servidor de Automatización n8n en VPS por $5/mes"
### Laboratorio: Crea tu Asistente Personal IA · GC2 Legal Solutions

---

## 🎯 OBJETIVO DE ESTA SESIÓN:
Montar tu propio entorno independiente de n8n en un servidor en la nube (Hetzner VPS), asegurando **flujos y ejecuciones ilimitadas** sin pagar las tarifas abusivas por operación de herramientas como Make o Zapier.

---

## 🛠️ PASO 1: CREACIÓN DE TU SERVIDOR EN LA NUBE
1. Crea tu cuenta en **Hetzner Cloud** (o DigitalOcean).
2. Haz clic en **`Add Server`**:
   * **Ubicación:** Ashburn (EE. UU.) o Falkenstein (Alemania).
   * **Sistema Operativo:** Ubuntu 22.04 LTS.
   * **Tipo:** Shared vCPU (Plan CX22 · ~€4.50 EUR/mes).
3. Guarda tu dirección IP pública asignada (ejemplo: `123.45.67.89`).

---

## 🚀 PASO 2: INSTALACIÓN DE DOCKER Y N8N EN 1 LÍNEA
Abre tu terminal (PowerShell o Terminal de Mac) y conéctate a tu servidor:
```bash
ssh root@TU_IP_PUBLICA
```

Ejecuta el script de despliegue automático de n8n:
```bash
docker run -d --name n8n -p 5678:5678 -v ~/.n8n:/home/node/.n8n --restart unless-stopped n8nio/n8n
```

Abre tu navegador e ingresa a: `http://TU_IP_PUBLICA:5678`. ¡Tu n8n ya está vivo!

---

## 🔑 PASO 3: CONFIGURACIÓN DE APIS DE IA
En tu panel de n8n:
1. Ve a **`Credentials`** ➔ **`Add Credential`**.
2. **Anthropic API:** Pega tu API Key de Claude (`sk-ant-...`).
3. **OpenAI API:** Pega tu API Key de OpenAI (`sk-proj-...`).

---

## 🏆 MICRO-VICTORIA DE LA SESIÓN 1:
* Ejecutar tu primer flujo de prueba: Crear un nodo de `Manual Trigger` conectado a un nodo de `Anthropic Chat Model`, enviar el mensaje *"Hola Claude, mi servidor n8n está listo"* y ver la respuesta generada en menos de 2 segundos.
