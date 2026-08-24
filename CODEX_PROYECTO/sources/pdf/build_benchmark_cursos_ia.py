from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, Color
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.lib.utils import simpleSplit
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from pathlib import Path
import math

ROOT = Path('/Users/user/Documents/Codex/2026-07-19/new-chat')
OUT = ROOT / 'output/pdf/Benchmark_Competitivo_Cursos_IA_2026.pdf'

W, H = 1600, 900
BG = HexColor('#070B12'); PANEL = HexColor('#101927'); PANEL2 = HexColor('#142238')
LINE = HexColor('#28415D'); WHITE = HexColor('#F4F8FF'); MUTED = HexColor('#AFC1D4')
ORANGE = HexColor('#FF7642'); ICE = HexColor('#A8E2FF'); VIOLET = HexColor('#A786FF')
GREEN = HexColor('#8DF0B7'); RED = HexColor('#FF9E9E')

try:
    pdfmetrics.registerFont(TTFont('Inter', '/System/Library/Fonts/Supplemental/Arial.ttf'))
    pdfmetrics.registerFont(TTFont('InterBold', '/System/Library/Fonts/Supplemental/Arial Bold.ttf'))
except:
    pass
FONT = 'Inter'; BOLD = 'InterBold'

def rect(c,x,y,w,h,fill,stroke=None,r=22,alpha=None):
    c.saveState()
    if alpha is not None: c.setFillAlpha(alpha)
    c.setFillColor(fill)
    if stroke:
        c.setStrokeColor(stroke); c.setLineWidth(1)
    else: c.setStrokeColor(fill)
    c.roundRect(x,y,w,h,r,fill=1,stroke=1 if stroke else 0)
    c.restoreState()

def txt(c,s,x,y,size=24,color=WHITE,font=FONT,align='left'):
    c.setFillColor(color); c.setFont(font,size)
    if align=='center': x -= stringWidth(s,font,size)/2
    if align=='right': x -= stringWidth(s,font,size)
    c.drawString(x,y,s)

def wrap(c,s,x,y,width,size=22,color=WHITE,font=FONT,leading=None, max_lines=None):
    leading=leading or size*1.34
    lines=simpleSplit(s,font,size,width)
    if max_lines: lines=lines[:max_lines]
    c.setFillColor(color); c.setFont(font,size)
    for line in lines:
        c.drawString(x,y,line); y-=leading
    return y

def pill(c,label,x,y,color=ICE):
    tw=stringWidth(label,BOLD,13)+32
    rect(c,x,y,tw,30,Color(color.red,color.green,color.blue,alpha=.13),color,15)
    txt(c,label,x+16,y+9,13,color,BOLD)
    return tw

def header(c,kicker,title,sub=None,page=None):
    # Each report page is a dark desktop canvas; the glass cards sit above it.
    c.setFillColor(BG); c.rect(0,0,W,H,fill=1,stroke=0)
    # restrained technical grid gives the page depth without becoming a busy HUD
    c.saveState(); c.setStrokeColor(Color(0.35,0.58,0.9,alpha=.055)); c.setLineWidth(.7)
    for gx in range(0,W+1,80): c.line(gx,0,gx,H)
    for gy in range(0,H+1,80): c.line(0,gy,W,gy)
    c.restoreState()
    # top dark translucent glass strip
    rect(c,70,806,1460,42,Color(0.05,0.1,0.17,alpha=.86),LINE,18)
    txt(c,kicker.upper(),94,821,13,ORANGE,BOLD)
    txt(c,title,94,754,34,WHITE,BOLD)
    if sub: wrap(c,sub,94,718,1250,17,MUTED,FONT,23,max_lines=2)
    if page: txt(c,f'{page:02d}',1500,821,14,ICE,BOLD,'right')

