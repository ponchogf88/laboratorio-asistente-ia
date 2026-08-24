import { FileBlob, SpreadsheetFile } from '/Users/user/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/@oai/artifact-tool/dist/artifact_tool.mjs';
const wb=await SpreadsheetFile.importXlsx(await FileBlob.load('/Users/user/.codex/plugins/cache/openai-curated-remote/openai-templates/0.1.0/skills/artifact-template-analytics-dashboard/assets/reference.xlsx'));
console.log(wb.help('chart',{include:'index,examples,notes',maxChars:9000}).ndjson);
