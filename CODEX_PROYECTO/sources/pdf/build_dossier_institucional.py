from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, Color
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.utils import ImageReader, simpleSplit
from pathlib import Path
import math

ROOT=Path('/Users/user/Documents/Codex/2026-07-19/new-chat')
OUT=ROOT/'output/pdf/Dossier_Comercial_Institucional_Laboratorio_IA.pdf'
HERO=ROOT/'output/pdf/assets/estudio-ologos-hero-v1.png'
W,H=1600,900
BG=HexColor('#070B12'); GLASS=HexColor('#101B2C'); GLASS2=HexColor('#14263A'); LINE=HexColor('#2A5177')
WHITE=HexColor('#F4F8FF'); MUTED=HexColor('#B2C5DB'); ORANGE=HexColor('#FF7642'); ICE=HexColor('#A8E2FF'); PURPLE=HexColor('#A786FF'); GREEN=HexColor('#8DF0B7')
try:
 pdfmetrics.registerFont(TTFont('Inter','/System/Library/Fonts/Supplemental/Arial.ttf')); pdfmetrics.registerFont(TTFont('InterB','/System/Library/Fonts/Supplemental/Arial Bold.ttf'))
except: pass
F='Inter'; B='InterB'
def R(c,x,y,w,h,fill,stroke=None,r=22,a=None):
 c.saveState();
 if a is not None:c.setFillAlpha(a)
 c.setFillColor(fill); c.setStrokeColor(stroke or fill); c.setLineWidth(1)
 c.roundRect(x,y,w,h,r,fill=1,stroke=1 if stroke else 0);c.restoreState()
def T(c,s,x,y,z=22,col=WHITE,font=F,al='left'):
 c.setFont(font,z);c.setFillColor(col)
 if al=='center':x-=stringWidth(s,font,z)/2
 if al=='right':x-=stringWidth(s,font,z)
 c.drawString(x,y,s)
def WRP(c,s,x,y,w,z=18,col=MUTED,font=F,lead=None,maxn=None):
 lead=lead or z*1.32; lines=simpleSplit(s,font,z,w);lines=lines if maxn is None else lines[:maxn]
 c.setFont(font,z);c.setFillColor(col)
 for q in lines:c.drawString(x,y,q);y-=lead
 return y
def grid(c):
 c.setFillColor(BG);c.rect(0,0,W,H,fill=1,stroke=0);c.saveState();c.setStrokeColor(Color(.35,.6,.95,alpha=.045));c.setLineWidth(.7)
 for x in range(0,W+1,80):c.line(x,0,x,H)
 for y in range(0,H+1,80):c.line(0,y,W,y)
 c.restoreState()
def head(c,k,title,sub,n):
 grid(c);R(c,70,808,1460,42,Color(.05,.12,.2,alpha=.92),LINE,18);T(c,k.upper(),94,822,13,ORANGE,B);T(c,str(n).zfill(2),1504,822,14,ICE,B,'right');T(c,title,94,748,35,WHITE,B);WRP(c,sub,94,713,1290,17,MUTED,F,23,2)
def foot(c,n):
 c.setStrokeColor(LINE);c.line(70,49,1530,49);T(c,'LABORATORIO: CREA TU ASISTENTE PERSONAL IA',70,25,11,MUTED,B);T(c,str(n).zfill(2),800,25,12,ORANGE,B,'center');T(c,'DOSSIER INSTITUCIONAL | 20 AGO 2026',1530,25,11,MUTED,B,'right')
