import math

# ============================================================
# DATOS NOMINALES - JARRA TRONCOCONICA
# ============================================================
g = 9.81

# Geometria
Rb  = 0.057            # m, radio base (11.4 cm diametro / 2)
Rt  = 0.0615           # m, radio boca (12.3 cm diametro / 2)
h0  = 0.113            # m, altura inicial (11.3 cm)
A0  = math.pi * 0.0025**2  # m2, orificio 0.5 cm diametro

# Cd obtenidos experimentalmente (promedio de todos los puntos)
Cd_agua   = 0.5899
Cd_aceite = 0.4446

# Incertidumbres estadisticas (tipo A) del Excel
u_stat_agua   = 0.0008
u_stat_aceite = 0.0009

# ============================================================
# INCERTIDUMBRES INSTRUMENTALES (tipo B)
# ============================================================
delta_Rb = 0.0005   # m, calibre ±0.5 mm
delta_Rt = 0.0005   # m, calibre ±0.5 mm
delta_h0 = 0.001    # m, regla ±1 mm
delta_d  = 0.00005  # m, calibre ±0.05 mm (diametro orificio)

# ============================================================
# FUNCION f(h) Y Cd
# ============================================================
def f_integral(h, Rb_loc, Rt_loc, h0_loc):
    alpha_loc = (Rt_loc - Rb_loc) / h0_loc
    return (Rb_loc**2 * (math.sqrt(h0_loc) - math.sqrt(h))
            + (2/3) * Rb_loc * alpha_loc * (h0_loc**1.5 - h**1.5)
            + (1/5) * alpha_loc**2 * (h0_loc**2.5 - h**2.5))

def calcular_Cd(t, h, Rb_loc, Rt_loc, h0_loc, A0_loc):
    f = f_integral(h, Rb_loc, Rt_loc, h0_loc)
    return (2 * math.pi / (t * A0_loc * math.sqrt(2 * g))) * f

# ============================================================
# PROPAGACION NUMERICA DE INCERTIDUMBRE SISTEMATICA (tipo B)
# Se evalua en un punto representativo (~mitad del vaciado)
# ============================================================
t_tip = 60.0
h_tip = h0 / 2

Cd_ref = calcular_Cd(t_tip, h_tip, Rb, Rt, h0, A0)

# Derivada numerica: (dCd/dx) ≈ (Cd(x+h) - Cd(x-h)) / (2h)
def dCd_dx_Rb(h_step):
    p = calcular_Cd(t_tip, h_tip, Rb + h_step, Rt, h0, A0)
    m = calcular_Cd(t_tip, h_tip, Rb - h_step, Rt, h0, A0)
    return (p - m) / (2 * h_step)

def dCd_dx_Rt(h_step):
    p = calcular_Cd(t_tip, h_tip, Rb, Rt + h_step, h0, A0)
    m = calcular_Cd(t_tip, h_tip, Rb, Rt - h_step, h0, A0)
    return (p - m) / (2 * h_step)

def dCd_dx_h0(h_step):
    p = calcular_Cd(t_tip, h_tip, Rb, Rt, h0 + h_step, A0)
    m = calcular_Cd(t_tip, h_tip, Rb, Rt, h0 - h_step, A0)
    return (p - m) / (2 * h_step)

# Paso pequeno para derivadas (0.1% del valor nominal)
eps_Rb = Rb * 0.001
eps_Rt = Rt * 0.001
eps_h0 = h0 * 0.001

# Contribuciones absolutas: u_x = |dCd/dx| * delta_x
u_Rb_contrib = abs(dCd_dx_Rb(eps_Rb)) * delta_Rb
u_Rt_contrib = abs(dCd_dx_Rt(eps_Rt)) * delta_Rt
u_h0_contrib = abs(dCd_dx_h0(eps_h0)) * delta_h0

# A0 = pi*d^2/4 -> u(A0)/A0 = 2*u(d)/d
d_orificio = math.sqrt(4 * A0 / math.pi)
u_A0_rel = 2 * delta_d / d_orificio

# Contribuciones relativas para mostrar
u_Rb_rel = u_Rb_contrib / Cd_ref
u_Rt_rel = u_Rt_contrib / Cd_ref
u_h0_rel = u_h0_contrib / Cd_ref

# Incertidumbre sistematica relativa combinada
u_sys_rel = math.sqrt(u_Rb_rel**2 + u_Rt_rel**2 + u_h0_rel**2 + u_A0_rel**2)

# Incertidumbre sistematica absoluta
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
print("INCERTIDUMBRE DEL COEFICIENTE DE DESCARGA - JARRA TRONCOCONICA")
print("=" * 65)
print()
print("Parametros geometricos:")
print(f"  Rb  = {Rb} m  (±{delta_Rb} m, calibre)")
print(f"  Rt  = {Rt} m  (±{delta_Rt} m, calibre)")
print(f"  h0  = {h0} m  (±{delta_h0} m, regla)")
print(f"  A0  = {A0:.6f} m2  (diam. orificio = {d_orificio*1000:.1f}±{delta_d*1000:.2f} mm)")
print(f"  Punto tipico evaluado: t={t_tip}s, h={h_tip:.4f}m")
print()
print("Incertidumbres relativas instrumentales (tipo B):")
print(f"  u(Rb)/Cd  = {u_Rb_rel*100:.2f} %")
print(f"  u(Rt)/Cd  = {u_Rt_rel*100:.2f} %")
print(f"  u(h0)/Cd  = {u_h0_rel*100:.2f} %")
print(f"  u(A0)/A0  = {u_A0_rel*100:.1f} %")
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