def icon(c, kind, x,y, r=31, color=ICE):
    # clean custom icon disk - avoids unsupported emoji glyphs while preserving visual semantics
    c.saveState(); c.setFillColor(Color(color.red,color.green,color.blue,alpha=.16)); c.setStrokeColor(color); c.setLineWidth(1.4); c.circle(x,y,r,fill=1,stroke=1)
    c.setStrokeColor(WHITE); c.setLineWidth(3); c.setLineCap(1)
    if kind=='signal':
        for i,h in enumerate([11,18,27]): c.line(x-14+i*14,y-12,x-14+i*14,y-12+h)
    elif kind=='course':
        c.roundRect(x-16,y-11,32,22,4,fill=0,stroke=1); c.line(x,y-11,x,y+11)
    elif kind=='people':
        c.circle(x-8,y+7,5,fill=0,stroke=1); c.circle(x+10,y+7,5,fill=0,stroke=1); c.arc(x-18,y-15,x+1,y+4,0,180); c.arc(x+0,y-15,x+20,y+4,0,180)
    elif kind=='search':
        c.circle(x-5,y+5,11,fill=0,stroke=1); c.line(x+3,y-3,x+16,y-16)
    elif kind=='play':
        p=c.beginPath(); p.moveTo(x-7,y-13); p.lineTo(x-7,y+13); p.lineTo(x+15,y); p.close(); c.drawPath(p,fill=0,stroke=1)
    elif kind=='shield':
        p=c.beginPath(); p.moveTo(x,y+17); p.lineTo(x+15,y+10); p.lineTo(x+12,y-12); p.lineTo(x,y-20); p.lineTo(x-12,y-12); p.lineTo(x-15,y+10); p.close(); c.drawPath(p,fill=0,stroke=1)
    elif kind=='map':
        c.line(x-18,y-13,x-5,y+14); c.line(x-5,y+14,x+8,y-13); c.line(x+8,y-13,x+18,y+13); c.line(x-18,y-13,x+18,y+13)
    c.restoreState()

def chart_bars(c, x,y,w,h, vals, labels, colors):
    maxv=max(vals)
    for i,(v,l,col) in enumerate(zip(vals,labels,colors)):
        bw=(w-48)/len(vals); bx=x+24+i*bw
        bh=(h-70)*v/maxv
        rect(c,bx,y+42,bw-20,bh,col,None,12)
        txt(c,l,bx+(bw-20)/2,y+15,13,MUTED,BOLD,'center')
        txt(c,str(v)+'K',bx+(bw-20)/2,y+48+bh,15,WHITE,BOLD,'center')

def card(c,x,y,w,h,title,body,accent=ICE,kind='signal',small=False):
    rect(c,x,y,w,h,Color(PANEL.red,PANEL.green,PANEL.blue,alpha=.94),LINE,24)
    icon(c,kind,x+43,y+h-43,22,accent)
    txt(c,title,x+78,y+h-49,19 if not small else 16,WHITE,BOLD)
    wrap(c,body,x+28,y+h-91,w-56,16 if not small else 13,MUTED,FONT,21 if not small else 17,max_lines=4)

def footer(c,num):
    c.setStrokeColor(LINE); c.setLineWidth(1); c.line(70,50,1530,50)
    txt(c,'LABORATORIO IA - BENCHMARK PUBLICO',70,26,12,MUTED,BOLD)
    txt(c,'PUBLICACIONES VISIBLES | 20 AGO 2026',1530,26,12,MUTED,BOLD,'right')
    txt(c,str(num).zfill(2),800,26,12,ORANGE,BOLD,'center')

def cover(c):
    # atmospheric visual field
    c.setFillColor(BG); c.rect(0,0,W,H,fill=1,stroke=0)
    for i in range(12):
        cx=1180+math.cos(i*.7)*250; cy=460+math.sin(i*.7)*245
        c.setFillColor(Color(0.32,0.6,1,alpha=.018+i*.002)); c.circle(cx,cy,420-i*24,fill=1,stroke=0)
    # 3 glass orbs / network graphic
    for (x,y,r,col,label,n) in [(1100,570,138,VIOLET,'COMUNIDAD',425),(1300,420,106,ICE,'CONTENIDO',125),(1010,310,88,ORANGE,'OFERTA',5)]:
        c.setFillColor(Color(col.red,col.green,col.blue,alpha=.12)); c.circle(x,y,r,fill=1,stroke=0)
        c.setStrokeColor(col); c.setLineWidth(2); c.circle(x,y,r,fill=0,stroke=1)
        c.setStrokeColor(Color(WHITE.red,WHITE.green,WHITE.blue,alpha=.32)); c.circle(x,y,r-18,fill=0,stroke=1)
        txt(c,label,x,y+8,14,WHITE,BOLD,'center'); txt(c,str(n)+'K',x,y-25,26,col,BOLD,'center')
    c.setStrokeColor(Color(ICE.red,ICE.green,ICE.blue,alpha=.55)); c.setLineWidth(2); c.line(1070,470,1225,448); c.line(1065,405,1050,370)
    pill(c,'RESEARCH NOTEBOOK 01',92,750,ORANGE)
    txt(c,'¿QUIEN VENDE',92,640,55,WHITE,BOLD)
    txt(c,'APRENDIZAJE DE IA',92,577,55,ICE,BOLD)
    txt(c,'Y COMO CAPTA',92,514,55,WHITE,BOLD)
    txt(c,'ATENCION?',92,451,55,ORANGE,BOLD)
    wrap(c,'Benchmark competitivo de cinco creadores con comunidad, contenido educativo y oferta vinculada a IA. Muestra: hasta 25 publicaciones publicas recientes por cuenta.',92,365,720,23,MUTED,FONT,31)
    txt(c,'20 AGOSTO 2026 | MONTERREY, NUEVO LEON',92,150,15,ICE,BOLD)
    txt(c,'FUENTES PUBLICAS · NO SE EXTRAEN DATOS PERSONALES',92,116,14,MUTED,BOLD)

