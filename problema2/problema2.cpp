#include <iostream>
#include <chrono>
#include <iomanip>
#include <fstream>
#include <vector>

using namespace std;
using namespace chrono;

void function(int n) {
    if (n <= 1) return;
    
    int i, j;
    
    for (i = 1; i <= n; i++) {
        for (j = 1; j <= n; j++) {
            printf("Sequence\n");
            break;
        }
    }
}

void profileFunction(vector<int> n_values) {
    cout << "============================================================" << endl;
    cout << "ANÁLISIS DE COMPLEJIDAD - PROBLEMA 2 (C++)" << endl;
    cout << "============================================================" << endl;
    
    // Archivo CSV para resultados
    ofstream csvFile("resultados2.csv");
    csvFile << "n,tiempo_segundos" << endl;
    
    cout << "\n" << setw(12) << "n" 
         << setw(20) << "tiempo (s)" << endl;
    cout << string(32, '-') << endl;
    
    for (int n : n_values) {
        cout << "Ejecutando con n = " << n << "..." << flush;
        
        // Medir tiempo
        auto start = high_resolution_clock::now();
        function(n);
        auto end = high_resolution_clock::now();
        
        duration<double> elapsed = end - start;
        double seconds = elapsed.count();
        
        // Mostrar resultados
        cout << "\r" << setw(12) << n 
             << setw(20) << fixed << setprecision(6) << seconds << endl;
        
        // Guardar en CSV
        csvFile << n << "," << seconds << endl;
    }
    
    csvFile.close();
    
    cout << "============================================================" << endl;
    cout << "✓ Resultados guardados en 'resultados2.csv'" << endl;
    cout << "✓ Análisis completado!" << endl;
}

int main() {
    // Valores de n a probar
    vector<int> n_values = {1, 10, 100, 1000, 10000, 100000, 1000000};
    
    profileFunction(n_values);
    
    return 0;
}
