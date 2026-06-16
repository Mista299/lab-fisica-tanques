import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Parámetros físicos (SI)
# -----------------------------
h0 = 0.25          # m (25 cm)
A0 = 0.000025      # m² (1 cm²)
AT = 0.0056        # m² (7 cm × 8 cm = 56 cm²)
g = 9.81           # m/s²

# -----------------------------
# Solución analítica: h(t) = (sqrt(h0) - k t)^2
# k = (Cd * A0 * sqrt(2g)) / (2 * AT)
# -----------------------------
def modelo_teorico(Cd):
    k = (Cd * A0 * np.sqrt(2 * g)) / (2 * AT)
    t_end = np.sqrt(h0) / k
    t = np.linspace(0, t_end, 500)
    h = (np.sqrt(h0) - k * t)**2
    return t, h, t_end

def calcular_Cd(t, h):
    k = (np.sqrt(h0) - np.sqrt(h)) / t
    return (k * 2 * AT) / (A0 * np.sqrt(2 * g))

# -----------------------------
# Lectura de datos experimentales
# -----------------------------
def parse_datos(filepath):
    t_data, y_data = [], []
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.replace(',', '.').split('\t')
            if len(parts) >= 3:
                try:
                    t_data.append(float(parts[0]))
                    y_data.append(float(parts[2]))
                except ValueError:
                    continue
    return np.array(t_data), np.array(y_data)

agua_path = 'datos_experimentales/cuadrado/Datos agua.txt'
aceite_path = 'datos_experimentales/cuadrado/Datos aceite.txt'
t_agua, y_agua = parse_datos(agua_path)
t_aceite, y_aceite = parse_datos(aceite_path)

# -----------------------------
# Cálculo de Cd desde datos experimentales (promedio todos los puntos)
# -----------------------------
cds_agua = [calcular_Cd(t, h) for t, h in zip(t_agua, y_agua) if h > 0 and h < h0 and t > 0]
cds_aceite = [calcular_Cd(t, h) for t, h in zip(t_aceite, y_aceite) if h > 0 and h < h0 and t > 0]
cds_agua = [c for c in cds_agua if 0 < c < 2]
cds_aceite = [c for c in cds_aceite if 0 < c < 2]

Cd_agua = np.mean(cds_agua)
Cd_aceite = np.mean(cds_aceite)
sigma_agua = np.std(cds_agua, ddof=1) / np.sqrt(len(cds_agua))
sigma_aceite = np.std(cds_aceite, ddof=1) / np.sqrt(len(cds_aceite))

print("=== Cálculo de Cd (promedio sobre todos los puntos) ===")
print(f"  Agua:   N = {len(cds_agua):d}  ->  Cd = {Cd_agua:.4f} ± {sigma_agua:.4f}")
print(f"  Aceite: N = {len(cds_aceite):d}  ->  Cd = {Cd_aceite:.4f} ± {sigma_aceite:.4f}")
print()

# -----------------------------
# Curvas teóricas con los Cd calculados
# -----------------------------
t_agua_teo, h_agua_teo, t_end_agua = modelo_teorico(Cd_agua)
t_aceite_teo, h_aceite_teo, t_end_aceite = modelo_teorico(Cd_aceite)

print(f"Tiempo de vaciado teórico (agua):   {t_end_agua:.1f} s")
print(f"Tiempo de vaciado teórico (aceite): {t_end_aceite:.1f} s")

# -----------------------------
# Gráficas (subplots lado a lado)
# -----------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# --- Agua ---
ax1.plot(t_agua_teo, h_agua_teo, linewidth=2, color='navy', label=f'Modelo teórico (Cd={Cd_agua:.2f})')
ax1.scatter(t_agua, y_agua, color='dodgerblue', s=8, alpha=0.7, label='Datos experimentales')
ax1.set_title("Agua")
ax1.set_xlabel("Tiempo (s)")
ax1.set_ylabel("Altura del fluido h(t) (m)")
ax1.grid(True)
ax1.axhline(0, color='black', linewidth=1)
ax1.axvline(t_end_agua, linestyle='--', color='gray', label=f"t vaciado ≈ {t_end_agua:.1f} s")
ax1.legend()

# --- Aceite ---
ax2.plot(t_aceite_teo, h_aceite_teo, linewidth=2, color='darkorange', label=f'Modelo teórico (Cd={Cd_aceite:.2f})')
ax2.scatter(t_aceite, y_aceite, color='red', s=8, alpha=0.7, label='Datos experimentales')
ax2.set_title("Aceite de cocina")
ax2.set_xlabel("Tiempo (s)")
ax2.set_ylabel("Altura del fluido h(t) (m)")
ax2.grid(True)
ax2.axhline(0, color='black', linewidth=1)
ax2.axvline(t_end_aceite, linestyle='--', color='gray', label=f"t vaciado ≈ {t_end_aceite:.1f} s")
ax2.legend()

plt.suptitle("Vaciado de un tanque cuadrado", fontsize=14)
plt.tight_layout()
plt.show()