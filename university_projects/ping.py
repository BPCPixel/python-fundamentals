import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns

# --- 1. DATOS (Cargados de las imágenes originales) ---
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

# Crear DataFrame
df = pd.DataFrame({
    'Ping': wifi_data + cable_data,
    'Conexion': ['WiFi']*60 + ['Cable']*60
})

# --- 2. CONFIGURACIÓN DE GRÁFICAS ---
sns.set_style("whitegrid")
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# --- GRÁFICA 1: HISTOGRAMAS + CURVA NORMAL ---
sns.histplot(data=df, x='Ping', hue='Conexion', kde=True, bins=10, ax=axes[0], palette=['orange', 'blue'])
axes[0].set_title('Distribución de Frecuencias (Ping)')
axes[0].set_xlabel('Ping (ms)')
axes[0].set_ylabel('Frecuencia')

# --- GRÁFICA 2: BOXPLOT (COMPARACIÓN CLARA) ---
sns.boxplot(data=df, x='Conexion', y='Ping', ax=axes[1], palette=['orange', 'blue'])
axes[1].set_title('Comparación de Estabilidad (Caja y Bigotes)')
axes[1].set_ylabel('Ping (ms) - Menor es mejor')

plt.tight_layout()
plt.show()

# --- 3. PRUEBA DE BONDAD DE AJUSTE (DISTRIBUCIONES) ---
# Esto es para la sección "Variables aleatorias y distribuciones"
print("\n--- ANÁLISIS DE DISTRIBUCIONES (CABLE) ---")
mu, std = stats.norm.fit(cable_data)
print(f"Ajuste Normal -> Media: {mu:.2f}, Std: {std:.2f}")

# Prueba de Shapiro-Wilk para ver si es Normal
stat, p = stats.shapiro(cable_data)
print(f"Prueba de Normalidad (Shapiro): p={p:.5f} (Si p < 0.05, NO es normal)")

# --- 4. PRUEBA DE HIPÓTESIS (T-STUDENT) ---
print("\n--- PRUEBA DE HIPÓTESIS: ¿Es el cable más rápido? ---")
# H0: Medias iguales
# H1: Media Cable < Media WiFi
t_stat, p_val = stats.ttest_ind(cable_data, wifi_data, alternative='less')
print(f"Estadístico T: {t_stat:.4f}")
print(f"Valor P: {p_val:.10e}") # Notación científica porque es muy pequeño

if p_val < 0.05:
    print("CONCLUSIÓN: Rechazamos H0. El CABLE es estadísticamente MÁS RÁPIDO.")
else:
    print("CONCLUSIÓN: No hay diferencia significativa.")

# --- 5. CÁLCULO DE PROBABILIDAD (Confirmando lo de David) ---
mean_diff = np.mean(wifi_data) - np.mean(cable_data)
std_diff = np.sqrt(np.var(wifi_data) + np.var(cable_data))
z_score = mean_diff / std_diff
prob_wifi_slower = stats.norm.cdf(z_score) * 100

print(f"\n--- PROBABILIDAD (CORREGIDA) ---")
print(f"Probabilidad de que el WiFi tenga MAS LAG que el cable: {prob_wifi_slower:.2f}%")
print(f"(Esto coincide con el 95% de David, pero interpretado correctamente: WiFi es PEOR).")