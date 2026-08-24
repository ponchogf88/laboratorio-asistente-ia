# Google AI Studio como fábrica del curso

Fecha de investigación: 19 de agosto de 2026  
Proyecto: **Laboratorio: Crea tu Asistente Personal IA**

## Dictamen ejecutivo

Sí conviene usar Google AI Studio desde hoy, pero no como plataforma para alojar alumnos ni como sustituto de tu criterio docente. Su mejor papel en la primera cohorte es ser una **fábrica editorial y laboratorio de prompts**: nos ayuda a convertir la Course Bible en sesiones, ejercicios, guiones, rúbricas, diapositivas, piezas de lanzamiento y revisiones de calidad repetibles.

La secuencia correcta es:

1. **Primero:** crear el curso y sus activos en AI Studio con revisión humana.
2. **Después de probar una cohorte:** automatizar las salidas repetibles con la Gemini API y salidas estructuradas.
3. **Sólo si la demanda lo justifica:** construir un portal de alumnos con autenticación, pagos, progreso y privacidad. Eso ya es otro producto, no un experimento de fin de semana.

No recomiendo clonar todavía un “AI course generator” completo. Añadiría complejidad (usuarios, pagos, base de datos, seguridad y mantenimiento) antes de comprobar qué partes del método realmente valoran los alumnos.

## Qué puede hacer AI Studio por el curso

Google AI Studio permite experimentar con modelos y prompts, guardar el experimento y obtener código cuando ya se quiere pasar a la API. En sus ajustes se pueden configurar instrucciones del sistema, seguridad y herramientas como salida estructurada, function calling, code execution y grounding.

| Trabajo del curso | Uso recomendado en AI Studio | Revisión humana obligatoria |
| --- | --- | --- |
| Arquitectura de 5 sesiones | Prompt de arquitecto instruccional + Course Bible | Promesa, duración, nivel y coherencia pedagógica |
| Guiones de clase | Prompt por sesión con agenda fija de 90 min | Demos realmente ejecutables y tono del instructor |
| Workbook y tareas | Generar borrador con criterios y ejemplo de buena evidencia | Que la tarea corresponda al resultado que se evalúa |
| Diapositivas y storyboard del explainer | Convertir una sesión o landing en bloques visuales | Diseño final, copyright y mensajes de venta |
| Investigación de herramientas/certificaciones | Grounding sólo con fuentes oficiales, URLs y fecha | Vigencia, elegibilidad, precios y atribución de cada proveedor |
| Rúbrica y QA | Revisor que marque afirmaciones no demostradas o promesas riesgosas | Decisión final antes de publicar |

## Lo que no debe hacer por sí solo

- No sustituye el LMS ni resguarda expedientes de alumnos.
- No debe recibir datos confidenciales de clientes, expedientes jurídicos, claves API ni datos personales innecesarios.
- No debe emitir ni prometer credenciales de Google, AWS, IBM, Microsoft u otras entidades.
- No debe inventar requisitos, costos, rutas o validez de certificaciones. Cuando se trate de información actualizable, se investiga en fuente oficial y se etiqueta con fecha.
- No debe tomar decisiones de publicación sin una revisión humana de exactitud, privacidad, derechos y tono.

## Operación recomendada: cinco espacios de trabajo

En lugar de un chat gigante, crea cinco prompts guardados o conversaciones separadas. Cada uno recibe la versión vigente de la Course Bible y una tarea concreta.

1. **Arquitecto del curso**: traduce la promesa, público y resultados a la estructura de la cohorte.
2. **Diseñador de sesión**: produce la agenda de 90 minutos, demo, práctica, entregable, tarea y evaluación de una sola sesión.
3. **Creador de artefactos**: crea workbook, plantilla, checklist, guion de teleprompter y storyboard.
4. **Investigador verificable**: sólo investiga con URLs oficiales, fecha de consulta y etiquetas de incertidumbre.
5. **Auditor pedagógico y de claims**: detecta humo, afirmaciones sin evidencia, promesas de ingreso y confusiones sobre certificaciones.

No copies conversaciones interminables entre sesiones. Conserva un documento fuente único y pega sólo el extracto pertinente a cada tarea: reduce contradicciones, contaminación de contexto y consumo innecesario de tokens.

## Método de prompting que sí sirve para este curso

La documentación oficial recomienda instrucciones claras, contexto suficiente, ejemplos consistentes y pruebas iterativas. Para este proyecto, cada prompt debe tener estas seis capas:

