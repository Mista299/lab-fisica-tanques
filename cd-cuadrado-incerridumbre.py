import math
import numpy as np

# ============================================================
# DATOS NOMINALES - TANQUE CUADRADO
# ============================================================
g = 9.81

# Geometria
AT = 0.0056           # m2, area transversal (7 cm x 8 cm)
A0 = 0.000025         # m2, area del orificio (1 cm2)
h0 = 0.25             # m, altura inicial

# Cd obtenidos experimentalmente (promedio de todos los puntos)
Cd_agua   = 0.4164
Cd_aceite = 0.3983

# Incertidumbres estadisticas (tipo A) del Excel
u_stat_agua   = 0.0011
u_stat_aceite = 0.0008

# ============================================================
# INCERTIDUMBRES INSTRUMENTALES (tipo B)
# ============================================================
# Regla: ±1 mm -> lados del tanque: 7.0±0.1 cm y 8.0±0.1 cm
delta_a = 0.001   # m, incertidumbre en lado a = 7 cm
delta_b = 0.001   # m, incertidumbre en lado b = 8 cm
# AT = a*b -> dAT/AT = sqrt((da/a)^2 + (db/b)^2)
a, b = 0.07, 0.08
u_AT_rel = math.sqrt((delta_a/a)**2 + (delta_b/b)**2)

# Orificio: A0 = pi*(d/2)^2, diametro medido con calibre ±0.05 mm
# A0 nominal: 0.000025 m2 -> d = sqrt(4*A0/pi)
d_orificio = math.sqrt(4 * A0 / math.pi)
delta_d = 0.00005     # m, ±0.05 mm
# A0 = pi*d^2/4 -> dA0/A0 = 2*dd/d
u_A0_rel = 2 * delta_d / d_orificio

# Altura inicial: regla ±1 mm
delta_h0 = 0.001      # m
u_h0_rel = delta_h0 / h0

# ============================================================
# PROPAGACION DE INCERTIDUMBRE SISTEMATICA (tipo B)
# Para Cd = 2*AT*(sqrt(h0)-sqrt(h)) / (t*A0*sqrt(2g))
# Las variables AT, A0, h0 afectan sistematicamente.
# t y h son aleatorias (capturadas por tipo A).
#
# Derivadas relativas:
#   dCd/dAT * 1/Cd = 1/AT
#   dCd/dA0 * 1/Cd = -1/A0
#   dCd/dh0 * 1/Cd = 1/(2*sqrt(h0)*(sqrt(h0)-sqrt(h)))
#
# Para h tipica ~ h0/2 = 0.125 m:
#   (sqrt(h0)-sqrt(h)) ~ sqrt(0.25)-sqrt(0.125) = 0.5-0.354 = 0.146
#   dCd/dh0 * 1/Cd = 1/(2*0.5*0.146) = 6.85 -> u_Cd_rel_h0 = 6.85 * u_h0 = 6.85*0.001 = 0.00685
#   Pero esto depende fuertemente de h. Integrando sobre todos los puntos:
# ============================================================

# Para estimar la derivada promedio respecto a h0, usamos el valor tipico en t~33s (mitad del recorrido)
h_tipica = h0 / 2  # ~0.125 m
S = math.sqrt(h0) - math.sqrt(h_tipica)
dCd_dh0_rel = 1 / (2 * math.sqrt(h0) * S)  # (1/Cd)*(dCd/dh0)

u_h0_contrib = dCd_dh0_rel * delta_h0

# Incertidumbre sistematica relativa combinada
u_sys_rel = math.sqrt(u_AT_rel**2 + u_A0_rel**2 + u_h0_contrib**2)

# Incertidumbre sistematica absoluta para cada fluido
u_sys_agua   = Cd_agua   * u_sys_rel
u_sys_aceite = Cd_aceite * u_sys_rel

# ============================================================
# INCERTIDUMBRE COMBINADA (tipo A + tipo B)
# ============================================================
u_comb_agua   = math.sqrt(u_stat_agua**2   + u_sys_agua**2)
u_comb_aceite = math.sqrt(u_stat_aceite**2 + u_sys_aceite**2)

# ============================================================
# RESULTADOS
# ============================================================
print("=" * 65)
print("INCERTIDUMBRE DEL COEFICIENTE DE DESCARGA - TANQUE CUADRADO")
print("=" * 65)
print()
print("Parametros geometricos:")
print(f"  AT = {AT} m2  (lados a={a}±{delta_a} m, b={b}±{delta_b} m)")
print(f"  A0 = {A0} m2  (diametro orificio = {d_orificio*1000:.2f}±{delta_d*1000:.2f} mm)")
print(f"  h0 = {h0} m  (±{delta_h0} m)")
print()
print("Incertidumbres relativas instrumentales (tipo B):")
print(f"  u(AT)/AT  = {u_AT_rel*100:.1f} %")
print(f"  u(A0)/A0  = {u_A0_rel*100:.1f} %")
print(f"  u(h0)/h0  = {u_h0_rel*100:.1f} %  (contribucion a Cd: {u_h0_contrib*100:.2f} %)")
print(f"  u_sys/Cd (combinada) = {u_sys_rel*100:.2f} %")
print()
print("Resultados:")
print(f"  Agua:")
print(f"    Cd               = {Cd_agua:.4f}")
print(f"    u_tipo_A (estad)  = {u_stat_agua:.4f}")
print(f"    u_tipo_B (instr)  = {u_sys_agua:.4f}")
print(f"    u_combinada       = {u_comb_agua:.4f}")
print(f"    Cd = {Cd_agua:.4f} ± {u_comb_agua:.4f}")
print()
print(f"  Aceite:")
print(f"    Cd               = {Cd_aceite:.4f}")
print(f"    u_tipo_A (estad)  = {u_stat_aceite:.4f}")
print(f"    u_tipo_B (instr)  = {u_sys_aceite:.4f}")
print(f"    u_combinada       = {u_comb_aceite:.4f}")
print(f"    Cd = {Cd_aceite:.4f} ± {u_comb_aceite:.4f}")