def methodology(c):
    header(c,'01 / COMO LEER ESTE ESTUDIO','Muestra publica. Nada de perseguir personas.','La unidad de analisis es la publicacion y el embudo visible, no el perfil individual de quien mira o comenta.',1)
    card(c,94,430,420,205,'125 piezas revisadas','25 publicaciones publicas recientes por cada una de las cinco cuentas. Se capturaron titulo, formato, duracion, vistas y edad visible.',ICE,'play')
    card(c,590,430,420,205,'Interes agregado','Se codificaron senales como: curso, guia, comunidad, plantilla, demo, pricing, certificacion o ingreso. No se recopilaron nombres ni handles.',GREEN,'people')
    card(c,1086,430,420,205,'Limite real','Hora exacta, ubicacion, segmentacion, presupuesto y configuracion de distribucion no son datos publicos de YouTube. Se reportan como no disponibles.',ORANGE,'shield')
    rect(c,94,155,1412,190,Color(PANEL2.red,PANEL2.green,PANEL2.blue,alpha=.76),LINE,28)
    icon(c,'search',145,248,34,VIOLET)
    txt(c,'Criterio de seleccion',205,269,25,WHITE,BOLD)
    wrap(c,'Canales con audiencia publica alta y una oferta de formacion/comunidad visible vinculada al creador. La comparacion de audiencia usa suscriptores de YouTube, no mezcla miembros de comunidad como si fueran seguidores.',205,232,1120,18,MUTED,FONT,25)
    footer(c,1)

def landscape(c):
    header(c,'02 / EL MAPA','Cinco ofertas. Cinco embudos.','Suscriptores son una fotografia publica aproximada de agosto de 2026; comunidad y precio se presentan solo si el creador los declara.',2)
    rows=[
        ('Nate Herk','945K','AI Automation Society','425K comunidad / 3.5K Plus','Automatizacion + negocio',ORANGE),
        ('Matt Wolfe','978K','Future Tools / AI for Creators','Newsletter 250K+','Noticias + herramientas',ICE),
        ('Liam Ottley','806K','AI Automation Agency Hub','193.1K miembros','Agencia + negocio IA',VIOLET),
        ('AI Jason','230K','AI Builder Club','Cursos propios','Builder / productos IA',GREEN),
        ('Cole Medin','221K','Dynamous AI Mastery','Cursos y comunidad','Agentes + coding',ORANGE),
    ]
    y=630
    for i,(name,aud,offer,proof,theme,col) in enumerate(rows):
        rect(c,94,y,1412,78,Color(PANEL.red,PANEL.green,PANEL.blue,alpha=.94),LINE,18)
        rect(c,112,y+15,48,48,Color(col.red,col.green,col.blue,alpha=.17),col,14)
        txt(c,str(i+1).zfill(2),136,y+31,16,col,BOLD,'center')
        txt(c,name,187,y+42,21,WHITE,BOLD); txt(c,aud+' YouTube',187,y+18,14,ICE,BOLD)
        txt(c,offer,500,y+41,18,WHITE,BOLD); txt(c,proof,500,y+18,14,MUTED,FONT)
        txt(c,theme,1165,y+30,16,col,BOLD,'center')
        y-=93
    rect(c,94,130,1412,92,Color(ORANGE.red,ORANGE.green,ORANGE.blue,alpha=.09),ORANGE,22)
    icon(c,'map',142,175,28,ORANGE)
    wrap(c,'Hallazgo: los gigantes combinan contenido gratuito de alta utilidad con una siguiente accion muy concreta: comunidad, plantilla, curso, newsletter o llamada. La leccion no es prometer dinero; es reducir el siguiente paso.',195,183,1230,18,WHITE,BOLD,25)
    footer(c,2)

