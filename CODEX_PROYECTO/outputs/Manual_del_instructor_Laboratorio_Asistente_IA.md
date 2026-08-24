# Manual del instructor — Laboratorio: Crea tu Asistente Personal IA

**Uso:** guía de facilitación para cinco sesiones en vivo de 90 minutos. No sustituye las guías vigentes de los proveedores. Antes de cada cohorte, verificar enlaces, precios, límites y disponibilidad regional de cualquier herramienta que se vaya a mostrar.

## Preparación común

### Sesión cero asíncrona — 45 minutos antes del inicio

Enviar un kit breve que cubra: modelo, prompt, token, contexto, revisión humana, interfaz, agente, automatización, API, CLI y SDK. Incluir un microdiagnóstico no calificable y tres plantillas base. El instructor revisa el diagnóstico para agrupar apoyo, no para excluir alumnos.

Las tres plantillas base son:

1. **Investigación/Documentos:** para estudiante, abogado o consultor; entrada → preguntas → tabla/síntesis → fuentes → revisión humana.
2. **Clientes/Proyectos:** para emprendedor/freelancer; consulta → preguntas → brief → borrador → aprobación humana.
3. **Contenido/Presencia:** para creador/profesional; idea → investigación → guion → revisión → adaptación a formatos.

### El tablero de cada alumno

Cada alumno crea una carpeta o página llamada **Sistema Profesional IA Personal**, con estas secciones:

1. Meta profesional y problema a resolver.
2. Ruta de credenciales/progreso.
3. Inventario de herramientas y suscripciones.
4. Biblioteca de prompts.
5. Proyecto aplicado.
6. Evidencia y plan de 30 días.

### Regla de oro para todo ejercicio

No se usan datos de clientes, expedientes, contraseñas, información financiera sensible ni contenido protegido que el alumno no tenga derecho de compartir. Si se necesita un caso, se anonimiza o se crea uno ficticio.

### Rutina docente de cada sesión

- Abrir con una demostración o pregunta con tensión real, no con definiciones.
- Explicar en bloques de máximo 12–15 minutos.
- Hacer visible el trabajo del alumno antes de mostrar otra herramienta.
- Cerrar con un entregable verificable y una siguiente acción de menos de 30 minutos.

---

## Sesión 1 — Activa tu perfil profesional de IA

**Resultado observable:** cada alumno termina con una meta clara, una tarea prioritaria y una ruta inicial de evidencia/credenciales.

**Materiales:** presentación ligera, enlace/QR a tablero de alumno, lista de proveedores, matriz Impacto × Riesgo × Facilidad.

### 0–10 min — Apertura

**Guion sugerido**

> “Este laboratorio no existe para que uses más aplicaciones. Existe para que dejes de empezar de cero cada lunes. En cinco sesiones vas a construir un asistente personal para una parte concreta de tu trabajo, tu estudio o tu negocio; además vas a ordenar una ruta para poder demostrar lo que estás aprendiendo.”

Pregunta al grupo: “¿Qué tarea te roba tiempo cada semana y te hace pensar: esto no debería empezar desde cero?” Recoger de tres a cinco respuestas.

### 10–28 min — Mapa de credenciales sin confusión

Explicar con una tabla en vivo:

| Término | Qué significa | Quién lo emite |
| --- | --- | --- |
| Curso/módulo | Contenido de aprendizaje | Plataforma o institución. |
| Laboratorio | Práctica guiada con evidencia técnica o funcional | Plataforma. |
| Badge/insignia | Señal digital de logro | Proveedor. |
| Certificado | Comprobante de finalización | Proveedor/institución. |
| Certificación | Credencial con requisitos/examen definidos | Proveedor. |

**Frase clave:**

> “Yo no voy a fabricar credenciales ni a prepararte para un examen externo. Mi trabajo es mostrarte dónde están las rutas, qué te piden, cómo abrirlas y cómo ordenar tu avance. La tarea la haces tú desde tu cuenta; la credencial la emite quien corresponde.”

Presentar Google Skills/Developer Profile como puerta base y AWS, IBM SkillsBuild, Microsoft Learn, Cisco y Coursera como rutas de acuerdo con el objetivo. No asegurar que todos los alumnos obtendrán todas las credenciales en 7.5 horas ni vender el curso como preparación para sus exámenes.

