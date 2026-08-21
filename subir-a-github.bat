@echo off
title 🧬 Sincronizador de Laboratorio Asistente IA a GitHub
color 0b
echo ====================================================================
echo             🧬 ACADEMIA AAA - ASISTENTE DE IA AUTOMÁTICO 🧬
echo ====================================================================
echo.
echo  Iniciando proceso de subida del curso de IA a tu repositorio...
echo  Repositorio: https://github.com/ponchogf88/laboratorio-asistente-ia
echo.
echo ====================================================================
echo.

cd /d "C:\Users\USUARIO\laboratorio-asistente-ia"

echo [1/2] Verificando estado de Git...
git status
echo.

echo [2/2] Ejecutando push a GitHub...
echo (Si aparece una ventana emergente en tu pantalla o navegador,
echo por favor inicia sesion/autoriza para completar la subida de archivos).
echo.

git push -f -u origin main

echo.
echo ====================================================================
echo  ¡Sincronizacion completada!
echo ====================================================================
echo.
pause