def creator_page(c, num, name, audience, title, offer, observation, top, colors):
    header(c,f'03 / PERFIL {num:02d}',name,offer,num+2)
    rect(c,94,600,470,102,Color(PANEL2.red,PANEL2.green,PANEL2.blue,alpha=.92),LINE,24)
    txt(c,audience,126,648,39,colors[0],BOLD); txt(c,'audiencia YouTube publica',126,621,15,MUTED,FONT)
    pill(c,'EMBUDO VISIBLE',320,636,colors[1])
    card(c,592,500,432,202,'Lo que engancha',observation,colors[1],'signal')
    card(c,1050,500,456,202,'Pieza de mayor traccion',top,colors[0],'play')
    # three visual content atoms
    atoms=[('01','NOVEDAD','Actualizacion o nueva herramienta'),('02','RESULTADO','Caso, sistema o promesa concreta'),('03','PUENTE','Guia / comunidad / curso')]
    x=94
    for n,head,body in atoms:
        rect(c,x,260,430,155,Color(PANEL.red,PANEL.green,PANEL.blue,alpha=.96),LINE,24)
        txt(c,n,x+28,359,28,colors[0],BOLD); txt(c,head,x+84,366,17,WHITE,BOLD)
        wrap(c,body,x+84,336,300,14,MUTED,FONT,19,max_lines=2)
        x+=458
    rect(c,94,114,1412,100,Color(ICE.red,ICE.green,ICE.blue,alpha=.07),ICE,22)
    txt(c,'OPORTUNIDAD PARA EL LABORATORIO',122,176,14,ICE,BOLD)
    wrap(c,title,122,145,1280,19,WHITE,BOLD,25,max_lines=2)
    footer(c,num+2)

def post_patterns(c):
    header(c,'04 / 125 PUBLICACIONES','Que tipo de pieza concentra el alcance','No son datos de conversion. Son patrones publicos de vistas, empaques y duracion en las 25 publicaciones recientes de cada cuenta.',8)
    rect(c,94,390,760,310,Color(PANEL.red,PANEL.green,PANEL.blue,alpha=.96),LINE,28)
    txt(c,'Vistas altas visibles: ejemplos',126,655,21,WHITE,BOLD)
    chart_bars(c,120,430,710,190,[212,275,165,153,207],['Nate','Liam','Matt','Cole','Jason'],[ORANGE,VIOLET,ICE,GREEN,ORANGE])
    txt(c,'Ejemplos no equivalentes: publicacion / antiguedad distinta.',126,402,13,MUTED,FONT)
    right=[('Novedad con tesis','"esto cambia", "nuevo paradigma", "que necesitas saber"'),('Ruta guiada','guia completa, curso largo, paso a paso, sistema'),('Resultado concreto','primer agente, segundo cerebro, ahorrar tokens, vender flujo'),('Contrarian controlado','"lo estabas haciendo mal", "no te dejes llevar"')]
    y=650
    for h,b in right:
        rect(c,900,y-50,606,72,Color(PANEL2.red,PANEL2.green,PANEL2.blue,alpha=.9),LINE,18)
        txt(c,h,928,y-10,17,WHITE,BOLD); wrap(c,b,928,y-35,530,14,MUTED,FONT,18,max_lines=1); y-=88
    rect(c,94,160,1412,128,Color(ORANGE.red,ORANGE.green,ORANGE.blue,alpha=.10),ORANGE,24)
    icon(c,'signal',148,223,31,ORANGE)
    wrap(c,'Interpretacion: la audiencia reacciona a aprendizaje util empaquetado como cambio inmediato. El curso debe ser la consecuencia logica del contenido, no el unico tema de la cuenta.',210,235,1180,22,WHITE,BOLD,30,max_lines=2)
    footer(c,8)

