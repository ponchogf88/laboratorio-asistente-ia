# CUADERNO DE TRABAJO DEL ALUMNO · SESIÓN 4
## "Agente RAG con Base de Conocimiento Vectorial y Guardrails Anti-Alucinaciones"
### Laboratorio: Crea tu Asistente Personal IA · GC2 Legal Solutions

---

## 🎯 OBJETIVO DE LA SESIÓN:
Conectar a tu Asistente de IA con una base de conocimiento privada (manuales de procesos, catálogos de productos, contratos o políticas en PDF) utilizando una **base de datos vectorial (Supabase / pgvector)** y blindarlo con **guardrails estrictos** para que jamás invente respuestas ni alucine.

---

## 🛠️ PASO 1: IMPORTAR EL WORKFLOW EN TU N8N
1. Abre tu panel de n8n.
2. Ve a **`Workflows` ➔ `Import from File`**.
3. Selecciona el archivo: [`03_agente_soporte_rag_pgvector.json`](file:///C:/Users/USUARIO/ai-academy-enterprise/curriculum/workflows_json/03_agente_soporte_rag_pgvector.json).

---

## 📚 PASO 2: INGESTA Y VECTORIZACIÓN DE TU DOCUMENTO
1. Sube un documento en PDF (mínimo 3 páginas: catálogo, reglamento o lista de precios).
2. En n8n, ejecuta el sub-flujo de **Ingesta**:
   * **Text Splitter:** Divide el documento en fragmentos (*chunks*) de 500 caracteres con 50 de solapamiento.
   * **Embeddings:** Convierte los fragmentos en vectores con OpenAI `text-embedding-3-small`.
   * **Vector Store:** Guarda los vectores en tu tabla de Supabase / Qdrant.

---

## 🛡️ PASO 3: CONFIGURAR LOS GUARDRAILS DE BLINDAJE
En el System Prompt del agente de soporte, añade las siguientes reglas obligatorias:
```markdown
REGLAS DE ORO DE SEGURIDAD (GUARDRAILS):
1. Basa tus respuestas ÚNICAMENTE en la información recuperada del documento.
2. Si el usuario pregunta algo que no está en el texto recuperado, responde textualmente:
   "Esa información no se encuentra en nuestras políticas oficiales. ¿Deseas que transfiera tu consulta con un asesor humano?"
3. NUNCA hagas suposiciones, cálculos no descritos ni inventes garantías.
4. Mantén la temperatura del modelo en 0.2.
```

---

## 🧪 PRUEBA DE ESTRÉS (MICRO-VICTORIA):
1. Hazle una pregunta legítima que esté en el PDF (ej. *"¿Cuál es la política de garantía de 14 días?"*) ➔ Debe responder con precisión citando el documento.
2. Hazle una pregunta trampa (ej. *"¿Tienen servicio de entrega en helicóptero?"*) ➔ Debe rechazar la pregunta y declarar que no está en las políticas oficiales.

---

## 📊 RÚBRICA DE EVALUACIÓN (10 PUNTOS):
* [ ] **Base de datos vectorial conectada (Supabase / Qdrant):** (3 Puntos)
* [ ] **Ingesta y procesamiento de documento PDF exitoso:** (3 Puntos)
* [ ] **Recuperación semántica precisa de fragmentos de texto:** (2 Puntos)
* [ ] **Superación de la prueba de estrés anti-alucinaciones:** (2 Puntos)
