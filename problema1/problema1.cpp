#include <iostream>
#include <chrono>
#include <iomanip>
#include <fstream>
#include <vector>

using namespace std;
using namespace chrono;

long long function(int n) {
    int i, j, k;
    long long counter = 0;
    
    for (i = n/2; i <= n; i++) {
        for (j = 1; j+n/2 <= n; j++) {
            for (k = 1; k <= n; k = k*2) {
                counter++;
            }
        }
    }
    
    return counter;
}

void profileFunction(vector<int> n_values) {
    cout << "============================================================" << endl;
    cout << "ANÁLISIS DE COMPLEJIDAD - PROBLEMA 1 (C++)" << endl;
    cout << "============================================================" << endl;
    
    // Archivo CSV para resultados
    ofstream csvFile("resultados1.csv");
    csvFile << "n,tiempo_segundos,operaciones" << endl;
    
    cout << "\n" << setw(12) << "n" 
         << setw(20) << "tiempo (s)" 
         << setw(20) << "operaciones" << endl;
    cout << string(52, '-') << endl;
    
    for (int n : n_values) {
        cout << "Ejecutando con n = " << n << "..." << flush;
        
        // Medir tiempo
        auto start = high_resolution_clock::now();
        long long operations = function(n);
        auto end = high_resolution_clock::now();
        
        duration<double> elapsed = end - start;
        double seconds = elapsed.count();
        
        // Mostrar resultados
        cout << "\r" << setw(12) << n 
             << setw(20) << fixed << setprecision(6) << seconds
             << setw(20) << operations << endl;
        
        // Guardar en CSV
        csvFile << n << "," << seconds << "," << operations << endl;
    }
    
    csvFile.close();
    
    cout << "============================================================" << endl;
    cout << "✓ Resultados guardados en 'resultados1.csv'" << endl;
    cout << "✓ Análisis completado!" << endl;
}

int main() {
    // Valores de n a probar
    vector<int> n_values = {1, 10, 100, 1000, 10000, 100000, 1000000};
    
    profileFunction(n_values);
    
    return 0;
}
