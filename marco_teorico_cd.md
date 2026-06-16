## Marco teórico: Coeficiente de descarga

### Ecuación de Torricelli

Cuando un fluido sale por un orificio en el fondo de un tanque, la velocidad ideal de salida está dada por la ecuación de Torricelli:

$$v_{\text{ideal}} = \sqrt{2gh}$$

donde $$g$$ es la aceleración de la gravedad y $$h$$ la altura del fluido sobre el orificio. Esta expresión se obtiene aplicando la ecuación de Bernoulli entre la superficie libre y el orificio, asumiendo un fluido ideal sin pérdidas.

El caudal volumétrico ideal sería:

$$Q_{\text{ideal}} = A_0 \sqrt{2gh}$$

donde $$A_0$$ es el área geométrica del orificio.

### El coeficiente de descarga

En la práctica, el caudal real es menor que el ideal debido a dos fenómenos físicos:

1. **Contracción de la vena líquida:** al atravesar el orificio, las líneas de corriente convergen y la sección efectiva del chorro se reduce. El área real de salida es $$A_c = C_c A_0$$, donde $$C_c$$ es el coeficiente de contracción.

2. **Pérdidas por fricción:** la viscosidad del fluido y la geometría del orificio disipan energía, reduciendo la velocidad real de salida: $$v_{\text{real}} = C_v v_{\text{ideal}}$$, donde $$C_v$$ es el coeficiente de velocidad.

El coeficiente de descarga engloba ambos efectos:

$$C_d = C_c \cdot C_v$$

Y el caudal real queda expresado como:

$$Q_{\text{real}} = C_d \, A_0 \sqrt{2gh}$$

### Valores de referencia

El valor de $$C_d$$ depende principalmente de la geometría del orificio, no del fluido. En régimen turbulento, los valores típicos son:

- Orificio de pared delgada con bordes vivos: $$C_d \approx 0.62$$
- Orificio con bordes redondeados: $$C_d \approx 0.80$$ a $$0.95$$
- Boquilla convergente (bellmouth): $$C_d \approx 0.98$$

Un fluido más viscoso reduce el número de Reynolds y puede disminuir ligeramente el $$C_d$$, aunque el efecto dominante es geométrico.

### Determinación experimental

El $$C_d$$ se obtiene experimentalmente invirtiendo el modelo de vaciado del tanque. Para ello se mide la altura del fluido $$h(t)$$ en función del tiempo con un sistema de video (Tracker) y se despeja $$C_d$$ de la ecuación de conservación de masa:

$$\frac{dh}{dt} = -\frac{C_d A_0}{A_T(h)} \sqrt{2gh}$$

La solución de esta ecuación diferencial depende de la geometría del tanque.

Para un **tanque de sección constante** (área $$A_T$$ fija), la solución analítica es:

$$h(t) = \left( \sqrt{h_0} - k t \right)^2 \quad \text{donde} \quad k = \frac{C_d A_0 \sqrt{2g}}{2 A_T}$$

Invirtiendo para despejar $$C_d$$:

$$C_d = \frac{2 A_T \left( \sqrt{h_0} - \sqrt{h} \right)}{t \, A_0 \sqrt{2g}}$$

Para un **tanque troncocónico**, el área transversal varía con la altura según $$A_T(h) = \pi (R_b + \alpha h)^2$$, donde $$\alpha = (R_t - R_b)/h_0$$, $$R_b$$ es el radio de la base y $$R_t$$ el radio de la boca. La solución analítica conduce a la relación implícita:

$$t(h) = \frac{2\pi}{C_d A_0 \sqrt{2g}} \left[ R_b^2 \left( \sqrt{h_0} - \sqrt{h} \right) + \frac{2}{3} R_b \alpha \left( h_0^{3/2} - h^{3/2} \right) + \frac{1}{5} \alpha^2 \left( h_0^{5/2} - h^{5/2} \right) \right]$$

De la cual se despeja:

$$C_d = \frac{2\pi}{t A_0 \sqrt{2g}} \left[ R_b^2 \left( \sqrt{h_0} - \sqrt{h} \right) + \frac{2}{3} R_b \alpha \left( h_0^{3/2} - h^{3/2} \right) + \frac{1}{5} \alpha^2 \left( h_0^{5/2} - h^{5/2} \right) \right]$$

### Tratamiento estadístico

Para cada punto experimental $$(t_i, h_i)$$ registrado por Tracker se calcula un valor individual de $$C_d$$. El resultado final se reporta como el promedio $$\overline{C_d}$$ con su incertidumbre $$\sigma / \sqrt{N}$$, donde $$\sigma$$ es la desviación estándar muestral y $$N$$ el número de puntos válidos.
