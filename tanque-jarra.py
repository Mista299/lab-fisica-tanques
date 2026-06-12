import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root_scalar

# -----------------------------
# Datos experimentales
# -----------------------------
R = 0.123      # m
r0 = 0.114     # m
h0 = 0.113     # m

Cd = 0.62
A0 = 1.96e-5   # m²
g = 9.81       # m/s²

# Para el modelo del tronco de cono
H = h0

alpha = (R - r0) / H

# -----------------------------
# Función F(h)
# -----------------------------
def F(h):
    return (
        2 * r0**2 * np.sqrt(h)
        + (4/3) * alpha * r0 * h**(3/2)
        + (2/5) * alpha**2 * h**(5/2)
    )

# Constante del lado derecho
K = Cd * A0 * np.sqrt(2 * g) / np.pi

# -----------------------------
# Tiempo total de vaciado
# -----------------------------
t_v = F(h0) / K

print(f"Tiempo de vaciado ≈ {t_v:.2f} s")

# -----------------------------
# Vector de tiempo
# -----------------------------
t = np.linspace(0, t_v, 500)

# -----------------------------
# Resolver F(h)=F(h0)-Kt
# -----------------------------
h_vals = []

for ti in t:

    rhs = F(h0) - K * ti

    # Función cuya raíz buscamos
    def ecuacion(h):
        return F(h) - rhs

    sol = root_scalar(
        ecuacion,
        bracket=[0, h0],
        method='brentq'
    )

    h_vals.append(sol.root)

h_vals = np.array(h_vals)

# -----------------------------
# Gráfica
# -----------------------------
plt.figure(figsize=(8,5))

plt.plot(t, h_vals, linewidth=2)

plt.title("Vaciado de una jarra (tronco de cono)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Altura h(t) [m]")
plt.grid(True)

plt.axvline(
    t_v,
    color="red",
    linestyle="--",
    label=f"t_v ≈ {t_v:.1f} s"
)

plt.legend()
plt.tight_layout()
plt.show()