def ico(c,kind,x,y,col=ICE):
 c.saveState();c.setFillColor(Color(col.red,col.green,col.blue,alpha=.14));c.setStrokeColor(col);c.setLineWidth(1.4);c.circle(x,y,28,fill=1,stroke=1);c.setStrokeColor(WHITE);c.setLineWidth(2.6)
 if kind=='star':
  p=c.beginPath();
  for i in range(11):
   a=-math.pi/2+i*math.pi/5;r=16 if i%2==0 else 7;px=x+r*math.cos(a);py=y+r*math.sin(a);(p.moveTo if i==0 else p.lineTo)(px,py)
  p.close();c.drawPath(p,fill=0,stroke=1)
 elif kind=='stack':
  for dy in [-10,0,10]:c.line(x-14,y+dy,x+14,y+dy)
 elif kind=='person':
  c.circle(x,y+8,6,fill=0,stroke=1);c.arc(x-14,y-15,x+14,y+6,0,180)
 elif kind=='check':c.line(x-14,y,x-3,y-11);c.line(x-3,y-11,x+16,y+13)
 elif kind=='lock':c.roundRect(x-12,y-12,24,21,4,fill=0,stroke=1);c.arc(x-9,y,x+9,y+19,0,180)
 elif kind=='flow':c.line(x-15,y,x+15,y);c.line(x+8,y+7,x+15,y);c.line(x+8,y-7,x+15,y)
 c.restoreState()
def card(c,x,y,w,h,title,body,col=ICE,kind='star'):
 R(c,x,y,w,h,Color(GLASS.red,GLASS.green,GLASS.blue,alpha=.95),LINE,26);ico(c,kind,x+48,y+h-46,col);T(c,title,x+88,y+h-53,19,WHITE,B);WRP(c,body,x+30,y+h-97,w-58,16,MUTED,F,21,4)
def chip(c,x,y,label,col):
 w=stringWidth(label,B,13)+34;R(c,x,y,w,31,Color(col.red,col.green,col.blue,alpha=.12),col,15);T(c,label,x+17,y+9,13,col,B);return w
def cover(c):
 grid(c); c.drawImage(ImageReader(str(HERO)),720,0,880,900,mask='auto',preserveAspectRatio=True,anchor='c')
 c.saveState();c.setFillColor(Color(.027,.043,.071,alpha=.87));c.rect(0,0,960,H,fill=1,stroke=0);c.restoreState()
 chip(c,92,765,'PROPUESTA PARA INSTITUCIONES Y ALIADOS',ORANGE)
 T(c,'LABORATORIO:',92,643,56,WHITE,B);T(c,'CREA TU',92,579,56,ICE,B);T(c,'ASISTENTE',92,515,56,WHITE,B);T(c,'PERSONAL IA',92,451,56,ORANGE,B)
 WRP(c,'Programa en vivo para que profesionales, emprendedores y estudiantes conviertan la inteligencia artificial en una practica util, verificable y responsable.',92,365,700,24,MUTED,F,32)
 R(c,92,143,628,118,Color(GLASS.red,GLASS.green,GLASS.blue,alpha=.9),LINE,24);T(c,'COHORTE PILOTO',122,220,14,ORANGE,B);T(c,'5 sesiones x 90 min | jueves 20:00 | Google Meet',122,183,21,WHITE,B);T(c,'Ruta individual, asistente personal y portafolio de evidencias.',122,155,16,MUTED,F)
 T(c,'DOCUMENTO DE COMERCIALIZACION',92,92,13,ICE,B)
def page2(c):
 head(c,'01 / PROPOSITO','Una experiencia que deja evidencia, no solo entusiasmo.','La propuesta convierte curiosidad por IA en competencia aplicada: cada participante configura, practica, documenta y demuestra un sistema propio.',2)
 card(c,94,410,430,235,'Aprender haciendo','El alumno parte de su propio trabajo o negocio. No usa un caso ficticio como sustituto de la practica.',ICE,'person')
 card(c,585,410,430,235,'Construir un activo','Cada persona termina con un asistente personal, un centro de mando y un portafolio inicial de evidencias.',PURPLE,'stack')
 card(c,1076,410,430,235,'Validar con criterio','Se diferencia entre constancia privada del curso y credenciales emitidas solo por proveedores externos.',GREEN,'check')
 R(c,94,145,1412,150,Color(ORANGE.red,ORANGE.green,ORANGE.blue,alpha=.10),ORANGE,26);ico(c,'star',150,220,ORANGE);T(c,'PROMESA ACADEMICA',212,245,14,ORANGE,B);WRP(c,'La persona no termina “sabiendo todo de IA”. Termina sabiendo que herramienta usar, como proteger su criterio y como producir una evidencia util para su contexto.',212,210,1160,23,WHITE,B,31,2);foot(c,2)
