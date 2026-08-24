from reportlab.lib.colors import HexColor, Color
from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.colors import white
from pathlib import Path

OUT = Path('output/pdf/Manifiesto_Estudio_de_Produccion_Educativa_IA.pdf')
HERO = Path('output/pdf/assets/estudio-ologos-hero-v1.png')
PAGE_W, PAGE_H = landscape(A4)

BG = HexColor('#08090B')
PANEL = HexColor('#121419')
PANEL_2 = HexColor('#171A20')
LINE = HexColor('#2B3039')
TEXT = HexColor('#F4F2EE')
MUTED = HexColor('#A8ADB7')
ORANGE = HexColor('#FF7642')
BLUE = HexColor('#A8E2FF')
WHITE = HexColor('#FFFFFF')

FONT_REG = 'Helvetica'
FONT_BOLD = 'Helvetica-Bold'

def fit(c, text, max_w, font=FONT_REG, start=20, min_size=7):
    size = start
    while size > min_size and stringWidth(text, font, size) > max_w:
        size -= .5
    c.setFont(font, size)
    return size

def rect(c, x, y, w, h, fill=PANEL, stroke=LINE, radius=18, alpha=1):
    c.saveState(); c.setFillColor(fill); c.setStrokeColor(stroke); c.setLineWidth(.7)
    if alpha != 1: c.setFillAlpha(alpha); c.setStrokeAlpha(.72)
    c.roundRect(x, y, w, h, radius, fill=1, stroke=1); c.restoreState()

def pill(c, x, y, label, accent=ORANGE):
    w = stringWidth(label, FONT_BOLD, 7.5) + 18
    c.saveState(); c.setFillColor(accent); c.setFillAlpha(.15); c.setStrokeColor(accent); c.setStrokeAlpha(.65)
    c.roundRect(x, y, w, 17, 8.5, fill=1, stroke=1); c.restoreState()
    c.setFillColor(accent); c.setFont(FONT_BOLD, 7.5); c.drawString(x+9, y+5.2, label)
    return w

def label(c, x, y, text, accent=ORANGE):
    c.setFillColor(accent); c.setFont(FONT_BOLD, 8); c.drawString(x, y, text.upper())

def text(c, x, y, value, size=11, color=TEXT, font=FONT_REG):
    c.setFillColor(color); c.setFont(font, size); c.drawString(x, y, value)

def wrap(c, value, max_w, font=FONT_REG, size=10):
    words=value.split(); lines=[]; line=''
    for word in words:
        trial=(line+' '+word).strip()
        if stringWidth(trial,font,size) <= max_w:
            line=trial
        else:
            if line: lines.append(line)
            line=word
    if line: lines.append(line)
    return lines

def paragraph(c,x,y,value,max_w,size=10,color=MUTED,leading=14,font=FONT_REG):
    c.setFillColor(color); c.setFont(font,size)
    for line in wrap(c,value,max_w,font,size):
        c.drawString(x,y,line); y-=leading
    return y

def footer(c, num, title='ESTUDIO DE PRODUCCION EDUCATIVA IA'):
    c.setStrokeColor(LINE); c.setLineWidth(.6); c.line(38, 25, PAGE_W-38, 25)
    text(c, 38, 12, title, 6.7, MUTED, FONT_BOLD)
    text(c, PAGE_W-55, 12, f'{num:02d}', 7, ORANGE, FONT_BOLD)

def orb(c, x,y,r, glow=ORANGE):
    c.saveState()
    for i in range(7,0,-1):
        c.setFillColor(glow); c.setFillAlpha(.012*i)
        c.circle(x,y,r+(8-i)*5,fill=1,stroke=0)
    c.setFillColor(Color(.06,.09,.12)); c.setFillAlpha(.92); c.setStrokeColor(glow); c.setStrokeAlpha(.9); c.setLineWidth(1.2)
    c.circle(x,y,r,fill=1,stroke=1)
    c.setStrokeColor(BLUE); c.setStrokeAlpha(.8); c.circle(x,y,r*.64,fill=0,stroke=1)
    c.setFillColor(glow); c.setFillAlpha(.85); c.circle(x,y,r*.13,fill=1,stroke=0)
    c.restoreState()

def role_card(c,x,y,w,h,role,mission,accent):
    rect(c,x,y,w,h,PANEL_2,LINE,15,.95)
    c.saveState(); c.setFillColor(accent); c.setFillAlpha(.16); c.circle(x+22,y+h-21,9,fill=1,stroke=0); c.restoreState()
    c.setFillColor(accent); c.setFont(FONT_BOLD,12); c.drawCentredString(x+22,y+h-24,'+')
    text(c,x+39,y+h-22,role,10.5,TEXT,FONT_BOLD)
    paragraph(c,x+18,y+h-43,mission,w-36,8.4,MUTED,11)