1. **Rol limitado**: qué función cumple y qué no decide.
2. **Fuente de verdad**: pegar sólo el fragmento vigente de la Course Bible, no suposiciones.
3. **Tarea atómica**: una sesión, una rúbrica o una pieza; no “haz el curso completo”.
4. **Restricciones**: duración, audiencia, tono de español MX, salvaguardas legales/comerciales y formato.
5. **Uno o dos ejemplos**: demuestran el estilo, profundidad y estructura esperados.
6. **Salida verificable**: tabla o JSON con campos obligatorios; separar hechos, hipótesis y pendientes de validar.

### Reglas de calidad para cada prompt

- Especifica qué se debe entregar y qué debe evitarse.
- Da ejemplos cortos y consistentes; no metas veinte ejemplos que vuelvan rígida la respuesta.
- Para información actual, pide URL primaria, fecha de consulta y cita al lado de cada afirmación.
- Para cálculos de tiempo, precio o calendario, usa code execution sólo para la matemática; no como fuente de hechos externos.
- Para noticias o proveedores, activa grounding y exige que el modelo no complete huecos con suposiciones.
- Cuando llevemos esto a código, usa **structured output** con JSON Schema para evitar que un generador rompa el formato de las sesiones.

## Prompt maestro para AI Studio: Diseñador de sesión

Pega primero la Course Bible o el fragmento que corresponda. Después usa esta plantilla y reemplaza los corchetes.

```text
<ROL>
Eres el diseñador instruccional del curso "Laboratorio: Crea tu Asistente Personal IA".
Tu trabajo es crear un borrador verificable para revisión del instructor; no inventas
hechos, avales, certificaciones, precios, requisitos de proveedores ni resultados económicos.
</ROL>

<FUENTE_DE_VERDAD>
[PEGA AQUÍ EL EXTRACTO VIGENTE DE LA COURSE BIBLE]
</FUENTE_DE_VERDAD>

<REGLAS_NO_NEGOCIABLES>
- Público: emprendedores, freelancers, estudiantes, abogados y consultores de nivel inicial a bajo-intermedio.
- Español de México, directo, cálido y sin tecnicismos innecesarios.
- Cada sesión dura exactamente 90 minutos y debe culminar en un artefacto práctico.
- Las rutas externas de Google, AWS, IBM, Microsoft u otros proveedores las emite cada proveedor;
  no prometas certificaciones externas ni preparación de exámenes.
- Si un dato depende de actualidad, escribe "POR VERIFICAR" y no lo presentes como hecho.
- Nunca pidas datos confidenciales, expedientes, credenciales, claves API ni datos personales de terceros.
- Evita promesas de dinero, empleo garantizado o automatización infalible.
</REGLAS_NO_NEGOCIABLES>

<TAREA>
Diseña la sesión [NÚMERO Y NOMBRE]. Su resultado observable es: [RESULTADO].
Incluye una demo realista de [HERRAMIENTA/CASO], una práctica guiada y una tarea que
el alumno pueda completar desde su propia cuenta.
</TAREA>

<FORMATO_DE_SALIDA>
Devuelve una tabla con:
1) objetivo observable;
2) hook inicial de máximo 30 segundos;
3) agenda minuto a minuto que sume 90;
4) demo; 5) práctica; 6) artefacto entregable; 7) tarea; 8) criterio de evidencia;
9) riesgos/advertencias; 10) afirmaciones que requieren fuente oficial.

Al final agrega:
- "Decisiones del instructor requeridas";
- "Datos por verificar";
- "Qué NO prometer en ventas".
</FORMATO_DE_SALIDA>
```

### Prompt de auditoría antes de publicar

```text
Actúa como auditor pedagógico y de claims. Revisa el siguiente activo del curso.
No lo reescribas todavía.

Devuelve una tabla con: fragmento, problema detectado, tipo (hecho sin fuente /
promesa económica / confusión de credencial / riesgo de privacidad / ambigüedad
pedagógica / tono), severidad (alta-media-baja), corrección sugerida y fuente
primaria necesaria cuando aplique.

Reglas: no atribuyas aval a UANL, Google ni ninguna institución sin autorización;
las credenciales externas las emite cada proveedor; no aceptar datos confidenciales
en herramientas de IA.

ACTIVO:
[PEGA AQUÍ EL TEXTO]
```

## Primer sprint: qué producir esta semana