def page3(c):
 head(c,'02 / FICHA TECNICA','Programa base listo para comercializar.','La primera cohorte prioriza accesibilidad, practica en vivo y continuidad hacia niveles posteriores.',3)
 left=[('Modalidad','En linea, sincrona, por Google Meet. Grabacion para participantes inscritos.'),('Duracion','5 sesiones de 90 minutos. Total: 7.5 horas en vivo.'),('Horario','Jueves, 20:00 hora Monterrey. Calendario por cohorte.'),('Precio piloto','MXN $1,000 total por persona (referencia: $200 por sesion). Convenios institucionales se cotizan por grupo.'),('Cupo','Grupo reducido recomendado: 12 a 20 participantes para revision y demo.')]
 y=650
 for a,b in left:
  R(c,94,y-45,685,72,Color(GLASS.red,GLASS.green,GLASS.blue,alpha=.94),LINE,16);T(c,a,122,y,16,ICE,B);WRP(c,b,310,y,430,14,WHITE,F,18,2);y-=88
 R(c,835,288,671,392,Color(GLASS2.red,GLASS2.green,GLASS2.blue,alpha=.95),LINE,28);T(c,'DIRIGIDO A',869,632,18,WHITE,B)
 audiences=[('Emprendedores','quieren ahorrar tiempo, ordenar operaciones y crear presencia digital.'),('Freelancers y consultores','quieren elevar su entrega, propuesta y productividad sin perder criterio.'),('Estudiantes y profesionistas','quieren documentar aprendizaje y actualizar su perfil profesional.'),('Abogados / servicios profesionales','quieren utilizar IA con limites, trazabilidad y cuidado de informacion.')]
 y=586
 for a,b in audiences:ico(c,'person',900,y,ORANGE);T(c,a,946,y+6,16,WHITE,B);WRP(c,b,946,y-18,490,14,MUTED,F,18,2);y-=82
 foot(c,3)
def page4(c):
 head(c,'03 / ARQUITECTURA','Cuatro niveles; uno se comercializa hoy.','El nivel base se imparte ahora. Los siguientes son una ruta de continuidad, no una promesa de contenido ya liberado.',4)
 data=[('01','FUNDAMENTOS APLICADOS','ACTIVO','5 x 90 min','Configuracion, prompts, control de uso, asistente personal y ruta individual.',ORANGE),('02','SISTEMA PROFESIONAL','DISEÑO','proxima cohorte','Productividad, presencia digital, recursos y automatizaciones supervisadas.',ICE),('03','IMPLEMENTACION PARA NEGOCIO','DISEÑO','proxima cohorte','Procesos, equipos, tableros y orquestacion de herramientas para un caso real.',PURPLE),('04','EXPERT LAB','EXPLORACION','por definir','Laboratorio selectivo para proyectos, integraciones y demostraciones avanzadas.',GREEN)]
 y=632
 for no,title,state,dur,desc,col in data:
  R(c,94,y-54,1412,99,Color(GLASS.red,GLASS.green,GLASS.blue,alpha=.94),LINE,20);T(c,no,126,y-2,24,col,B);T(c,title,220,y+8,21,WHITE,B);chip(c,635,y-4,state,col);T(c,dur,867,y+8,16,ICE,B);WRP(c,desc,1065,y+10,395,14,MUTED,F,18,2);y-=119
 foot(c,4)
