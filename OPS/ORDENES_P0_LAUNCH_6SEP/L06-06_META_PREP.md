# ORDEN-L06-06 · Preparación de Pauta Meta Ads (Modo Standby — SIN ENCENDER)
**Orden:** ORDEN-L06-06  
**Prioridad:** P0 (Preparación Crítica de Tráfico Pagado)  
**Dueño:** Media Buyer  
**Colaboran:** Jesús (Aprobación de Presupuesto), Copy Ads, Visual Production  
**Estado Actual:** **STANDBY / CAMPAÑAS EN BORRADOR (OFF)**  
**Regla Absoluta:** NO encender campañas ni presionar "Publicar" hasta que Jesús ingrese el monto en `TOPE_APROBADO_MXN` y dé la orden expresa de "ON".  

---

## 🔒 Control Presupuestal y Candado de Seguridad

```text
====================================================================
CAMPO OBLIGATORIO DE AUTORIZACIÓN (SOLO JESÚS LO LLENA):

TOPE_APROBADO_MXN = ____________________ (Firma/OK Jesús)

FECHA DE AUTORIZACIÓN: _____ / _____ / 2026
====================================================================
```

- **Rango sugerido por Media Buyer:** `$800.00 – $1,500.00 MXN` en total para la ventana Viernes 4 sep noche → Sábado 5 sep medianoche.
- **Distribución sugerida:**
  - Anuncio A (Productividad): 40% del presupuesto.
  - Anuncio B (Construcción): 35% del presupuesto.
  - Anuncio C (Servicio/Agencia): 25% del presupuesto.

---

## 🎯 Configuración de Audiencia en Meta Ads Manager
*(Etiqueta: Hipótesis de Segmentación - Media Buyer · Validar en primeras 12h de pauta)*

- **Ubicación Geográfica:** Monterrey, Nuevo León, México + Área Metropolitana (San Pedro Garza García, San Nicolás, Guadalupe, Apodaca, Santa Catarina) + radio de 25 km a la redonda.
- **Edad:** 25 a 45 años.
- **Género:** Todos.
- **Idiomas:** Español (todos).
- **Segmentación Detallada (Intereses sugeridos combinados con lógica O):**
  - `Automatización de procesos` OR `n8n` OR `Make.com`
  - `Inteligencia artificial` OR `ChatGPT` OR `Google Gemini`
  - `Agencias de marketing digital` OR `Consultoría de empresas`
  - `Software as a service (SaaS)` OR `Desarrollo de software`
- **Ubicaciones (Placements):** Feeds de Instagram y Facebook, Instagram Stories, Facebook Stories, Instagram Reels.

---

## 📢 Creativos y Textos Listos para Pegar (A/B/C)
*(Textos exactos extraídos de COPY_FINAL_HOY.md · Sin invenciones)*

### Anuncio A — Enfoque Productividad / Automatización
- **Asset Visual:** `LANZAMIENTO_6_SEP/FINAL_03_FEED_META_1080x1080.png`
- **Texto Primario:**
```text
¿Sigues perdiendo horas respondiendo lo mismo y cotizando a mano?

Este domingo 6 de septiembre a las 7:00 pm (hora Monterrey) te muestro en vivo cómo armar un asistente con n8n + Gemini: mensaje → decisión → acción.

Masterclass gratis · Cupo 50
Después: Laboratorio 30 días (early bird $1,000 MXN)
No es un curso de prompts: sales con un asistente que ejecuta. Garantía 7 días o hasta Clase 1.

Toca y reserva tu lugar en Telegram.

https://t.me/AcademiaIA_Bot

Dudas: WhatsApp 81 4005 0088
```
- **Headline (Título corto):** Dom 6 · 7pm MTY · Cupo 50
- **Descripción:** Masterclass gratis. Reserva en Telegram.
- **Botón CTA:** Registrarse / Más información
- **URL de Destino con UTM:**
  `https://t.me/AcademiaIA_Bot?utm_source=meta&utm_medium=paid&utm_campaign=masterclass_6sep&utm_content=ad_a_productividad`

---

