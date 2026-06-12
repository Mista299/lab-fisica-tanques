import math

# --- DATOS NOMINALES DEL EXPERIMENTO 2 ---
V_litros = 1.5
V_m3 = V_litros / 1000  # Conversión obligatoria a m^3 (0.0015 m^3)
t = 97.2                # Segundos
Ao = 2.5e-5             # m^2
h0 = 0.113              # m
g = 9.81                # m/s^2

# --- CÁLCULO DEL Cd NOMINAL ---
denominador = t * Ao * math.sqrt(2 * g * h0)
Cd_calculado = V_m3 / denominador

print(f"Denominador exacto: {denominador:.8f}")
print(f"Valor nominal calculado de Cd: {Cd_calculado:.6f}")