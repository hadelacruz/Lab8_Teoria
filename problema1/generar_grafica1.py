import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

def generar_graficas():
    """
    Lee el CSV generado por C++ y crea gráficas profesionales
    """
    # Verificar si existe el archivo CSV
    csv_file = 'resultados1.csv'
    
    if not os.path.exists(csv_file):
        print(f"❌ Error: No se encontró el archivo '{csv_file}'")
        print("   Por favor, ejecuta primero: .\\ejecutar1.bat")
        return
    
    # Leer datos del CSV
    df = pd.read_csv(csv_file)
    
    print("="*60)
    print("GENERANDO GRÁFICAS - PROBLEMA 1")
    print("="*60)
    print(f"\n📊 Datos leídos: {len(df)} mediciones")
    print("\nResultados:")
    print(df.to_string(index=False))
    
    # Crear figura con 2 subgráficas
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # Gráfica 1: Escala lineal
    ax1.plot(df['n'], df['tiempo_segundos'], marker='o', linewidth=2.5, 
             markersize=8, color='#2E86AB', markerfacecolor='#A23B72')
    ax1.set_xlabel('Tamaño de entrada (n)', fontsize=13, fontweight='bold')
    ax1.set_ylabel('Tiempo de ejecución (segundos)', fontsize=13, fontweight='bold')
    ax1.set_title('Problema 1: Tiempo vs Tamaño de entrada\n(Escala Lineal)', 
                  fontsize=14, fontweight='bold', pad=15)
    ax1.grid(True, alpha=0.3, linestyle='--')
    ax1.set_facecolor('#F8F9FA')
    
    # Anotaciones en puntos clave
    for i, row in df.iterrows():
        if row['n'] >= 1000:
            ax1.annotate(f"{row['tiempo_segundos']:.2f}s", 
                        (row['n'], row['tiempo_segundos']),
                        textcoords="offset points", xytext=(0,10),
                        ha='center', fontsize=9, color='#333333')
    
    # Gráfica 2: Escala logarítmica
    ax2.plot(df['n'], df['tiempo_segundos'], marker='s', linewidth=2.5,
             markersize=8, color='#F18F01', markerfacecolor='#C73E1D')
    ax2.set_xlabel('Tamaño de entrada (n)', fontsize=13, fontweight='bold')
    ax2.set_ylabel('Tiempo de ejecución (segundos)', fontsize=13, fontweight='bold')
    ax2.set_title('Problema 1: Tiempo vs Tamaño de entrada\n(Escala Log-Log)', 
                  fontsize=14, fontweight='bold', pad=15)
    ax2.set_xscale('log')
    ax2.set_yscale('log')
    ax2.grid(True, alpha=0.3, linestyle='--', which='both')
    ax2.set_facecolor('#F8F9FA')
    
    # Línea teórica O(n² log n)
    df_valid = df[df['tiempo_segundos'] > 0]
    if len(df_valid) > 0:
        idx_valid = df_valid.index[0]
        n0 = df.loc[idx_valid, 'n']
        t0 = df.loc[idx_valid, 'tiempo_segundos']
        k = t0 / (n0**2 * np.log2(n0))
        
        n_ref = np.logspace(0, np.log10(df['n'].max()), 100)
        tiempo_teorico = k * n_ref**2 * np.log2(n_ref)
        
        ax2.plot(n_ref, tiempo_teorico, '--', color='gray', alpha=0.5, 
                 linewidth=2, label='O(n² log n) teórico')
        ax2.legend(fontsize=10, loc='upper left')
    
    plt.tight_layout()
    
    # Guardar gráfica
    output_file = 'grafica1.png'
    plt.savefig(output_file, dpi=300, bbox_inches='tight', facecolor='white')
    
    print(f"\n✓ Gráfica guardada: '{output_file}'")
    print("="*60)
    
    plt.show()
    
    # Análisis
    print("\n📈 ANÁLISIS:")
    print(f"   • Complejidad: O(n² log n)")
    print(f"   • Rango n: {df['n'].min()} - {df['n'].max():,}")
    print(f"   • Tiempo mínimo: {df['tiempo_segundos'].min():.6f} segundos")
    print(f"   • Tiempo máximo: {df['tiempo_segundos'].max():.6f} segundos")
    print("\n¡Completado! 🎉\n")


if __name__ == "__main__":
    generar_graficas()