def gap(c):
    header(c,'05 / HUECO DE MERCADO','Lo que ellos no estan resolviendo para tu alumno','La oportunidad no es competir por el hype en ingles. Es entregar claridad, contexto local y evidencia de avance.',9)
    cards=[
        ('IA PARA GENTE QUE NO VIENE DE SISTEMAS','Abogados, consultores, freelancers y emprendedores que quieren una ruta sin sentirse fuera de lugar.','course',ICE),
        ('CREDENCIAL + PORTAFOLIO, NO SOLO VIDEOS','Ruta personalizada desde el dia uno, pruebas de avance y certificados externos obtenidos por el alumno.','shield',ORANGE),
        ('IMPLEMENTACION LOCAL Y HUMANA','Google Meet en vivo, Monterrey como comunidad base, caso real del alumno y un asistente personal construido.','people',VIOLET),
    ]
    x=94
    for h,b,k,col in cards:
        rect(c,x,300,430,350,Color(PANEL.red,PANEL.green,PANEL.blue,alpha=.96),LINE,28)
        icon(c,k,x+56,584,30,col); wrap(c,h,x+36,520,358,22,WHITE,BOLD,29,max_lines=3); wrap(c,b,x+36,390,358,17,MUTED,FONT,24,max_lines=4); x+=458
    rect(c,94,130,1412,100,Color(GREEN.red,GREEN.green,GREEN.blue,alpha=.10),GREEN,24)
    txt(c,'POSICIONAMIENTO RECOMENDADO',124,187,14,GREEN,BOLD)
    wrap(c,'"No te vendo otra lista de prompts. Te acompano a construir una practica de IA, un asistente personal y evidencia que puedes mostrar."',124,153,1220,22,WHITE,BOLD,30,max_lines=2)
    footer(c,9)

def action(c):
    header(c,'06 / TRADUCCION A ACCION','Un embudo limpio para el Laboratorio','Un contenido no pide "compra mi curso". Entrega una micro-victoria y abre el siguiente paso correcto.',10)
    steps=[('01','DESCUBRE','Reel / Short: noticia o problema',ICE),('02','ENTIENDE','Carrusel: mapa o checklist',VIOLET),('03','PRUEBA','Guia gratis: diagnostico de ruta',ORANGE),('04','DECIDE','Landing: laboratorio de 5 sesiones',GREEN),('05','DEMUESTRA','Demo Day + portafolio',ICE)]
    x=92
    for n,a,b,col in steps:
        rect(c,x,455,260,178,Color(PANEL.red,PANEL.green,PANEL.blue,alpha=.96),LINE,24)
        txt(c,n,x+28,584,24,col,BOLD); txt(c,a,x+28,548,18,WHITE,BOLD); wrap(c,b,x+28,512,205,15,MUTED,FONT,20,max_lines=2)
        if x<1200:
            c.setStrokeColor(col); c.setLineWidth(2); c.line(x+260,544,x+286,544)
        x+=288
    rect(c,94,197,1412,164,Color(PANEL2.red,PANEL2.green,PANEL2.blue,alpha=.92),LINE,28)
    txt(c,'PRIMERA SERIE DE CONTENIDO',126,319,15,ORANGE,BOLD)
    series=[('A','"Tu suscripcion de IA ya puede ser tu asistente"'),('B','"Certificaciones reales: donde sacar evidencia sin inventarte un titulo"'),('C','"Un abogado / consultor puede usar IA sin convertirse en programador"')]
    y=282
    for n,s in series:
        txt(c,n,128,y,16,ICE,BOLD); txt(c,s,165,y,18,WHITE,BOLD); y-=34
    footer(c,10)

