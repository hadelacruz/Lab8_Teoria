import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

def generar_graficas():
    """
    Lee el CSV generado por C++ y crea gráficas profesionales
    """
    # Verificar si existe el archivo CSV
    csv_file = 'resultados2.csv'
    
    if not os.path.exists(csv_file):
        print(f"❌ Error: No se encontró el archivo '{csv_file}'")
        print("   Por favor, ejecuta primero: .\\ejecutar2.bat")
        return
    
    # Leer datos del CSV
    df = pd.read_csv(csv_file)
    
    print("="*60)
    print("GENERANDO GRÁFICAS - PROBLEMA 2")
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
    ax1.set_title('Problema 2: Tiempo vs Tamaño de entrada\n(Escala Lineal)', 
                  fontsize=14, fontweight='bold', pad=15)
    ax1.grid(True, alpha=0.3, linestyle='--')
    ax1.set_facecolor('#F8F9FA')
    
    # Anotaciones en puntos clave
    for i, row in df.iterrows():
        if row['n'] >= 10000 and row['tiempo_segundos'] > 0:
            ax1.annotate(f"{row['tiempo_segundos']:.6f}s", 
                        (row['n'], row['tiempo_segundos']),
                        textcoords="offset points", xytext=(0,10),
                        ha='center', fontsize=9, color='#333333')
    
    # Gráfica 2: Escala logarítmica
    ax2.plot(df['n'], df['tiempo_segundos'], marker='s', linewidth=2.5,
             markersize=8, color='#F18F01', markerfacecolor='#C73E1D')
    ax2.set_xlabel('Tamaño de entrada (n)', fontsize=13, fontweight='bold')
    ax2.set_ylabel('Tiempo de ejecución (segundos)', fontsize=13, fontweight='bold')
    ax2.set_title('Problema 2: Tiempo vs Tamaño de entrada\n(Escala Log-Log)', 
                  fontsize=14, fontweight='bold', pad=15)
    ax2.set_xscale('log')
    
    # Solo usar escala log en Y si hay valores positivos
    if df['tiempo_segundos'].max() > 0:
        ax2.set_yscale('log')
    
    ax2.grid(True, alpha=0.3, linestyle='--', which='both')
    ax2.set_facecolor('#F8F9FA')
    
    # Línea teórica O(n)
    df_valid = df[df['tiempo_segundos'] > 0]
    if len(df_valid) > 0:
        n0 = df_valid.iloc[0]['n']
        t0 = df_valid.iloc[0]['tiempo_segundos']
        k = t0 / n0
        
        n_ref = np.logspace(np.log10(df['n'].min()), np.log10(df['n'].max()), 100)
        tiempo_teorico = k * n_ref
        
        ax2.plot(n_ref, tiempo_teorico, '--', color='gray', alpha=0.5, 
                 linewidth=2, label='O(n) teórico')
        ax2.legend(fontsize=10, loc='upper left')
    
    plt.tight_layout()
    
    # Guardar gráfica
    output_file = 'grafica2.png'
    plt.savefig(output_file, dpi=300, bbox_inches='tight', facecolor='white')
    
    print(f"\n✓ Gráfica guardada: '{output_file}'")
    print("="*60)
    
    plt.show()
    
    # Análisis
    print("\n📈 ANÁLISIS:")
    print(f"   • Complejidad: O(n) - Lineal")
    print(f"   • Rango n: {df['n'].min()} - {df['n'].max():,}")
    print(f"   • Tiempo máximo: {df['tiempo_segundos'].max():.6f} segundos")
    print(f"   • Operaciones máximas: {df['operaciones'].max():,}")
    print(f"\n💡 El 'break' convierte O(n²) en O(n)")
    print("\n¡Completado! 🎉\n")


if __name__ == "__main__":
    generar_graficas()