### Anuncio B — Enfoque Construcción Técnica / Flujos
- **Asset Visual:** `LANZAMIENTO_6_SEP/FINAL_02_IG_STORY_COUNTDOWN_1080x1920.png` (o `FINAL_04_REEL_COVER_1080x1920.png`)
- **Texto Primario:**
```text
La IA no es solo chat. Es contexto + decisión + acción en un flujo que sí puedes construir.

Domingo 6 · 7:00 pm MTY · Masterclass gratis (50 lugares)
Vas a ver un flujo completo de punta a punta y el mapa del Laboratorio de 30 días.

Sin humo. Solo el sistema y el siguiente paso claro.
Laboratorio 30 días = asistente que ejecuta, no otro curso de prompts. Garantía 7 días o hasta Clase 1.

Reserva en Telegram:

https://t.me/AcademiaIA_Bot

Dudas: WhatsApp 81 4005 0088
```
- **Headline (Título corto):** De chat a sistema real
- **Descripción:** Gratis · Dom 6 · 7:00 pm MTY
- **Botón CTA:** Registrarse / Más información
- **URL de Destino con UTM:**
  `https://t.me/AcademiaIA_Bot?utm_source=meta&utm_medium=paid&utm_campaign=masterclass_6sep&utm_content=ad_b_construccion`

---

### Anuncio C — Enfoque Consultores / Agencias
- **Asset Visual:** `LANZAMIENTO_6_SEP/FINAL_03_FEED_META_1080x1080.png`
- **Texto Primario:**
```text
Si eres consultor o agencia: el valor no está en “saber de IA”. Está en entregar un sistema que atiende, califica y agenda.

Masterclass gratis este domingo 6 a las 7:00 pm (MTY).
Cupo 50. Early bird del programa: $1,000 MXN.
Empaqueta sistemas (no prompts sueltos). Garantía 7 días o hasta Clase 1.

Entra al bot de Telegram y asegura tu lugar. El acceso a la sala va solo a inscritos.

https://t.me/AcademiaIA_Bot

Dudas: WhatsApp 81 4005 0088
```
- **Headline (Título corto):** Empaqueta sistemas, no solo prompts
- **Descripción:** Cupo 50 · Dom 6 · 7pm MTY
- **Botón CTA:** Registrarse / Más información
- **URL de Destino con UTM:**
  `https://t.me/AcademiaIA_Bot?utm_source=meta&utm_medium=paid&utm_campaign=masterclass_6sep&utm_content=ad_c_agencias`

---

## 🛑 Reglas Automatizadas de Pausa (Stop-Loss)

1. **Regla de CPL Alto (Costo por Lead / Clic Calificado a Bot):**
   - *Hipótesis Etiquetada Media Buyer:* Si un anuncio individual supera un CPL de `$45.00 MXN` por registro en Telegram tras haber recibido al menos 20 clics al enlace sin generar conversiones confirmadas, **pausar ese anuncio específico** y reasignar el presupuesto al anuncio con menor costo.
2. **Regla de Cupo Lleno en Notion:**
   - En el momento exacto en que la base de datos de Notion registre **≥ 45 inscritos confirmados**, el Media Buyer o Launch Manager debe **pausar de inmediato todas las campañas activas** para evitar sobrecupo de la sala de 50.
3. **Regla de Límite de Gasto:**
   - La campaña en Meta debe crearse con **Límite de Gasto de Campaña (Campaign Spending Limit)** exactamente igual a `TOPE_APROBADO_MXN` para garantizar que no haya cobros excedentes bajo ninguna circunstancia.

---

## 🖱️ Checklist de 8 Clics en Meta Ads Manager (Para cuando Jesús diga "ON")

Cuando Jesús autorice el presupuesto, seguir estos 8 clics exactos:

1. **Clic 1:** Abrir [Meta Ads Manager](https://adsmanager.facebook.com/) en la cuenta publicitaria designada de AI Academy / Dynamic Punch.
2. **Clic 2:** Entrar en la campaña borrador: `2026-09-06_P0_Masterclass_LabIA`.
3. **Clic 3:** En el nivel Campaña, verificar que el **Límite de Gasto** esté configurado con el valor exacto de `TOPE_APROBADO_MXN`.
4. **Clic 4:** En el nivel Conjunto de Anuncios, confirmar la segmentación: Monterrey + AMMty, 25–45 años.
5. **Clic 5:** En el nivel Anuncios, verificar que los creativos correspondan a `FINAL_02` y `FINAL_03` y que los enlaces de destino lleven el parámetro UTM correspondiente a cada variante.
6. **Clic 6:** Confirmar que el número de WhatsApp `81 4005 0088` aparezca **solo como texto al pie** y nunca como botón de llamada a la acción.
7. **Clic 7:** Encender el switch principal de la campaña de **OFF** a **ON**.
8. **Clic 8:** Presionar el botón verde **Revisar y Publicar (Publish)** en la esquina superior derecha.

---

ESTADO: LISTO_PARA_OK · AGY · 4 sep 2026
