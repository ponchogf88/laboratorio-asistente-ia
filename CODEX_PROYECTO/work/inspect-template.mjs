import { FileBlob, SpreadsheetFile } from '/Users/user/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/@oai/artifact-tool/dist/artifact_tool.mjs';
const p='/Users/user/.codex/plugins/cache/openai-curated-remote/openai-templates/0.1.0/skills/artifact-template-analytics-dashboard/assets/reference.xlsx';
const wb=await SpreadsheetFile.importXlsx(await FileBlob.load(p));
console.log((await wb.inspect({kind:'workbook,sheet,table,drawing',maxChars:12000,tableMaxRows:8,tableMaxCols:8})).ndjson);
