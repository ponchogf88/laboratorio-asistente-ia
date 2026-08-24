@echo off
echo ========================================
echo  ACADEMIA AAA - Subir a GitHub
echo ========================================
echo.

cd /d "%~dp0"

echo [1/4] Verificando estado del repo...
git status
echo.

echo [2/4] Agregando todos los archivos...
git add .
echo.

set /p COMMIT_MSG="Escribe el mensaje del commit (Enter para mensaje por defecto): "
if "%COMMIT_MSG%"=="" set COMMIT_MSG=update: mejoras al proyecto Academia AAA

echo [3/4] Haciendo commit: "%COMMIT_MSG%"
git commit -m "%COMMIT_MSG%"
echo.

echo [4/4] Subiendo a GitHub (rama main)...
git push origin main
echo.

if %ERRORLEVEL%==0 (
    echo ========================================
    echo  LISTO. Cambios publicados en GitHub.
    echo  https://github.com/ponchogf88/laboratorio-asistente-ia
    echo ========================================
) else (
    echo ========================================
    echo  ERROR al hacer push. Intenta:
    echo  1. git pull origin main --rebase
    echo  2. Vuelve a ejecutar este script
    echo ========================================
)

pause
