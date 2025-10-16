# Lab 8 - Análisis de Complejidad Computacional

Laboratorio de Teoría de Computación que implementa y analiza la complejidad temporal de diferentes algoritmos mediante profiling en C++ y visualización con Python.

---

[![Ver video en YouTube](https://img.youtube.com/vi/mAVceSycYTs/0.jpg)](https://youtu.be/mAVceSycYTs)


## 📁 Estructura del Proyecto

```
Lab8_Teoria/
│
├── problema1/               # Problema 1 - O(n² log n)
│   ├── problema1.cpp        # Código fuente
│   ├── generar_grafica1.py  # Script de visualización
│   ├── ejecutar1.bat        # Script de ejecución automática
│   ├── resultados1.csv      # Datos generados (git-ignored)
│   ├── grafica1.png         # Gráfica generada (git-ignored)
│   └── problema1.exe        # Ejecutable (git-ignored)
│
├── problema2/               # Problema 2 - O(n)
│   ├── problema2.cpp        # Código fuente
│   ├── generar_grafica2.py  # Script de visualización
│   ├── ejecutar2.bat        # Script de ejecución automática
│   ├── resultados2.csv      # Datos generados (git-ignored)
│   ├── grafica2.png         # Gráfica generada (git-ignored)
│   └── problema2.exe        # Ejecutable (git-ignored)
│
├── problema3/               # Problema 3 - O(n²)
│   ├── problema3.cpp        # Código fuente
│   ├── generar_grafica3.py  # Script de visualización
│   ├── ejecutar3.bat        # Script de ejecución automática
│   ├── resultados3.csv      # Datos generados (git-ignored)
│   ├── grafica3.png         # Gráfica generada (git-ignored)
│   └── problema3.exe        # Ejecutable (git-ignored)
│
├── .gitignore
└── README.md
```

---

## 🚀 Ejecución Rápida

### Problema 1
```powershell
cd problema1
.\ejecutar1.bat
```

### Problema 2
```powershell
cd problema2
.\ejecutar2.bat
```

### Problema 3
```powershell
cd problema3
.\ejecutar3.bat
```

**¡Solo un comando por problema!** Cada script `.bat` automáticamente:
1. ✅ Compila el código C++
2. ✅ Ejecuta el profiling
3. ✅ Genera las gráficas

---

## 📊 Problema 1 - Complejidad O(n² log n)

### Código Analizado
```c
void function(int n) {
    int i, j, k, counter = 0;
    for (i = n/2; i <= n; i++) {           // O(n)
        for (j = 1; j+n/2 <= n; j++) {     // O(n)
            for (k = 1; k <= n; k = k*2) { // O(log n)
                counter++;
            }
        }
    }
}
```

### Análisis de Complejidad
- **Bucle externo (i)**: n/2 iteraciones → O(n)
- **Bucle medio (j)**: n/2 iteraciones → O(n)
- **Bucle interno (k)**: log₂(n) iteraciones → O(log n)
- **Complejidad total**: O(n) × O(n) × O(log n) = **O(n² log n)**

### Valores de n probados
`1, 10, 100, 1,000, 10,000, 100,000, 1,000,000`


## 📊 Problema 2 - Complejidad O(n)

### Código Analizado
```c
void function(int n) {
    if (n <= 1) return;
    int i, j;
    for (i = 1; i <= n; i++) {      // O(n)
        for (j = 1; j <= n; j++) {  
            printf("Sequence\n");
            break;                   // ← Ejecuta solo 1 vez!
        }
    }
}
```

### Análisis de Complejidad
- **Bucle externo (i)**: n iteraciones → O(n)
- **Bucle interno (j)**: 1 iteración (por el `break`) → O(1)
- **Complejidad total**: O(n) × O(1) = **O(n)**

### ¿Por qué no es O(n²)?
El `break` hace que el bucle interno **siempre ejecute exactamente 1 iteración**, sin importar el valor de n. Por eso la complejidad es lineal.

### Valores de n probados
`1, 10, 100, 1,000, 10,000, 100,000, 1,000,000`


## 📊 Problema 3 - Complejidad O(n²)

### Código Analizado
```c
void function(int n) {
    int i, j;
    for (i = 1; i <= n/3; i++) {      // O(n/3) = O(n)
        for (j = 1; j <= n; j += 4) {  // O(n/4) = O(n)
            printf("Sequence\n");
        }
    }
}
```

### Análisis de Complejidad
- **Bucle externo (i)**: n/3 iteraciones → O(n)
- **Bucle interno (j)**: n/4 iteraciones (incremento de 4) → O(n)
- **Complejidad total**: O(n) × O(n) = **O(n²)**

### Valores de n probados
`1, 10, 100, 1,000, 10,000, 100,000, 1,000,000`

---

## 🛠️ Tecnologías

- **C++ (g++)**: Implementación y profiling con alta eficiencia
- **Python 3**: Generación de gráficas con matplotlib y pandas
- **Batch Scripts**: Automatización de compilación y ejecución

---

## 📝 Archivos Generados

Cada problema genera:
- `resultados{N}.csv` - Tabla con n, tiempo y operaciones
- `grafica{N}.png` - Visualización en escala lineal y logarítmica

---

## 🔧 Requisitos

- **g++** (MinGW o similar)
- **Python 3** con pandas y matplotlib
- **Windows** (para scripts .bat)

### Instalación de librerías Python
```powershell
pip install pandas matplotlib
```

**Nota para PowerShell**: Recuerda usar `.\` antes de los archivos `.bat`
```powershell
.\ejecutar1.bat  # Correcto
ejecutar1.bat    # Error en PowerShell
```

---

## 📖 Documentación Adicional

- Ver código fuente en cada carpeta `problema1/` y `problema2/`
- Las gráficas incluyen escala lineal y logarítmica
- Los scripts `.bat` manejan errores automáticamente

---

**Universidad** | Teoría de Computación | Lab 8  
**Autor**: [Tu nombre]  
**Fecha**: Octubre 2025