def page5(c):
 head(c,'04 / SESIONES','La cohorte base no es un temario de diapositivas.','Cada encuentro une conceptos minimos, demostracion, practica guiada y una evidencia que se integra al portafolio.',5)
 sessions=[('01','TU PERFIL + TU RUTA','Diagnostico, mapa de objetivos, ecosistema de herramientas y seleccion de ruta externa.'),('02','TU CENTRO DE MANDO','Notion o Google Drive como estructura de proyectos, recursos, prompts y tareas.'),('03','TU ASISTENTE PERSONAL','Instrucciones, contexto, conectores disponibles, modos de trabajo y verificacion humana.'),('04','LABORATORIO GOOGLE IA','Google AI Studio, Gemini, NotebookLM y rutas de aprendizaje; experimentacion controlada.'),('05','DEMO DAY','Caso real, portafolio, plan de 30 dias y siguientes pasos hacia nivel intermedio.')]
 x=94
 for no,a,b in sessions:
  R(c,x,322,260,335,Color(GLASS.red,GLASS.green,GLASS.blue,alpha=.95),LINE,25);T(c,no,x+28,602,29,ORANGE,B);WRP(c,a,x+28,551,204,18,WHITE,B,23,3);WRP(c,b,x+28,451,204,15,MUTED,F,20,5);x+=286
 R(c,94,140,1412,115,Color(ICE.red,ICE.green,ICE.blue,alpha=.08),ICE,24);T(c,'EVIDENCIA MINIMA POR SESION',124,208,14,ICE,B);WRP(c,'Diagnostico - centro de mando - configuracion de asistente - bitacora de laboratorio - demo y plan de continuidad.',124,171,1210,21,WHITE,B,28);foot(c,5)
def page6(c):
 head(c,'05 / STACK QUE SE ENSENA','No es una lista de apps: es un criterio para combinarlas.','Se explican costos, niveles gratuitos, limitaciones, privacidad y como evitar pagar por herramientas que no se usaran.',6)
 cols=[('CONVERSACION Y RAZONAMIENTO',['ChatGPT','Claude','Gemini','Grok'],ICE),('CREACION Y CONOCIMIENTO',['Canva','NotebookLM','Google AI Studio','Google Drive'],PURPLE),('TRABAJO Y EVIDENCIA',['Notion','Google Docs','Google Meet','GitHub opcional'],ORANGE),('RUTAS EXTERNAS',['Google Skills','AWS Skill Builder','Microsoft Learn','IBM SkillsBuild'],GREEN)]
 x=94
 for h,items,col in cols:
  R(c,x,260,330,400,Color(GLASS.red,GLASS.green,GLASS.blue,alpha=.96),LINE,26);ico(c,'stack',x+50,600,col);WRP(c,h,x+32,540,260,18,WHITE,B,23,2);y=480
  for it in items:R(c,x+32,y,266,43,Color(col.red,col.green,col.blue,alpha=.10),col,14);T(c,it,x+51,y+14,15,WHITE,B);y-=57
  x+=356
 T(c,'Cada proveedor conserva sus propios términos, planes, límites y requisitos de elegibilidad.',94,170,16,MUTED,F);foot(c,6)
def page7(c):
 head(c,'06 / STACK ENTREGABLE','Recursos que siguen vivos despues de la ultima sesion.','El paquete de salida esta pensado para que el alumno pueda continuar solo y para que la institución pueda observar evidencia tangible.',7)
 cards=[('CENTRO DE MANDO','Plantilla editable en Notion o Drive para recursos, calendario, prompts, tareas y evidencia.',ICE,'stack'),('KIT DE PROMPTS','Prompts contextualizables para investigar, redactar, planear, revisar y convertir ideas en entregables.',ORANGE,'star'),('RUTA PERSONAL','Mapa inicial de herramientas, objetivos y credenciales externas que el alumno puede perseguir por cuenta propia.',GREEN,'flow'),('PORTAFOLIO BASE','Estructura de carpeta / repositorio opcional con bitacora, evidencias y demo del proyecto personal.',PURPLE,'check'),('GUIA DE SEGURIDAD','Checklist de datos sensibles, verificacion de resultados y reglas de uso responsable.',ICE,'lock'),('PLAN 30 DIAS','Siguientes acciones ordenadas por impacto para consolidar habitos y elegir el siguiente nivel.',ORANGE,'flow')]
 x,y=94,475
 for i,(a,b,col,k) in enumerate(cards):
  card(c,x,y,430,190,a,b,col,k)
  x+=458
  if i==2:
   x,y=94,250
 foot(c,7)