def page_bg(c):
    c.setFillColor(BG); c.rect(0,0,PAGE_W,PAGE_H,fill=1,stroke=0)
    c.saveState(); c.setStrokeColor(HexColor('#18202B')); c.setStrokeAlpha(.35); c.setLineWidth(.25)
    for xx in range(0,int(PAGE_W)+1,28): c.line(xx,0,xx,PAGE_H)
    for yy in range(0,int(PAGE_H)+1,28): c.line(0,yy,PAGE_W,yy)
    c.restoreState()

c = canvas.Canvas(str(OUT), pagesize=(PAGE_W,PAGE_H))
c.setTitle('Manifiesto - Estudio de Produccion Educativa IA')
c.setAuthor('Laboratorio: Crea tu Asistente Personal IA')

# 1 COVER
page_bg(c)
c.drawImage(ImageReader(str(HERO)), 0, 0, width=PAGE_W, height=PAGE_H, mask='auto')
c.saveState(); c.setFillColor(BG); c.setFillAlpha(.77); c.rect(0,0,PAGE_W*.58,PAGE_H,fill=1,stroke=0); c.restoreState()
c.saveState(); c.setFillColor(BG); c.setFillAlpha(.35); c.rect(0,0,PAGE_W,PAGE_H,fill=1,stroke=0); c.restoreState()
pill(c,46,470,'MANIFIESTO OPERATIVO',ORANGE)
text(c,46,412,'EL ESTUDIO DE',31,TEXT,FONT_BOLD)
text(c,46,367,'PRODUCCION',39,TEXT,FONT_BOLD)
text(c,46,322,'EDUCATIVA IA',39,ORANGE,FONT_BOLD)
paragraph(c,48,278,'No es un curso con diapositivas. Es una fabrica de transformacion profesional verificable: personas, agentes, evidencia y proyectos que se conectan para mover una cohorte completa.',360,11.3,TEXT,16)
rect(c,46,90,360,92,HexColor('#101419'),HexColor('#455161'),17,.82)
label(c,65,153,'PREMISA')
paragraph(c,65,132,'Un alumno no compra clases. Compra una nueva capacidad de construir, demostrar y escalar.',305,10.1,TEXT,14,FONT_BOLD)
text(c,47,45,'DOCUMENTO FUNDACIONAL · COHORTE 1 · MONTERREY',7,MUTED,FONT_BOLD)
c.showPage()

# 2 THE IDEA
page_bg(c); footer(c,2)
label(c,48,520,'01 / LA TESIS')
text(c,48,476,'No contratamos un diseñador.',29,TEXT,FONT_BOLD)
text(c,48,439,'Construimos un estudio.',29,ORANGE,FONT_BOLD)
paragraph(c,48,400,'Un sistema donde cada disciplina convierte una parte de la experiencia educativa en algo mas claro, mas bello, mas verificable y mas vendible.',510,11,MUTED,16)

