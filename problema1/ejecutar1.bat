@echo off
echo ============================================================
echo EJECUTANDO PROBLEMA 1 - Analisis de Complejidad O(n^2 log n)
echo ============================================================
echo.

echo [1/3] Compilando problema1.cpp...
g++ -O3 -o problema1.exe problema1.cpp
if errorlevel 1 (
    echo.
    echo ERROR: Fallo la compilacion
    pause
    exit /b 1
)
echo OK: Compilacion exitosa
echo.

echo [2/3] Ejecutando profiling...
problema1.exe
if errorlevel 1 (
    echo.
    echo ERROR: Fallo la ejecucion
    pause
    exit /b 1
)
echo.

echo [3/3] Generando graficas...
python generar_grafica1.py
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
echo   - resultados1.csv
echo   - grafica1.png
echo ============================================================
pause
