@echo off
echo ============================================================
echo EJECUTANDO PROBLEMA 2 - Analisis de Complejidad O(n)
echo ============================================================
echo.

echo [1/3] Compilando problema2.cpp...
g++ -O3 -o problema2.exe problema2.cpp
if errorlevel 1 (
    echo.
    echo ERROR: Fallo la compilacion
    pause
    exit /b 1
)
echo OK: Compilacion exitosa
echo.

echo [2/3] Ejecutando profiling...
problema2.exe
if errorlevel 1 (
    echo.
    echo ERROR: Fallo la ejecucion
    pause
    exit /b 1
)
echo.

echo [3/3] Generando graficas...
python generar_grafica2.py
if errorlevel 1 (
    echo.
    echo ERROR: Fallo la generacion de graficas
    pause
    exit /b 1
)

echo.
echo ============================================================
echo PROCESO COMPLETADO
echo ============================================================
echo Archivos generados:
echo   - resultados2.csv
echo   - grafica2.png
echo ============================================================
pause
