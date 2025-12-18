import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns

# ==========================================
# 1. CARGA DE DATOS (Recolección)
# ==========================================
wifi_data = [
    59, 58, 60, 57, 58, 60, 57, 61, 60, 56, 59, 60, 59, 60, 53, 55, 57, 41, 51, 60,
    61, 49, 44, 63, 55, 59, 55, 47, 42, 40, 45, 61, 58, 55, 49, 61, 66, 64, 69, 75,
    70, 60, 73, 56, 74, 71, 59, 57, 58, 63, 57, 51, 57, 63, 76, 56, 45, 52, 57, 73
]

cable_data = [
    35, 34, 31, 30, 32, 33, 34, 35, 37, 47, 48, 37, 36, 33, 35, 37, 39, 40, 36, 42,
    44, 46, 43, 41, 39, 38, 36, 35, 52, 44, 42, 37, 40, 38, 42, 37, 40, 45, 53, 35,
    41, 43, 37, 40, 36, 33, 35, 55, 43, 39, 40, 41, 34, 33, 36, 34, 38, 57, 54, 58
]


df = pd.DataFrame({
    'Ping': wifi_data + cable_data,
    'Conexion': ['WiFi']*60 + ['Cable']*60
})

# ==========================================
# 2. ESTADÍSTICA DESCRIPTIVA (Análisis Numérico)
# ==========================================
print("\n--- 1. RESUMEN ESTADÍSTICO ---")

resumen = df.groupby('Conexion')['Ping'].describe()
print(resumen)


print("\n--- VARIANZA (Qué tan dispersos están los datos) ---")
varianza = df.groupby('Conexion')['Ping'].var()
print(varianza)

# ==========================================
# 3. PRUEBA DE HIPÓTESIS (Ciencia de datos)
# ==========================================
print("\n--- 2. PRUEBA T-STUDENT (Validación Científica) ---")
# Objetivo: Demostrar matemáticamente que la diferencia no es suerte.
# H0 (Nula): El ping es igual en ambos.
# H1 (Alternativa): El ping de Cable es MENOR (más rápido) que el de WiFi.
t_stat, p_val = stats.ttest_ind(cable_data, wifi_data, alternative='less')

print(f"Valor T: {t_stat:.4f}")
print(f"Valor P (P-Value): {p_val:.10f}")

if p_val < 0.05:
    print("CONCLUSIÓN: El valor P es menor a 0.05.")
    print("Esto confirma científicamente que el CABLE es más rápido.")
else:
    print("CONCLUSIÓN: No hay suficiente evidencia.")

# ==========================================
# 4. GENERACIÓN DE GRÁFICAS (Visualización)
# ==========================================

sns.set_style("whitegrid")

# --- VENTANA 1: HISTOGRAMA ---
plt.figure(figsize=(10, 6))

sns.histplot(
    data=df,
    x='Ping',
    hue='Conexion',
    kde=True,
    bins=10,
    palette=['orange', 'blue']
)

plt.title('Comparación de Frecuencias: WiFi llega a pings más altos')
plt.xlabel('Ping (ms) - Hacia la derecha es más lento')
plt.ylabel('Frecuencia (Cantidad de veces)')

plt.show()  # PRIMERA VENTANA

# --- VENTANA 2: BOXPLOT ---
plt.figure(figsize=(8, 5))

sns.boxplot(
    data=df,
    x='Conexion',
    y='Ping',
    hue='Conexion',
    legend=False,
    palette=['orange', 'blue']
)

plt.title('Rango de Estabilidad (Menos es mejor)')
plt.ylabel('Ping (ms)')

plt.show()  # SEGUNDA VENTANA
