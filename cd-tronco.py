import math

# Parámetros experimentales (Geometría 1)
h0 = 0.113          # m
r0 = 0.114          # m
R = 0.123           # m
d_o = 0.005         # m (5 mm)
tv = 145.2          # s
g = 9.81            # m/s^2

# Cálculos intermedios
alpha = (R - r0) / h0
Ao = math.pi * (d_o / 2)**2

# Cálculo de la función de forma F(h0)
term1 = 2 * (r0**2) * math.sqrt(h0)
term2 = (4/3) * alpha * r0 * (h0**(3/2))
term3 = (2/5) * (alpha**2) * (h0**(5/2))
F_h0 = term1 + term2 + term3

# Cálculo del coeficiente de descarga (Cd)
Cd = (math.pi * F_h0) / (Ao * math.sqrt(2 * g) * tv)

print(f"--- Resultados del Cálculo ---")
print(f"Alpha: {alpha:.6f}")
print(f"Ao: {Ao:.6e}")
print(f"F(h0): {F_h0:.6f}")
print(f"Cd calculado: {Cd:.6f}")