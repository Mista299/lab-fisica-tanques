import math

# --- 1. DATOS NOMINALES ---
Cd = 0.050169
V = 1.5         # Litros
t = 97.2        # Segundos
Ao = 2.5e-5     # m^2 (equivale a 0.000025 m^2)
h0 = 0.113      # m

# --- 2. INCERTIDUMBRES (ERRORES ABSOLUTOS) ---
# Valores que proporcionaste:
delta_Ao = 0.00001  # m^2 
delta_h = 0.001   # m

# Valores asumidos (cámbialos por los de tus instrumentos reales):
delta_V = 0.001    # L (Ejemplo: error de lectura de 10 mL)
delta_t = 0.001     # s (Ejemplo: tiempo de reacción con cronómetro)

# --- 3. CÁLCULO ---
# Calculamos cada término dentro de la raíz por separado
term_V = (delta_V / V) ** 2
term_t = (delta_t / t) ** 2
term_Ao = (delta_Ao / Ao) ** 2
term_h = (0.5 * (delta_h / h0)) ** 2

# Suma y raíz cuadrada (Incertidumbre relativa total)
incertidumbre_relativa = math.sqrt(term_V + term_t + term_Ao + term_h)

# Error absoluto final de Cd
delta_Cd = Cd * incertidumbre_relativa

print(f"Incertidumbre relativa total: {incertidumbre_relativa:.2f}")
print(f"Error absoluto (delta Cd) calculado: {delta_Cd:.4f}")
print(f"Valor final a reportar: Cd = {Cd:.4f} ± {delta_Cd:.4f}")