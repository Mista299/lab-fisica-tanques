import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Parámetros físicos (SI)
# -----------------------------
h0 = 0.25          # m (25 cm)

Cd = 0.62          # coeficiente de descarga
A0 = 0.000025         # m² (1 cm²)
AT = 0.056          # m² (100 cm²)
g = 9.81           # m/s²

# -----------------------------
# Constante de la ecuación
# h(t) = (sqrt(h0) - k t)^2
# -----------------------------
k = (Cd * A0 * np.sqrt(2 * g)) / (2 * AT)

# Tiempo hasta vaciarse
t_end = np.sqrt(h0) / k

# Vector de tiempo
t = np.linspace(0, t_end, 500)

# Solución analítica
h = (np.sqrt(h0) - k * t)**2

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

agua_path = 'datos_experimentales/Datos agua.txt'
aceite_path = 'datos_experimentales/Datos aceite.txt'
t_agua, y_agua = parse_datos(agua_path)
t_aceite, y_aceite = parse_datos(aceite_path)

# -----------------------------
# Gráfica
# -----------------------------
plt.figure(figsize=(8, 5))
plt.plot(t, h, linewidth=2, label='Modelo teórico (agua)')
plt.scatter(t_agua, y_agua, color='blue', s=10, alpha=0.7, label='Datos experimentales (agua)')
plt.scatter(t_aceite, y_aceite, color='red', s=10, alpha=0.7, label='Datos experimentales (aceite)')

plt.title("Vaciado de un tanque cuadrado")
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

print(f"Tiempo de vaciado: {t_end:.2f} s")