def page8(c):
 head(c,'07 / FLUJO OPERATIVO','Una operación diseñada para no depender de memoria y mensajes dispersos.','Este es el blueprint que se puede activar. La automatizacion real requiere cuentas, permisos, politicas y aprobacion de la institución.',8)
 steps=[('1','REGISTRO','Landing / formulario / pago','Datos minimos y consentimiento.'),('2','ONBOARDING','Correo + acceso + diagnostico','Ruta inicial y calendario.'),('3','SESIONES','Meet + materiales + bitacora','Asistencia y evidencia por sesion.'),('4','REVISION','Checklist + retroalimentacion','No se valida aprendizaje solo por presencia.'),('5','CIERRE','Demo Day + constancia privada','Entrega condicionada a requisitos.'),('6','CONTINUIDAD','Plan 30 dias + nivel siguiente','Oferta opcional, nunca automatica.')]
 x=88
 for n,a,b,d in steps:
  R(c,x,385,220,250,Color(GLASS.red,GLASS.green,GLASS.blue,alpha=.96),LINE,24);T(c,n,x+27,579,24,ORANGE,B);WRP(c,a,x+27,540,166,16,WHITE,B,21,2);WRP(c,b,x+27,492,166,14,ICE,B,18,2);WRP(c,d,x+27,434,166,13,MUTED,F,17,3);x+=244
 R(c,94,150,1412,125,Color(ORANGE.red,ORANGE.green,ORANGE.blue,alpha=.09),ORANGE,24);ico(c,'lock',148,213,ORANGE);WRP(c,'Automatizable con aprobacion: recordatorios, calendarizacion, entrega de enlaces y centralizacion de evidencia. No se automatiza la evaluación sustantiva, las decisiones academicas ni el manejo de informacion sensible.',210,230,1150,20,WHITE,B,27,3);foot(c,8)
def page9(c):
 head(c,'08 / EVALUACION Y CREDENCIALES','Claridad sobre lo que si se acredita.','La confianza institucional nace de separar participacion, evidencia de aprendizaje y certificados que pertenecen a terceros.',9)
 card(c,94,425,430,235,'Evidencia del Laboratorio','Asistencia, bitacora, entregables por sesion y demo final. Estos criterios rigen acceso a constancia privada. ',ICE,'check')
 card(c,585,425,430,235,'Constancia privada','Puede emitirse por el programa al cumplir requisitos publicados. No es un certificado oficial de proveedor externo.',ORANGE,'lock')
 card(c,1076,425,430,235,'Credenciales externas','Google, AWS, Microsoft, IBM u otros proveedores emiten sus propios badges y certificados bajo sus reglas.',GREEN,'star')
 R(c,94,155,1412,145,Color(PURPLE.red,PURPLE.green,PURPLE.blue,alpha=.10),PURPLE,26);T(c,'GARANTIA DE INTEGRIDAD',124,245,14,PURPLE,B);WRP(c,'El curso ensena como encontrar rutas y como organizar evidencia. No promete aprobar exámenes, obtener beneficios de terceros ni representar a instituciones que no sean parte formal del programa.',124,210,1220,21,WHITE,B,28,2);foot(c,9)
def page10(c):
 head(c,'09 / PARA DIRECTIVOS','Que obtiene una institución al habilitar la cohorte.','Una experiencia de actualización profesional que puede presentarse como beneficio educativo, programa de empleabilidad o laboratorio de innovación.',10)
 rows=[('DIAGNOSTICO INICIAL','Mapa agregado de necesidades del grupo, sin publicar datos personales.'),('EXPERIENCIA GUIADA','Cinco sesiones con demostraciones, práctica y objetivos de evidencia.'),('REPORTE DE CIERRE','Participación, entregables y aprendizajes agregados; alcance definido con la institución.'),('ACTIVO REUTILIZABLE','Plantillas y guías para que el grupo continúe después de la cohorte.'),('RUTA DE CONTINUIDAD','Opciones de nivel intermedio o implementación institucional, bajo propuesta separada.')]
 y=620
 for i,(a,b) in enumerate(rows):R(c,94,y-37,1412,72,Color(GLASS.red,GLASS.green,GLASS.blue,alpha=.94),LINE,18);T(c,str(i+1).zfill(2),124,y-1,16,ORANGE,B);T(c,a,205,y+3,18,WHITE,B);WRP(c,b,655,y+3,680,15,MUTED,F,19,2);y-=89
 R(c,94,120,1412,100,Color(GREEN.red,GREEN.green,GREEN.blue,alpha=.08),GREEN,24);WRP(c,'Propuesta de conversación: "No venimos a sustituir carreras. Venimos a dar a cada participante una capa de criterio, productividad y evidencia para trabajar mejor con IA."',124,169,1230,21,WHITE,B,28,2);foot(c,10)
