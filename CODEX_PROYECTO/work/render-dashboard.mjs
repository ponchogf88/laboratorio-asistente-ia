import fs from 'node:fs/promises';
import { FileBlob, SpreadsheetFile } from '/Users/user/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/@oai/artifact-tool/dist/artifact_tool.mjs';
const wb=await SpreadsheetFile.importXlsx(await FileBlob.load('outputs/investigacion-demanda-productos-contenido-social.xlsx'));
const b=await wb.render({sheetName:'Dashboard',autoCrop:'all',scale:1,format:'png'});
await fs.writeFile('outputs/preview-dashboard.png',new Uint8Array(await b.arrayBuffer()));
console.log((await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A',options:{useRegex:true,maxResults:100},maxChars:5000})).ndjson);