| Día | Salida | Herramienta/función | Criterio de salida |
| --- | --- | --- | --- |
| 1 | Fuente única compacta de la Course Bible | AI Studio + revisión manual | Una sola versión de público, promesa, sesiones, límites y entregables |
| 2 | Sesiones 1 y 2 + workbook | Prompt Diseñador de sesión | Cada agenda suma 90 min y cada práctica deja evidencia |
| 3 | Sesiones 3, 4 y 5 + Demo Day | Prompt Diseñador de sesión | Secuencia sin saltos de dificultad |
| 4 | Rúbrica, checklist y política de constancia | Prompt de auditoría | Sin confundir constancia privada con credencial externa |
| 5 | Landing, webinar y 8 piezas de lanzamiento | Creador de artefactos | Claims verificables, CTA claro y no promesas de ingreso |
| 6 | Ensayo del primer módulo | Grabación de pantalla + guion | Demo ejecutable, duración real y errores anotados |
| 7 | Revisión final y backlog | Auditor + instructor | Lista de ajustes priorizada antes de abrir inscripciones |

## Repositorios evaluados

| Repositorio | Estado | Para qué sí | Riesgo / decisión |
| --- | --- | --- | --- |
| [google-gemini/cookbook](https://github.com/google-gemini/cookbook) | Oficial, Apache-2.0 | Patrones y ejemplos actuales del Gemini API: prompts, archivos, búsqueda y herramientas | **Usar como referencia técnica ahora.** No es un LMS ni un producto listo para vender. |
| [GoogleCloudPlatform/generative-ai](https://github.com/GoogleCloudPlatform/generative-ai) | Oficial, Apache-2.0 | Notebooks y patrones de RAG, grounding y agentes para una futura capa de automatización | **Guardar para fase 3.** Es demasiado amplio y orientado a Google Cloud para la primera cohorte. |
| [google-gemini/gemini-api-quickstart](https://github.com/google-gemini/gemini-api-quickstart) | Oficial | Base mínima si construimos un pequeño panel privado de “Course Factory” | **Posible fase 2.** Requiere revisión de seguridad y API key sólo del lado servidor. |
| [AI-Course_Generator](https://github.com/ManishSingh00/AI-Course_Generator) | Comunitario | Inspira el flujo tema → módulos → recursos y la arquitectura de una app educativa | **No clonar aún.** Primero auditar licencia, dependencias, manejo de claves, autenticación y pagos. |
| [CourseCraft](https://github.com/AnuragSinghDhami/CourseCraft) | Comunitario | Lista de funciones a considerar después: rutas, contenido dinámico, auth y pagos | **Referencia, no incorporación inmediata.** Evitar heredar deuda técnica de un repo ajeno. |

### Decisión de repos

No clonamos nada por ahora. La incorporación segura, cuando ya exista evidencia de uso, sería tomar **patrones puntuales** de los repos oficiales, crear un repositorio propio y escribir sólo el módulo mínimo: un formulario interno que genere una sesión en JSON, la someta a auditoría y guarde el borrador. No debe tener pagos, expedientes de alumnos ni publicación automática en su primera versión.

## Arquitectura futura, sólo cuando haga falta

```text
Course Bible aprobada
        ↓
AI Studio: prueba y mejora de prompts
        ↓
Gemini API (servidor) + salida estructurada JSON
        ↓
Panel privado: sesión / workbook / rúbrica / QA
        ↓
Revisión humana y control de versiones
        ↓
Canva, Docs, Slides y plataforma de entrega elegida
```

Más adelante, function calling tendría sentido para pedir una acción concreta a herramientas propias (por ejemplo, guardar un borrador aprobado en una base de conocimiento interna). No es necesario para generar la primera versión del curso.

## Seguridad y propiedad intelectual

- Guarda la clave de Gemini en variables de entorno de un servidor; nunca en una landing, un repositorio público ni un navegador de alumno.
- Revisa la licencia de cualquier repo antes de copiar, redistribuir o vender código derivado.
- El contenido generado se edita: no publiques de forma automática textos, cifras, recomendaciones legales o referencias de certificación.
- Usa ejemplos ficticios o anonimizados para el track legal y de consultoría.

## Fuentes consultadas

- Google AI Studio: [quickstart oficial](https://ai.google.dev/gemini-api/docs/ai-studio-quickstart).
- Google: [estrategias de prompting](https://ai.google.dev/gemini-api/docs/prompting-strategies).
- Google: [salidas estructuradas](https://ai.google.dev/gemini-api/docs/structured-output).
- Google: [function calling](https://ai.google.dev/gemini-api/docs/function-calling).
- GitHub oficial: [Gemini Cookbook](https://github.com/google-gemini/cookbook) y [Google Cloud generative-ai](https://github.com/GoogleCloudPlatform/generative-ai).
- Referencias comunitarias evaluadas: [AI-Course_Generator](https://github.com/ManishSingh00/AI-Course_Generator) y [CourseCraft](https://github.com/AnuragSinghDhami/CourseCraft).
