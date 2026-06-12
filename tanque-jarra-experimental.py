import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Parámetros físicos (SI)
# -----------------------------
h0 = 0.25          # m, altura inicial del fluido

# Geometría del tronco de cono (jarra)
R_bottom = 0.05    # m, radio de la base (inferior)
R_top = 0.15       # m, radio de la boca (superior)
# --- Ajustar estos valores con las dimensiones reales de la jarra ---

# Orificio de salida
Cd = 0.62          # coeficiente de descarga
A0 = 0.000025      # m², área del orificio
g = 9.81           # m/s²

# -----------------------------
# Solución analítica implícita t(h) para tronco de cono
# AT(h) = pi * (R_bottom + alpha * h)^2
# t(h) = (2*pi / (Cd*A0*sqrt(2g))) * [R_b^2*(sqrt(h0)-sqrt(h)) +
#         (2/3)*R_b*alpha*(h0^(3/2)-h^(3/2)) + (1/5)*alpha^2*(h0^(5/2)-h^(5/2))]
# -----------------------------
alpha = (R_top - R_bottom) / h0
const = 2 * np.pi / (Cd * A0 * np.sqrt(2 * g))

def tiempo_desde_h(h):
    return const * (
        R_bottom**2 * (np.sqrt(h0) - np.sqrt(h))
        + (2 / 3) * R_bottom * alpha * (h0**(3 / 2) - h**(3 / 2))
        + (1 / 5) * alpha**2 * (h0**(5 / 2) - h**(5 / 2))
    )

t_end = tiempo_desde_h(0)

h_vals = np.linspace(0.001, h0, 500)
t_vals = tiempo_desde_h(h_vals)

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
                    t_val = float(parts[0])
                    y_val = float(parts[2])
                    t_data.append(t_val)
                    y_data.append(y_val)
                except ValueError:
                    continue
    return t_data, y_data

# --- Descomentar y ajustar rutas cuando tengas los datos ---
# agua_path = 'datos_experimentales/Datos jarra agua.txt'
# aceite_path = 'datos_experimentales/Datos jarra aceite.txt'
# t_agua, y_agua = parse_datos(agua_path)
# t_aceite, y_aceite = parse_datos(aceite_path)

# -----------------------------
# Gráfica
# -----------------------------
plt.figure(figsize=(8, 5))
plt.plot(t_vals, h_vals, linewidth=2, label='Modelo teórico (tronco de cono)')

# --- Descomentar cuando tengas los datos ---
# plt.scatter(t_agua, y_agua, color='blue', s=10, alpha=0.7, label='Datos experimentales (agua)')
# plt.scatter(t_aceite, y_aceite, color='red', s=10, alpha=0.7, label='Datos experimentales (aceite)')

plt.title("Vaciado de un tanque troncocónico (jarra)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Altura del fluido h(t) (m)")
plt.grid(True)

plt.axhline(0, color='black', linewidth=1)
plt.axvline(
    t_end,
    linestyle='--',
    color='red',
    label=f"t vaciado ≈ {t_end:.2f} s"
)

plt.legend()
plt.tight_layout()
plt.show()

print(f"Tiempo de vaciado teórico: {t_end:.2f} s")
print(f"Geometría: R_base = {R_bottom} m, R_boca = {R_top} m, h0 = {h0} m")
print(f"Ajusta R_bottom y R_top con las dimensiones reales de la jarra.")
