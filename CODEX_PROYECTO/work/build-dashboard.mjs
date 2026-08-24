import fs from 'node:fs/promises';
import { FileBlob, SpreadsheetFile } from '/Users/user/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/@oai/artifact-tool/dist/artifact_tool.mjs';
const template='/Users/user/.codex/plugins/cache/openai-curated-remote/openai-templates/0.1.0/skills/artifact-template-analytics-dashboard/assets/reference.xlsx';
const outDir='/Users/user/Documents/Codex/2026-07-19/new-chat/outputs';
const data=JSON.parse(await fs.readFile('work/research/market-data.json','utf8'));
const wb=await SpreadsheetFile.importXlsx(await FileBlob.load(template));
const d=wb.worksheets.getItem('Dashboard');
const input=wb.worksheets.getItem('Data & Targets');
const helper=wb.worksheets.getItem('_Chart Helpers');
const raw=wb.worksheets.add('Listings observados');
const needs=wb.worksheets.add('Necesidades');
for (const s of [d,input,helper,raw,needs]) s.showGridLines=false;
d.deleteAllDrawings(); input.deleteAllDrawings(); helper.deleteAllDrawings();
// Raw listings, with source URLs and bounded evidence.
const headers=['Familia','Marketplace','Precio USD','Reseñas visibles','Rating','Producto','URL'];
const rows=data.listings.map(x=>[x.family,x.market,x.price,x.reviews,x.rating,x.product,x.url]);
raw.getRangeByIndexes(0,0,1,headers.length).values=[headers];
raw.getRangeByIndexes(1,0,rows.length,headers.length).values=rows;
raw.getRange('A1:G1').format={fill:'#13293D',font:{bold:true,color:'#FFFFFF'},rowHeight:28};
raw.getRange(`A2:G${rows.length+1}`).format={font:{color:'#14212B'},borders:{preset:'inside',style:'thin',color:'#D8E1E8'}};
raw.getRange(`C2:C${rows.length+1}`).setNumberFormat('$0.00');
raw.getRange(`D2:D${rows.length+1}`).setNumberFormat('0');
raw.getRange(`E2:E${rows.length+1}`).setNumberFormat('0.0');
raw.getRange('A:G').format.wrapText=true;
raw.getRange('A:A').format.columnWidth=24; raw.getRange('B:B').format.columnWidth=14; raw.getRange('C:E').format.columnWidth=14; raw.getRange('F:F').format.columnWidth=30; raw.getRange('G:G').format.columnWidth=48;
raw.freezePanes.freezeRows(1);
raw.tables.add(`A1:G${rows.length+1}`,true,'Listings');
// Needs table.
const nh=['Necesidad concreta','Fuerza (1-5)','Qué evidencia indica','Respuesta de producto'];
const nr=data.needs.map(x=>[x.need,x.strength,x.evidence,x.solution]);
needs.getRange('A1:D1').values=[nh]; needs.getRangeByIndexes(1,0,nr.length,4).values=nr;
needs.getRange('A1:D1').format={fill:'#13293D',font:{bold:true,color:'#FFFFFF'},rowHeight:28};
needs.getRange(`A2:D${nr.length+1}`).format={wrapText:true,borders:{preset:'inside',style:'thin',color:'#D8E1E8'}};
needs.getRange('A:A').format.columnWidth=28; needs.getRange('B:B').format.columnWidth=13; needs.getRange('C:D').format.columnWidth=48;
needs.freezePanes.freezeRows(1); needs.tables.add(`A1:D${nr.length+1}`,true,'Needs');
needs.getRange(`B2:B${nr.length+1}`).conditionalFormats.add('colorScale',{colors:['#FEE2E2','#FEF3C7','#DCFCE7']});
// Summary sheet reusing template styling and structure.
input.getRange('B2:P35').clear({applyTo:'contents'});
input.getRange('B2:P2').merge(); input.getRange('B2').values=[['Investigación de demanda — productos de contenido social']];
input.getRange('B3:P3').merge(); input.getRange('B3').values=[['Resumen de muestra y KPIs de lanzamiento']];
input.getRange('B5:P5').merge(); input.getRange('B5').values=[['CÓMO LEERLO']];
input.getRange('B6:P6').merge(); input.getRange('B6').values=[[`Muestra intencional de ${rows.length} listings visibles al ${data.as_of}; precios promocionales pueden cambiar. No representa todo el mercado.`]];
input.getRange('B8:C8').values=[['Fecha de corte',new Date('2026-07-19')]]; input.getRange('C8').setNumberFormat('yyyy-mm-dd');
input.getRange('B10:P10').merge(); input.getRange('B10').values=[['PRECIOS OBSERVADOS POR FAMILIA — FÓRMULAS SOBRE LA PESTAÑA LISTINGS']];
const families=[...new Set(data.listings.map(x=>x.family))];
input.getRange('B12:F12').values=[['Familia','N','Precio medio','Mínimo','Máximo']];
families.forEach((f,i)=>{const r=13+i; input.getRange(`B${r}`).values=[[f]]; input.getRange(`C${r}`).formulas=[[`=COUNTIF('Listings observados'!$A$2:$A$${rows.length+1},B${r})`]]; input.getRange(`D${r}`).formulas=[[`=AVERAGEIF('Listings observados'!$A$2:$A$${rows.length+1},B${r},'Listings observados'!$C$2:$C$${rows.length+1})`]]; input.getRange(`E${r}`).formulas=[[`=MINIFS('Listings observados'!$C$2:$C$${rows.length+1},'Listings observados'!$A$2:$A$${rows.length+1},B${r})`]]; input.getRange(`F${r}`).formulas=[[`=MAXIFS('Listings observados'!$C$2:$C$${rows.length+1},'Listings observados'!$A$2:$A$${rows.length+1},B${r})`]];});
input.getRange(`D13:F${12+families.length}`).setNumberFormat('$0.00');
input.getRange('H12:L12').values=[['KPI','Definición','Meta inicial*','Guardrail','Cadencia']];
const kpis=[
['Conversión pagada','Compras / visitas calificadas','2–5%','No descontar por debajo del rango probado','Semanal'],
['Activación <24h','Compradores que producen su primer output / compradores','60–75%','Soporte por confusión <2/10 compradores','Semanal'],
['Reuso semanas 2–4','Compradores que vuelven a usar / compradores','35–50%','Problemas de acceso <5%','Mensual']];
input.getRange('H13:L15').values=kpis;
input.getRange('H17:L17').merge(); input.getRange('H17').values=[['* Metas provisionales: deben recalibrarse tras 100 visitas calificadas o 20 ventas, lo que ocurra después.']];
input.getRange('B22:P22').merge(); input.getRange('B22').values=[['RECOMENDACIÓN DE PORTAFOLIO']];
const recs=[
['1','Sistema “1 idea → 10 piezas”','$19–29','Mayor dolor + ahorro de tiempo; incluir ejemplo completo y adaptación por canal.'],
['2','Kit “Primeras 10 publicaciones” por nicho','$15–25','Reduce la decisión y la curva de aprendizaje sin calendario rígido.'],
['3','Auditoría guiada + plan de 7 días','$19–29','Compra profesional: ahorra tiempo y convierte diagnóstico en acciones.'],
['4','Biblioteca de hooks nichada','$7–12','Mercado probado pero comoditizado; mejor como entrada u order bump.'],
['5','Calendario genérico','$5–10','Alta competencia y alternativas gratis; lanzar solo con flujo flexible y revisión semanal.']];
input.getRange('B24:E24').values=[['Prioridad','Producto','Precio sugerido','Por qué']]; input.getRange('B25:E29').values=recs;
input.getRange('B12:F12').format={fill:'#13293D',font:{bold:true,color:'#FFFFFF'}};
input.getRange('H12:L12').format={fill:'#13293D',font:{bold:true,color:'#FFFFFF'}};
input.getRange('B24:E24').format={fill:'#13293D',font:{bold:true,color:'#FFFFFF'}};
input.getRange('B2:P35').format.wrapText=true; input.getRange('B:B').format.columnWidth=24; input.getRange('C:F').format.columnWidth=15; input.getRange('H:H').format.columnWidth=22; input.getRange('I:I').format.columnWidth=44; input.getRange('J:L').format.columnWidth=20;
// Dashboard first viewport.
d.getRange('B2:Q52').clear({applyTo:'contents'});
d.getRange('B2:Q2').merge(); d.getRange('B2').values=[['Demanda real: productos digitales de contenido social']];
d.getRange('B3:Q3').merge(); d.getRange('B3').values=[['Qué duele, cuánto pagan y qué conviene construir primero']];
d.getRange('B4:Q4').merge(); d.getRange('B4').values=[[`Corte ${data.as_of} · muestra observada de ${rows.length} listings · precios en USD (una conversión aproximada)`]];
const totalReviews=data.listings.reduce((a,x)=>a+(x.reviews||0),0);
const cardLabels=['LISTINGS OBSERVADOS','RESEÑAS VISIBLES','FAMILIAS','DOLOR #1'];
const cardVals=[rows.length,totalReviews,families.length,'Decidir qué publicar'];
[['B5:E5','B6:E8'],['F5:I5','F6:I8'],['J5:M5','J6:M8'],['N5:Q5','N6:Q8']].forEach((p,i)=>{d.getRange(p[0]).merge();d.getRange(p[0].split(':')[0]).values=[[cardLabels[i]]];d.getRange(p[1]).merge();d.getRange(p[1].split(':')[0]).values=[[cardVals[i]]];d.getRange(p[0]).format={fill:'#13293D',font:{bold:true,color:'#9ED8F6'}};d.getRange(p[1]).format={fill:'#19354C',font:{bold:true,color:'#FFFFFF',size:18}};});
d.getRange('B6').setNumberFormat('0'); d.getRange('F6').setNumberFormat('0'); d.getRange('J6').setNumberFormat('0'); d.getRange('N6').setNumberFormat('@');
d.getRange('B11:I11').merge(); d.getRange('B11').values=[['Precio medio observado por familia (USD)']];
d.getRange('J11:Q11').merge(); d.getRange('J11').values=[['Fuerza de necesidades detectadas (1–5)']];
const means=families.map(f=>{const xs=data.listings.filter(x=>x.family===f).map(x=>x.price);return xs.reduce((a,b)=>a+b,0)/xs.length});
d.charts.add('bar',{title:'Precio medio por familia (USD)',categories:families,series:[{name:'USD',values:means}],hasLegend:false,from:{row:12,col:1},extent:{widthPx:610,heightPx:260}});
d.charts.add('bar',{title:'Problemas que más se repiten',categories:data.needs.map(x=>x.need),series:[{name:'Fuerza',values:data.needs.map(x=>x.strength)}],hasLegend:false,from:{row:12,col:9},extent:{widthPx:610,heightPx:260}});
d.getRange('B31:Q31').merge(); d.getRange('B31').values=[['DECISIÓN RECOMENDADA']];
d.getRange('B33:Q36').merge(); d.getRange('B33').values=[['Construir primero un sistema guiado “1 idea → 10 piezas” por $19–29. El comprador paga por reducir decisiones, ahorrar tiempo y obtener un primer resultado rápido; no por acumular más plantillas.']];
d.getRange('B38:F38').values=[['Prioridad','Producto','Precio','Señal de demanda','Riesgo']];
d.getRange('B39:F43').values=[
['1','1 idea → 10 piezas','$19–29','Dolor fuerte + oferta aún dispersa','Promesas AI sin prueba'],
['2','Primeras 10 publicaciones nichadas','$15–25','Principiante quiere empezar rápido','Elegir nicho incorrecto'],
['3','Auditoría + plan 7 días','$19–29','Ahorro profesional','Requiere ejemplos sólidos'],
['4','Hooks nichados','$7–12','Muchas ventas/reseñas visibles','Comoditizado'],
['5','Calendario genérico','$5–10','Compra existente','Gratis y saturado']];
d.getRange('B38:F38').format={fill:'#13293D',font:{bold:true,color:'#FFFFFF'}};
d.getRange('B45:Q45').merge(); d.getRange('B45').values=[['NOTA METODOLÓGICA']];
d.getRange('B46:Q49').merge(); d.getRange('B46').values=[['Los precios son observaciones puntuales, algunos promocionales. Las reseñas son señal de compra, no volumen total de ventas. Reddit aporta lenguaje y fricción, pero sufre autoselección. Tratar las metas de KPI como hipótesis hasta tener datos propios.']];
d.getRange('B2:Q52').format.wrapText=true;
await fs.mkdir(outDir,{recursive:true});
try {
  const out=await SpreadsheetFile.exportXlsx(wb); await out.save(`${outDir}/investigacion-demanda-productos-contenido-social.xlsx`);
  console.log((await wb.inspect({kind:'sheet,formula,drawing',sheetId:'Dashboard',range:'A1:Q52',maxChars:9000,options:{maxResults:100}})).ndjson);
} catch (e) { console.error('EXPORT_ERROR', e?.message, String(e?.stack||'').slice(-1800)); process.exit(2); }