### 28–43 min — Activación y selección

Pedir que cada persona registre:

- Profesión/negocio actual.
- Meta a 90 días.
- Credencial o módulo que le parece más útil.
- Tiempo semanal real disponible.
- Requisito visible del proveedor (si hay costo, examen o disponibilidad).

**Duda frecuente:** “¿Cuál saco primero?”  
Respuesta: “La que respalda la habilidad que vas a practicar en tu proyecto, no la que tenga el nombre más rimbombante.”

### 43–57 min — Auditoría de oportunidad

Introducir matriz:

- Impacto: ¿mejora dinero, tiempo, calidad o experiencia?
- Frecuencia: ¿ocurre cada semana?
- Riesgo: ¿qué debe seguir revisando un humano?
- Facilidad: ¿puedo probar un prototipo esta semana?

**Ejemplos:**

- Emprendedor: responder consultas iniciales y convertirlas en brief.
- Estudiante: transformar notas en plan de estudio y práctica oral.
- Abogado/consultor: organizar hechos y pendientes de un caso ficticio.

### 57–72 min — Demo comparativa

Mostrar una misma tarea de bajo riesgo en Gemini, ChatGPT y Claude. No hacer ranking universal. Comparar:

- calidad de pregunta inicial;
- estructura de la respuesta;
- fuentes/verificación;
- manejo de contexto;
- necesidad de revisión.

**Guion de transición:**

> “La herramienta no piensa por ti. Lo valioso es que tú sepas darle contexto, pedir evidencia y decidir qué sí usas.”

### 72–85 min — Taller

Alumno completa: meta, problema, usuario, resultado esperado, herramienta de prueba, riesgo y tipo de evidencia que guardará.

### 85–90 min — Cierre/tarea

Tarea: completar una primera lección/lab de la ruta elegida o registrar por qué no fue accesible; documentar el flujo actual de la tarea elegida con un ejemplo seguro.

---

## Sesión 2 — Configura tu Centro de Mando IA

**Resultado observable:** cada alumno sabe distinguir términos, selecciona herramientas intencionalmente y tiene un primer control de tokens, costos y prompts.

### 0–10 min — Revisión

Pedir que compartan una sola cosa: “¿Qué descubriste sobre la ruta o tarea que no sabías antes?” Mostrar dos avances y un bloqueo. Normalizar que la disponibilidad de herramientas puede variar.

### 10–25 min — Idioma de la IA

Usar analogía de taller:

