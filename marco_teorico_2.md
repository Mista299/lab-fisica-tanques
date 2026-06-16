## 2.1 Ecuación de Torricelli

Aplicando la ecuación de Bernoulli entre la superficie libre del fluido y la sección de salida del orificio, la velocidad teórica de descarga es:

$$v = \sqrt{2gh}$$

donde $$v$$ [m/s] es la velocidad de salida, $$g = 9.81\ \text{m/s}^2$$ y $$h$$ [m] es la altura de la columna de fluido sobre el centro del orificio. Esta expresión es independiente de la densidad del fluido y válida cuando $$A_T \gg A_o$$.

## 2.2 Caudal teórico

El caudal volumétrico teórico a través del orificio de área $$A_o$$ es:

$$Q_{\text{teo}} = A_o \cdot v = A_o \sqrt{2gh}$$

Para el orificio circular de diámetro $$d_o$$:

$$A_o = \frac{\pi d_o^2}{4}$$

Para el orificio cuadrado de lado $$a$$:

$$A_o = a^2$$

Para comparación justa, se fija $$A_{o,\text{circ}} = A_{o,\text{cuad}}$$, lo que implica:

$$a = d_o\sqrt{\frac{\pi}{4}} \approx 0.886\, d_o$$

Con $$d_o = 5\ \text{mm}$$ se obtiene $$a \approx 4.4\ \text{mm}$$.

## 2.3 Coeficiente de descarga

El caudal real $$Q_{\text{exp}}$$ es menor al teórico por dos efectos: (a) contracción del chorro (vena contracta), donde el área efectiva de flujo es menor que el área geométrica del orificio, y (b) pérdidas viscosas. El coeficiente de descarga $$C_d$$ cuantifica esta discrepancia:

$$C_d = \frac{Q_{\text{exp}}}{Q_{\text{teo}}}$$

$$Q_{\text{exp}} = C_d \, Q_{\text{teo}}$$

$$Q_{\text{exp}} = C_d \, A_o \sqrt{2gh}$$

La geometría del orificio determina la magnitud de la vena contracta. Para el orificio circular de filo vivo, la contracción es uniforme y simétrica en todas las direcciones radiales: $$C_d \approx 0.61{-}0.65$$. Para el orificio cuadrado, las esquinas generan una contracción asimétrica mayor que en los lados planos, lo que produce una vena contracta de sección no circular y, en general, un $$C_d$$ ligeramente menor o similar: $$C_d \approx 0.58{-}0.65$$. Ambos orificios están sin limar (filo vivo) para esta práctica.
