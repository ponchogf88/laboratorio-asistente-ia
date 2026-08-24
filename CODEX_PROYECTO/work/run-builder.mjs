process.on('uncaughtException',e=>{console.error('UNCAUGHT',e?.name,e?.message);process.exit(1)});
process.on('unhandledRejection',e=>{console.error('UNHANDLED',e?.name,e?.message);process.exit(1)});
import('./build-dashboard.mjs').catch(e=>{console.error('IMPORT_FAIL',e?.name,e?.message);process.exit(1)});