- **Interfaz:** el tablero/pantalla desde donde usas algo.
- **Modelo:** el motor que genera o razona.
- **Agente:** un rol que recibe objetivo, contexto y tareas.
- **Skill/plugin/conector:** una capacidad o puente adicional.
- **@ y /**: maneras de invocar contexto, personas o funciones donde la plataforma las soporte.
- **API:** puerta para que sistemas se comuniquen.
- **CLI:** forma de operar desde terminal.
- **SDK:** kit para que alguien desarrolle integraciones.

> “Hoy no necesitas memorizar siglas. Necesitas saber cuándo una sigla te abre una puerta y cuándo no la necesitas.”

### 25–42 min — Herramientas y suscripciones

Entregar una matriz vacía: tarea / herramienta posible / plan actual / límite / alternativa gratuita / información que no subiré.

Demostrar cómo elegir por función, no por moda: chat y redacción; investigación; razonamiento; diseño; síntesis; archivos; programación/builder.

### 42–55 min — Tokens y control

Demostración: mismo objetivo mal pedido vs dividido en fases. Hablar de contexto, créditos/límites, archivos y presupuestos. No usar promesas de “ahorro 90%”.

**Regla de control:** cada solicitud importante lleva objetivo, insumo mínimo, formato y criterio de revisión. Los alumnos anotan fecha, herramienta, resultado, costo/consumo conocido y valor percibido.

### 55–68 min — Prompt que opera

Plantilla:

```text
Situación: [contexto verificable]
Objetivo: [resultado concreto]
Insumos: [texto/datos seguros]
Restricciones: [tono, extensión, prohibiciones]
Formato: [tabla, guion, checklist]
Verificación: [qué fuentes, incertidumbres o puntos debo revisar]
```

Crear tres versiones para la misma tarea: creador, crítico y verificador.

### 68–80 min — Fuentes, archivos y gobernanza de datos

Ejercicio: detectar tres banderas rojas en una respuesta con citas incompletas o datos sensibles. Dedicar este bloque a una rúbrica obligatoria: qué dato puedo usar, qué debo anonimizar, qué no debo subir, qué salida exige revisión y dónde se almacena la evidencia. Recordar: borrador no es dictamen, y una respuesta segura no reemplaza juicio profesional.

### 80–90 min — Laboratorio/tarea

Configurar Centro de Mando v1. Tarea: probar los tres prompts y registrar qué se corrigió manualmente.

---

## Sesión 3 — Convierte conocimiento en un activo y un flujo útil

**Resultado observable:** cada alumno crea una primera versión de su asistente/flujo y un activo de presencia o entrega profesional.

### 0–12 min — Gancho

> “El asistente no tiene que ser un robot con voz. Puede ser un sistema que te hace mejores preguntas, te ordena información y te deja un primer borrador para revisar.”

Mostrar un ejemplo de flujo: consulta → preguntas de aclaración → brief → borrador → checklist → entrega.

### 12–27 min — Medir valor sin humo

Medir punto de partida: minutos, errores, entregas, re-trabajo, mensajes no respondidos o piezas publicadas. La métrica se formula como hipótesis: “buscaré reducir de 60 a 35 minutos”, no “voy a ganar X”.

### 27–42 min — Diseñar el asistente personal con plantilla base

Partir de una de las tres plantillas base y adaptar: nombre de trabajo, usuario, tarea, entrada, pasos, salida, guardrails, cuándo escalar a humano y qué evidencia archiva. Esto estandariza la lógica del grupo sin quitar personalización.

**Ejemplos de asistentes:** Carrera, Estudio, Clientes, Contenido, Consultoría, Segundo Cerebro.

### 42–58 min — De experiencia a activo

Propuesta de valor: persona + dolor + proceso + prueba + siguiente paso. Convertir la demostración del proyecto en guion, carrusel o post.

### 58–70 min — Producción responsable

Usar guion, teleprompter, pantalla, Canva/archivo visual. Atribuir fuentes y no copiar creativos ni fingir resultados.

### 70–85 min — Taller

Crear el diagrama del asistente y una pieza de explicación: “Así resuelvo [tarea] con IA sin delegar [criterio humano].”

### 85–90 min — Tarea

Probar el flujo con un caso seguro, guardar antes/después y anotar una mejora.

---

## Sesión 4 — Entra al nivel builder

**Resultado observable:** el alumno prueba o diseña un proyecto builder, y elige con intención su camino de siguiente nivel.

### 0–12 min — La escalera

Explicar tres tracks: **técnico** (GitHub, APIs, código), **visual/creativo** (IA Studio, NotebookLM, contenido/prototipos) y **negocio/operaciones** (automatización, procesos, agentes). No todos necesitan seguir el técnico.

### 12–30 min — Google Developer / Google Skills

Mostrar el perfil, labs y progreso que estén vigentes para la cohorte. Si GEAR, créditos o una herramienta no están disponibles para alguien, dar alternativa y registrar la limitación; no convertirlo en fracaso personal.

### 30–47 min — Exploración guiada

Presentar Google AI Studio y NotebookLM. Mostrar Flow, Pomelli o Antigravity solo si están disponibles en ese momento/territorio y solo con casos apropiados. Explicar para qué sirve la herramienta antes de mostrar botones.

### 47–60 min — Mapa de frontera

Explicar, con un diagrama, cómo se conectan GitHub, API, automatización, Make/n8n, agentes y orquestación. Frase clave: “Conocer el mapa no significa que tengas que construir toda una fábrica hoy.”

### 60–85 min — Laboratorio builder

Cada alumno elige una ruta:

- Prototipo de chat/assistant en herramienta visual.
- Notebook/segundo cerebro con fuentes propias permitidas.
- Mapa de automatización para ejecutar después.
- Primer repositorio/README si ya está preparado para track técnico.

### 85–90 min — Tarea

Preparar demo de 3 minutos: problema, flujo, prueba, resultado, revisión y siguiente credencial.

---

## Sesión 5 — Demo Day: evidencia, proyecto y plan de 30 días

**Resultado observable:** cada alumno presenta una variante de plantilla base, evidencia, límites y siguiente fase; el instructor tiene insumos comparables para validar la constancia privada.

### Preparación previa

Enviar 48 h antes:

> “Trae tu tablero abierto y una demo de máximo tres minutos. No necesitas tener algo perfecto; sí necesitas mostrar qué problema escogiste, qué probaste, qué verificaste y cuál es tu siguiente paso.”

Preparar checklist de evidencia: asistencia, tablero, prompts, proyecto, bitácora y progreso/labs seleccionados.

### Guion completo de la última clase

#### 0–8 min — Bienvenida y regla del Demo Day

> “Hoy no vamos a competir por quién tiene la automatización más espectacular. Vamos a demostrar criterio: qué problema resolviste, qué parte conserva decisión humana y qué evidencia te llevas. Eso es más valioso que una captura bonita.”

Explicar agenda y recordar regla de datos seguros.

#### 8–18 min — Tablero de evidencia

Cada alumno marca estado: iniciado / en progreso / completado / bloqueado por requisito externo. Revisar que ninguna persona use credenciales ajenas ni comparta contraseñas.

> “Tu avance vale aunque una plataforma tenga un requisito extra. Lo que sí controlas es documentar qué hiciste, qué falta y cuándo lo vas a retomar.”

#### 18–30 min — Diagnóstico final de proyectos

El instructor muestra la rúbrica:

| Criterio | Pregunta |
| --- | --- |
| Problema | ¿Es claro y real? |
| Diseño | ¿La entrada, salida y revisión están definidas? |
| Prueba | ¿Se ejecutó con caso seguro? |
| Criterio | ¿Qué corrigió o verificó el humano? |
| Evidencia | ¿Qué puede mostrar sin exponer información sensible? |
| Próximo paso | ¿Hay una acción fechada? |

#### 30–60 min — Presentaciones

Tres minutos por alumno, más un minuto de feedback. Estructura obligatoria:

1. “Mi usuario/problema es…”
2. “Mi asistente recibe… y entrega…”
3. “La IA hace…, yo reviso…”
4. “La prueba mostró…”
5. “Mi siguiente ruta de credencial o proyecto es…”

El instructor ofrece feedback con: una fortaleza, un riesgo, una mejora próxima.

#### 60–72 min — Revisión cruzada

Parejas intercambian proyectos y responden: “¿Qué no entendí?”, “¿Qué podría salir mal?”, “¿Qué pregunta falta?”, “¿Qué sí me inspiró?”

#### 72–82 min — Plan de 30 días

Cada alumno anota cuatro compromisos:

- Semana 1: mejorar/probar el asistente con otro caso.
- Semana 2: completar un módulo/lab seleccionado.
- Semana 3: publicar o entregar un activo basado en el proyecto.
- Semana 4: actualizar portafolio/LinkedIn y decidir siguiente nivel.

#### 82–87 min — Constancias y evidencia

> “La constancia privada no sustituye ninguna credencial externa. Las rutas externas son tarea individual: yo te indico dónde están y qué sigue; cada proveedor emite lo suyo. Para recibir mi constancia debes cumplir el proceso completo, incluida la evidencia de la tarea/ruta que seleccionaste. Si eliges no hacerla, está bien; simplemente no cierras con constancia.”

Indicar fecha de revisión y método de entrega. Nunca prometer aprobación antes de verificar el checklist.

#### 87–90 min — Cierre

> “No terminaste un curso para presumir una herramienta. Construiste la primera versión de un sistema profesional. A partir de hoy la pregunta no es ‘¿qué IA salió?’, sino ‘¿qué problema mío puede resolver de forma responsable y demostrable?’”

Pedir feedback y autorización separada para testimonio, si aplica.

## Checklist de constancia privada

- [ ] Asistencia/visualización comprobable de las cinco sesiones.
- [ ] Mapa Profesional IA y Centro de Mando completados.
- [ ] Biblioteca de prompts y bitácora de prueba.
- [ ] Proyecto mínimo funcional presentado o evidencia equivalente aprobada.
- [ ] Evidencia de ruta/lab oficial seleccionado cuando estuvo disponible para su cuenta/región.
- [ ] Plan de 30 días.

La constancia debe llevar nombre del programa, nombre del participante, duración, fecha, firma del instructor, folio/QR si se implementa y leyenda privada de no equivalencia a título, cédula, RVOE ni certificación oficial.