def page11(c):
 head(c,'10 / COMERCIALIZACION','Una oferta clara, responsable y escalable.','La comunicación debe vender transformación práctica, no promesas de ingresos garantizados ni credenciales ajenas.',11)
 card(c,94,410,430,235,'Oferta al alumno','Cohorte base: MXN $1,000 por participante. Incluye cinco sesiones, recursos, ruta y revisión de evidencias.',ORANGE,'star')
 card(c,585,410,430,235,'Oferta a institución','Grupo cerrado, personalización de casos y reporte agregado. Precio por grupo tras definir tamaño, soporte y alcance.',ICE,'person')
 card(c,1076,410,430,235,'Oferta a aliado','Patrocinio de becas, acceso a herramienta o participación técnica, solo con autorización y términos por escrito.',GREEN,'check')
 R(c,94,140,1412,150,Color(GLASS2.red,GLASS2.green,GLASS2.blue,alpha=.95),LINE,26);T(c,'MENSAJES QUE SI DEBEN APARECER',124,246,14,ICE,B);WRP(c,'Asistente personal - sistema de productividad - proyecto demostrable - ruta de aprendizaje - uso responsable - herramientas con niveles gratuitos y de pago.',124,211,1220,21,WHITE,B,28,2);T(c,'EVITAR: “certificación oficial incluida”, “empleo garantizado”, “ingresos garantizados”, logos o avales no autorizados.',124,165,16,ORANGE,B);foot(c,11)
def page12(c):
 head(c,'11 / SIGUIENTE PASO','De propuesta a piloto.','El objetivo de la primera colaboración es verificar utilidad, experiencia y evidencia; después, escalar solamente lo que funciona.',12)
 timeline=[('SEMANA 0','Alineación con institución','Objetivos, grupo, privacidad, responsables y modalidad.'),('SEMANA 1','Registro + diagnóstico','Onboarding, calendario y rutas individuales.'),('SEMANAS 2-6','5 sesiones del Laboratorio','Práctica, evidencias, acompañamiento y recursos.'),('SEMANA 7','Demo Day + reporte','Cierre, resultados agregados y decisión de continuidad.')]
 y=625
 for i,(a,b,d) in enumerate(timeline):
  R(c,94,y-40,1412,83,Color(GLASS.red,GLASS.green,GLASS.blue,alpha=.95),LINE,20);T(c,str(i+1).zfill(2),126,y-2,21,ORANGE,B);T(c,a,206,y+7,18,ICE,B);T(c,b,462,y+7,19,WHITE,B);WRP(c,d,880,y+7,500,15,MUTED,F,19,2);y-=103
 R(c,94,142,1412,119,Color(ORANGE.red,ORANGE.green,ORANGE.blue,alpha=.10),ORANGE,24);T(c,'DECISION QUE NECESITAMOS DEL DIRECTIVO',124,215,14,ORANGE,B);WRP(c,'Autorizar una reunión de 30 minutos para definir población, tamaño de cohorte, política de datos, condiciones de difusión y objetivo de impacto.',124,178,1120,21,WHITE,B,28,2);foot(c,12)
def make():
 OUT.parent.mkdir(parents=True,exist_ok=True);c=canvas.Canvas(str(OUT),pagesize=(W,H),pageCompression=1);c.setTitle('Dossier institucional - Laboratorio IA')
 for fn in [cover,page2,page3,page4,page5,page6,page7,page8,page9,page10,page11,page12]:fn(c);c.showPage()
 c.save()
if __name__=='__main__':make()
