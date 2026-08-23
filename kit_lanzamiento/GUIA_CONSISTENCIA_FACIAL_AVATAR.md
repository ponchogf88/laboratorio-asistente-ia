# 🎭 GUÍA TÉCNICA: CONSISTENCIA DE ROSTRO (FACE-LOCK) PARA LIKINYA & AVATARES DE IA
> **Herramientas de Referencia Facial:** Google AI Studio (Gemini Multimodal) + Grok 2 / Flux + LivePortrait & InstantID  
> **Objetivo:** Mantener el 100% de la identidad facial, rasgos biométricos y coherencia visual de **Likinya** en todas las imágenes y videos del curso.

---

## 🧭 1. GOOGLE AI STUDIO (MULTIMODAL IN-CONTEXT IMAGE PROMPTING)

En **Google AI Studio** ([aistudio.google.com](https://aistudio.google.com)), puedes usar el contexto multimodal para fijar el rostro de Likinya:

### 🛠️ Paso a Paso:
1. Abre un nuevo prompt en Google AI Studio (modelo *Gemini 2.0 Flash / Pro* o *Imagen 3*).
2. Sube la imagen con el **rostro congelado de Likinya** como archivo adjunto (`Input Image`).
3. Usa el siguiente prompt de fijación de identidad:

```text
[SYSTEM / INSTRUCTION]
You are an expert AI visual director. Maintain 100% facial consistency and character identity based on the reference photo provided in [Image 1].

[USER PROMPT]
Using the exact facial identity, bone structure, eye shape, smile, and skin tone of the woman in [Image 1] (Likinya):
Generate a photorealistic 8k candid photograph of her sitting at her cozy bedroom workstation. 
She is wearing a casual olive-green linen shirt with a compact white Eufy security camera clipped to her shoulder. On her desk next to her is the cute Loona robot pet dog with bright animated OLED eyes. In the background, her dual monitors display real n8n automation workflows with warm bedroom lighting and real home studio details. Shot on 35mm lens, natural depth of field, authentic raw photograph.
```

---

## ⚡ 2. GROK (X) & FLUX (PROMPT STRUCTURING & SEED LOCKING)

En **Grok** y motores basados en **Flux / Midjourney / Stable Diffusion**, la consistencia se logra mediante descripción de tokens de anclaje (Anchor Tokens) y contexto de hilo:

### 🛠️ Estructura de Prompt para Grok:
```text
Candid real-life photo of the same woman (Likinya), young Latina tech creator, exact same facial features, dark wavy hair tied casually, warm friendly smile. She is in her home bedroom holding the Loona robot pet, small white Eufy camera on her shoulder, computer screens with n8n nodes in the background, warm ambient room lighting, 8k photorealistic style.
```

---

## 🎬 3. PIPELINE PARA VIDEO Y AVATAR PARLANTE (ANIMACIÓN DEL ROSTRO CONGELADO)

Para que el rostro congelado de Likinya hable y dé las clases de la Masterclass:

```mermaid
flowchart LR
    A["🖼️ Foto Rostro Congelado Likinya"] + B["🎙️ Audio Clonado (ElevenLabs)"] --> C["🧠 LivePortrait / Hedra / HeyGen"]
    C --> D["🎥 Video Final de Likinya Hablando<br/>(Sincronización Labial Perfecta 100% Idéntica)"]
```

### Herramientas Recomendadas:
1. **LivePortrait (Open Source / Zero Cost):**
   * Toma la foto estática de Likinya y la anima en tiempo real calcando tus gestos o el audio sin alterar ni un solo píxel de su cara.
2. **Hedra.com (Character-to-Video):**
   * Subes la imagen fija de Likinya + el audio de la clase, y genera el video en minutos con movimientos de cabeza y expresiones hiperrealistas.
3. **InstantID / PulID (Face-Lock para Stable Diffusion / Flux):**
   * Extrae el vector de identidad (InsightFace) del rostro congelado y te permite generar a Likinya en cualquier posición, vestimenta o ángulo manteniendo exactamente su misma cara.
