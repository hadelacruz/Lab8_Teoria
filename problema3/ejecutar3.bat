@echo off
echo ============================================================
echo EJECUTANDO PROBLEMA 3 - Analisis de Complejidad O(n^2)
echo ============================================================
echo.

echo [1/3] Compilando problema3.cpp...
g++ -O3 -o problema3.exe problema3.cpp
if errorlevel 1 (
    echo.
    echo ERROR: Fallo la compilacion
    pause
    exit /b 1
)
echo OK: Compilacion exitosa
echo.

echo [2/3] Ejecutando profiling...
problema3.exe
if errorlevel 1 (
    echo.
    echo ERROR: Fallo la ejecucion
    pause
    exit /b 1
)
echo.

echo [3/3] Generando graficas...
python generar_grafica3.py
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
echo   - resultados3.csv
echo   - grafica3.png
echo ============================================================
pause