def sources(c):
    header(c,'07 / FUENTES Y LIMITES','Fuentes que si sostienen el analisis','Las cifras cambian. Las URLs y la fecha de consulta permiten repetir o actualizar el benchmark.',11)
    items=[
    ('Nate Herk','https://www.nateherk.com/ | https://www.youtube.com/@nateherk/videos | consultado 20 ago 2026'),
    ('Liam Ottley','https://www.youtube.com/@LiamOttley/videos | https://www.skool.com/ai-automation-agency-hub-8466 | consultado 20 ago 2026'),
    ('Matt Wolfe','https://mattwolfe.com/ | https://www.youtube.com/@mreflow/videos | consultado 20 ago 2026'),
    ('Cole Medin','https://dynamous.ai/ | https://www.youtube.com/@colemedin/videos | consultado 20 ago 2026'),
    ('AI Jason','https://www.aibuilderclub.com/about | https://www.youtube.com/@AIJasonZ/videos | consultado 20 ago 2026'),
    ('Conteos auxiliares','SocialCounts / vidIQ usados solo como fotografia secundaria; preferencia por la pagina oficial del creador.'),
    ]
    y=660
    for i,(a,b) in enumerate(items):
        rect(c,94,y-28,1412,70,Color(PANEL.red,PANEL.green,PANEL.blue,alpha=.9),LINE,16)
        txt(c,str(i+1).zfill(2),124,y,14,ORANGE,BOLD); txt(c,a,170,y+5,18,WHITE,BOLD); wrap(c,b,430,y+5,1000,14,MUTED,FONT,18,max_lines=2); y-=87
    rect(c,94,100,1412,94,Color(ORANGE.red,ORANGE.green,ORANGE.blue,alpha=.1),ORANGE,22)
    wrap(c,'Nota metodologica: no se obtuvo ni se entrega una lista de seguidores, comentaristas, ubicaciones, horarios exactos o configuracion interna. Esos datos no son publicos de forma confiable y no hacen falta para el analisis competitivo.',124,152,1260,17,WHITE,BOLD,23,max_lines=3)
    footer(c,11)

def make():
    OUT.parent.mkdir(parents=True,exist_ok=True)
    c=canvas.Canvas(str(OUT), pagesize=(W,H), pageCompression=1)
    c.setTitle('Benchmark competitivo: cursos de IA 2026')
    cover(c); c.showPage()
    methodology(c); c.showPage()
    landscape(c); c.showPage()
    creator_page(c,1,'Nate Herk','945K','Tomar la estructura de una guia amplia, pero prometer una practica verificable: un asistente, un caso y una demostracion.','AI Automation Society: comunidad gratuita + Society Plus con curriculum, plantillas y soporte.', 'Alterna tutoriales de 8-30 min con cursos largos y titulos que vinculan automatizacion con ingresos, ahorro o ventaja competitiva.','"GPT 5.6 Soul hizo todo este video" - 103K vistas visibles en la muestra reciente.',[ORANGE,ICE]); c.showPage()
    creator_page(c,2,'Matt Wolfe','978K','Tu version no debe ser "noticias por noticias". Convierte las novedades en una decision practica para el negocio o carrera del alumno.','Future Tools, newsletter y contenido educativo; el canal exhibe pestaña de Cursos.', 'Ritmo editorial semanal: titulares de noticia, seleccion de herramientas y guias con listas grandes. La recurrencia crea habito.', '"Base de conocimientos de segundo cerebro con IA" - 165K vistas visibles en la muestra.',[ICE,VIOLET]); c.showPage()
    creator_page(c,3,'Liam Ottley','806K','Donde ellos venden agencia, tu puedes abrir la puerta al profesional que quiere aplicar IA en su trabajo sin adoptar una identidad de "gurú".','AI Automation Agency Hub: curso, Q&A y recursos; 193.1K miembros visibles en Skool.', 'Los mejores empaques cruzan IA + ingreso + autonomia. Los cursos largos dan profundidad; el contenido corto mantiene el ritmo.', '"Build & Sell AI Agents" - 275K vistas visibles en la muestra.',[VIOLET,ORANGE]); c.showPage()
    creator_page(c,4,'Cole Medin','221K','Baja la complejidad de agentes y coding a un proyecto significativo: memoria, asistente o flujo de trabajo del alumno.','Dynamous AI Mastery: cursos y comunidad con Second Brain, Agentic Coding y AI Agents.', 'La autoridad viene de explicar sistemas concretos y mostrar limites. El enfoque tecnico necesita una rampa de entrada humana.', '"Google lanzó una masterclass sobre ingenieria agentica" - 153K vistas visibles en la muestra.',[GREEN,ICE]); c.showPage()
    creator_page(c,5,'AI Jason','230K','Responde a la ansiedad con una experiencia visual: "configura tu entorno y prueba una habilidad esta semana".','AI Builder Club: guias y cursos propios; el sitio declara ofertas gratuitas y de pago.', 'Títulos de prueba/error, setup y diseno de producto. Es tecnica, pero el gancho siempre es una mejora tangible en el flujo de trabajo.', '"Tool calling" - 207K vistas visibles en la muestra.',[ORANGE,GREEN]); c.showPage()
    post_patterns(c); c.showPage()
    gap(c); c.showPage()
    action(c); c.showPage()
    sources(c); c.showPage()
    c.save()

if __name__=='__main__': make()