items=[('CURSO','sesiones y tareas','Una experiencia que se termina, no solo se consume.'),('PORTAFOLIO','proyectos y evidencia','La prueba visible de que el alumno sabe resolver algo.'),('CREDENCIALES','rutas externas','Badges y certificados emitidos por cada proveedor, cuando el alumno cumple.'),('COMUNIDAD','rituales y demo','El grupo que exige avance, celebra evidencia y genera casos reales.')]
for i,(a,b,d) in enumerate(items):
    x=48+(i%2)*353; y=270-(i//2)*126
    rect(c,x,y,320,98,PANEL,LINE,18,.96); pill(c,x+18,y+63,a,ORANGE if i<2 else BLUE); text(c,x+18,y+44,b,13,TEXT,FONT_BOLD); paragraph(c,x+18,y+26,d,270,8.7,MUTED,11)
c.showPage()

# 3 ORCHESTRATION
page_bg(c); footer(c,3)
label(c,48,520,'02 / EL SISTEMA')
text(c,48,481,'Un centro. Muchos ologos.',28,TEXT,FONT_BOLD)
paragraph(c,48,452,'No necesitas veinte contrataciones el primer dia. Necesitas roles claros: algunos humanos, otros asistidos por IA, todos con una salida verificable.',565,10.5,MUTED,15)
cx,cy=420,270
for ax,ay,name in [(165,310,'ESTRATEGIA'),(256,172,'CONTENIDO'),(550,172,'AUTOMATIZACION'),(676,305,'VERIFICACION'),(410,420,'EXPERIENCIA')]:
    c.saveState(); c.setStrokeColor(BLUE); c.setStrokeAlpha(.35); c.setLineWidth(1); c.line(cx,cy,ax,ay); c.restoreState()
    rect(c,ax-62,ay-20,124,40,HexColor('#151D27'),HexColor('#39536C'),14,.9); text(c,ax,ay-3,name,7.2,BLUE,FONT_BOLD)
orb(c,cx,cy,66,ORANGE); text(c,cx,cy+7,'TODO',15,TEXT,FONT_BOLD); text(c,cx,cy-13,'LOGO',15,ORANGE,FONT_BOLD)
rect(c,50,72,740,62,HexColor('#111720'),HexColor('#334357'),18,.88)
text(c,72,106,'EL TODÓLOGO',11,ORANGE,FONT_BOLD)
paragraph(c,72,88,'Tu rol: decidir que importa, proteger la vision, priorizar la siguiente accion y evitar que veinte ideas se conviertan en cero lanzamientos.',650,9.5,TEXT,13)
c.showPage()

# 4 Roles
page_bg(c); footer(c,4)
label(c,48,520,'03 / LOS OLOGOS')
text(c,48,481,'Cada rol tiene un resultado.',27,TEXT,FONT_BOLD)
roles=[
('DISENADOLOGO','Convierte contenido en interfaz, workbook, dashboard y experiencia visual.',ORANGE),('IMAGENELOGO','Crea avatar, renders, iconos, fotografia y lenguaje de marca.',BLUE),('VIDEOLOGO','Produce explainer, reels, grabaciones, cortes y subtitulos.',ORANGE),('PRESENTACIONOLOGO','Transforma las sesiones en narrativa visual: imagen, practica y ritmo.',BLUE),
('ESTRATEGOLOGO','Define oferta, posicionamiento, precio, lanzamiento y competencia.',ORANGE),('CURRICULOLOGO','Diseña misiones, ejercicios, rubricas, tiempos y aprendizaje.',BLUE),('CERTIFICATOLOGO','Mapea rutas externas, evidencia, requisitos, fechas y progreso.',ORANGE),('VERIFICATOLOGO','Revisa fuentes, vigencia, elegibilidad y promesas de venta.',BLUE),
('ADMINISTRANOLOGO','Opera inscripciones, pagos, Meet, acceso, soporte y recordatorios.',ORANGE),('AUTOMATIZOLOGO','Conecta registro, onboarding, tareas, evidencia y seguimiento.',BLUE),('JARVISOLOGO','Diseña asistentes: instrucciones, memoria, comandos, pruebas y limites.',ORANGE),('PORTAFOLIOLOGO','Convierte evidencia en GitHub, LinkedIn y casos de estudio.',BLUE),
('CONTENIDOLOGO','Reutiliza cada clase en videos, carruseles, posts y newsletters.',ORANGE),('COPYBLOGO','Escribe hooks, landing, emails, CTA y guiones de venta.',BLUE),('COMUNIDADLOGO','Sostiene retos, accountability, victorias y Demo Day.',ORANGE),('REVISADOROLOGO','Controla calidad, enlaces, accesibilidad y coherencia final.',BLUE),
]
for i,r in enumerate(roles):
    col=i%4; row=i//4; role_card(c,48+col*186,378-row*92,170,78,*r)
c.showPage()

# 5 kernels
page_bg(c); footer(c,5)
label(c,48,520,'04 / CINCO NUCLEOS')
text(c,48,480,'La agencia minima que si puede lanzar.',28,TEXT,FONT_BOLD)
nuclei=[('01','VISION + ESTRATEGIA','Tu + Estrategologo','Que se construye y por que importa.'),('02','EXPERIENCIA EDUCATIVA','Curriculologo + Presentacionologo','Como aprende, practica y demuestra el alumno.'),('03','MARCA + PRODUCCION','Disenadologo + Imagenelogo + Videologo','Como se ve, se siente y se comunica.'),('04','OPERACION + AUTOMATIZACION','Administranologo + Automatizologo + Jarvisologo','Como entra, avanza y recibe seguimiento.'),('05','EVIDENCIA + MEJORA','Certificatologo + Verificatologo + Revisadorologo','Como se valida, documenta e itera la experiencia.')]
for i,(n,title,team,desc) in enumerate(nuclei):
    y=392-i*68
    rect(c,48,y,740,53,PANEL,LINE,16,.92)
    c.saveState(); c.setFillColor(ORANGE if i%2==0 else BLUE); c.setFillAlpha(.15); c.roundRect(63,y+11,37,31,10,fill=1,stroke=0); c.restoreState()
    text(c,81,y+21,n,11,ORANGE if i%2==0 else BLUE,FONT_BOLD)
    text(c,122,y+30,title,11,TEXT,FONT_BOLD); text(c,122,y+15,team,7.9,MUTED,FONT_BOLD)
    text(c,520,y+22,desc,8.5,BLUE if i%2 else ORANGE,FONT_BOLD)
c.showPage()

# 6 workflow
page_bg(c); footer(c,6)
label(c,48,520,'05 / EL FLUJO')
text(c,48,480,'De una idea a una evidencia.',28,TEXT,FONT_BOLD)
paragraph(c,48,451,'Cada pieza viaja por una cadena. La automatizacion acelera; la persona decide, revisa y responde por la calidad.',570,10.5,MUTED,15)
flow=[('BRIEF','problema real'),('ESTRATEGIA','oferta + ruta'),('DISENO','experiencia visible'),('PRODUCCION','clase + contenido'),('EVIDENCIA','proyecto + badge'),('ITERACION','mejor cohorte')]
for i,(a,b) in enumerate(flow):
    x=49+i*127; y=275
    rect(c,x,y,109,78,HexColor('#101720'),HexColor('#3B526B'),17,.94)
    text(c,x+16,y+47,a,8.3,ORANGE if i in [0,3] else BLUE,FONT_BOLD); text(c,x+16,y+27,b,8.2,TEXT,FONT_BOLD)
    if i<len(flow)-1:
        c.saveState(); c.setStrokeColor(ORANGE); c.setStrokeAlpha(.65); c.setLineWidth(1.1); c.line(x+109,y+39,x+123,y+39); c.restoreState()
        c.setFillColor(ORANGE); c.setFont(FONT_BOLD,9); c.drawString(x+116,y+36,'›')
rect(c,48,104,740,82,HexColor('#111820'),HexColor('#3D4E61'),17,.9)
label(c,67,156,'REGLA DE ORO',ORANGE)
paragraph(c,67,136,'No se entrega una constancia por presencia. Se desbloquea una credencial privada al demostrar asistencia, entregables, proyecto y la evidencia externa definida en la ruta del alumno.',650,10,TEXT,14,FONT_BOLD)
c.showPage()

# 7 actions
page_bg(c); footer(c,7)
label(c,48,520,'06 / ACTIVACION')
text(c,48,480,'El primer sprint del estudio.',28,TEXT,FONT_BOLD)
steps=[('DIA 01','Cerrar nombre, promesa y criterios de egreso.'),('SEMANA 01','Diseñar la identidad, landing y sistema de onboarding.'),('SEMANA 02','Producir sesion 1, workbook, dashboard y matriz de evidencia.'),('SEMANA 03','Grabar explainer, activar campaña, abrir lista de espera.'),('SEMANA 04','Probar cohorte piloto, medir friccion, corregir y publicar casos.')]
for i,(a,b) in enumerate(steps):
    x=48+(i%2)*376; y=370-(i//2)*105
    if i==4: x=236; y=113
    rect(c,x,y,342,79,PANEL,LINE,16,.95); pill(c,x+18,y+49,a,ORANGE if i%2==0 else BLUE); paragraph(c,x+18,y+31,b,288,9.4,TEXT,13,FONT_BOLD)
text(c,48,66,'LA META NO ES “TENER UN CURSO”.',13,MUTED,FONT_BOLD)
text(c,48,40,'LA META ES TENER UN SISTEMA QUE PRODUCE RESULTADOS QUE LA GENTE QUIERE MOSTRAR.',14,ORANGE,FONT_BOLD)
c.showPage()

# 8 closing
page_bg(c)
orb(c,676,312,105,ORANGE)
label(c,48,488,'CIERRE')
text(c,48,440,'Cada ologo es una',30,TEXT,FONT_BOLD)
text(c,48,400,'promesa de calidad.',30,ORANGE,FONT_BOLD)
paragraph(c,48,353,'No se trata de llenar un organigrama. Se trata de saber que funcion necesita una persona, un agente o un proceso para que el alumno llegue a una transformacion real.',450,11,MUTED,16)
rect(c,48,138,465,114,HexColor('#10151C'),HexColor('#45556B'),18,.9)
label(c,68,219,'EL JURAMENTO DEL ESTUDIO',BLUE)
paragraph(c,68,195,'Construir con ambicion. Explicar con claridad. Verificar con rigor. Disenar con respeto. Y no entregar nada que no ayude al alumno a avanzar.',405,11,TEXT,16,FONT_BOLD)
text(c,48,60,'ESTUDIO DE PRODUCCION EDUCATIVA IA',8,TEXT,FONT_BOLD)
text(c,48,43,'Documento fundacional - Cohorte 1 - Version 0.1',7,MUTED,FONT_REG)
c.showPage()

c.save()
print(OUT)
