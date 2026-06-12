import math

# Valores nominales
Cd = 2.2907
F_h0 = 0.009208
r0 = 0.114
alpha = 0.079646
h0 = 0.113
Ao = 1.9635e-5
tv = 145.2

# Incertidumbres (ajusta estos valores según tu instrumento)
delta_h0 = 0.001
delta_Ao = 1e-6
delta_tv = 0.1

# Cálculo de la derivada F'(h0)
dF_dh0 = (r0 + alpha * h0)**2 / math.sqrt(h0)

# Propagación de incertidumbre
term_h0 = ( (dF_dh0 / F_h0) * delta_h0 )**2
term_Ao = (delta_Ao / Ao)**2
term_tv = (delta_tv / tv)**2

delta_Cd = Cd * math.sqrt(term_h0 + term_Ao + term_tv)

print(f"delta_Cd: {delta_Cd:.6f}")
print(f"Resultado: {Cd} ± {delta_Cd:.6f}")