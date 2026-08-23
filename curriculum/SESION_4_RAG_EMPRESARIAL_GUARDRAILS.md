# GUÍA DEL INSTRUCTOR · SESIÓN 4 (90 MINUTOS)
## "Agente RAG con Base de Conocimiento y Guardrails Anti-Alucinaciones"
### Laboratorio: Crea tu Asistente Personal IA · GC2 Legal Solutions

---

## ⏱️ CRONOGRAMA MINUTO A MINUTO (90 MIN)

```text
[00:00 - 00:10] Revisión de Resultados de Prospección B2B (10 min)
[00:10 - 00:30] Qué es RAG (Retrieval-Augmented Generation) y Bases Vectoriales (20 min)
[00:30 - 00:55] Importación del Workflow `03_agente_soporte_rag_pgvector.json` (25 min)
[00:55 - 00:75] Ingesta de Documentos (PDFs/Manuales) y Configuración de Guardrails (20 min)
[00:75 - 00:85] Prueba de Estrés: Ataque de Preguntas Trampa y Alucinaciones (10 min)
[00:85 - 00:90] Asignación de Tarea y Preparación para el Demo Day (5 min)
```

---

## 🛠️ DESARROLLO PASO A PASO PARA EL INSTRUCTOR

### 1. [00:00 - 00:10] Apertura
* Por qué RAG: *"Un LLM estándar inventa cosas cuando no sabe. RAG le da una biblioteca privada (tus manuales, catálogos o políticas) y lo obliga a responder únicamente con base en tus documentos oficiales"*.

### 2. [00:10 - 00:30] Conceptos Clave de RAG
* **Embeddings:** Cómo convertir texto en vectores numéricos (OpenAI `text-embedding-3-small`).
* **Vector Store:** Base de datos en Supabase / Qdrant para almacenar y buscar por similitud semántica.
* **Vector Store Retriever:** El nodo de n8n que extrae los 3 fragmentos más relevantes del documento.

### 3. [00:30 - 00:55] Configuración en n8n
* Importar `03_agente_soporte_rag_pgvector.json`.
* Conectar el agente conversacional de LangChain con la herramienta de memoria vectorial.

### 4. [00:55 - 00:75] Implementación de Guardrails Estrictos
* Configurar las reglas de oro en el *System Prompt*:
  * *"Si la respuesta no está explícitamente contenida en los fragmentos recuperados, responde: 'No dispongo de esa información en mis políticas oficiales'."*
  * Ajuste de temperatura a `0.2`.

### 5. [00:75 - 00:85] Micro-Victoria de la Sesión
* Subir un PDF de catálogo o política de prueba.
* Hacerle 2 preguntas difíciles y 1 pregunta trampa sobre un tema no existente.
* Comprobar que el agente responde con precisión exacta y rechaza inventar datos en la pregunta trampa.

---

## 🏆 ENTREGABLE DE LA SESIÓN 4:
* Captura de pantalla del chat del agente respondiendo con citas exactas del PDF subido.
