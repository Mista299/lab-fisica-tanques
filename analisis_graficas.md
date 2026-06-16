## Análisis de resultados experimentales

### Tanque cuadrado

La Figura 1 presenta la comparación entre el modelo teórico y los datos experimentales para el vaciado del tanque de sección transversal cuadrada de 7 cm × 8 cm (área transversal AT = 0.0056 m²) con un orificio de salida de área A0 = 2.5 × 10⁻⁵ m². El modelo teórico corresponde a la solución analítica de la ecuación de Torricelli para un tanque de sección constante:

$$h(t) = \left( \sqrt{h_0} - k\,t \right)^2 \quad \text{con} \quad k = \frac{C_d\,A_0\,\sqrt{2g}}{2\,A_T}$$

donde h0 = 0.25 m es la altura inicial y el coeficiente de descarga Cd se determinó a partir del ajuste con los datos experimentales.

Figura 1. Comparación entre el modelo teórico y los datos experimentales para el vaciado del tanque cuadrado con agua (izquierda) y aceite de cocina (derecha).

Para el agua, el coeficiente de descarga obtenido fue Cd = 0.4164, lo que predice un tiempo de vaciado total de tv ≈ 121.4 s. Como se observa en la Figura 1 (izquierda), la curva teórica describe con muy buena precisión la evolución temporal de la altura del fluido registrada mediante Tracker. La desviación entre el modelo y los datos es mínima a lo largo de todo el rango de medición, con diferencias relativas inferiores al 3 % en puntos intermedios como t ≈ 40 s. La línea vertical discontinua marca el tiempo de vaciado extrapolado por el modelo, que resulta razonable dado que los datos experimentales abarcan desde h = 0.249 m hasta aproximadamente h = 0.049 m.

Para el aceite de cocina, el coeficiente de descarga resultó ser Cd = 0.3983, con un tiempo de vaciado de tv ≈ 127.0 s. La Figura 1 (derecha) muestra igualmente una concordancia satisfactoria entre la curva teórica y las mediciones. La dispersión de los puntos experimentales es ligeramente mayor que en el caso del agua, lo cual se atribuye a la mayor viscosidad del aceite de cocina (μ ≈ 50 mPa·s frente a μ ≈ 1 mPa·s del agua), que genera fluctuaciones en la dinámica del flujo y dificulta la detección precisa de la interfaz aire-líquido por parte de Tracker.

El valor de Cd para el aceite es menor que para el agua (0.3983 frente a 0.4164), comportamiento físicamente esperado: un fluido más viscoso reduce el número de Reynolds en el orificio, incrementa las pérdidas por fricción y, en consecuencia, disminuye el coeficiente de descarga efectivo.

Es importante señalar que los valores de Cd utilizados en las curvas teóricas no corresponden al valor estándar de libro Cd = 0.62 (orificio de pared delgada con bordes vivos, norma ISO 5167), sino que fueron determinados experimentalmente invirtiendo el modelo analítico y promediando los Cd obtenidos para cada par (t, h) medido con Tracker. El procedimiento detallado de cálculo del coeficiente de descarga, incluyendo el tratamiento estadístico completo (promedio, desviación estándar e incertidumbre), se describe en la sección de determinación del coeficiente de descarga.

### Jarra troncocónica

La Figura 2 presenta los resultados correspondientes al vaciado de la jarra con geometría de tronco de cono, cuyos parámetros geométricos son: radio de la base Rb = 5.7 cm, radio de la boca Rt = 6.15 cm, altura inicial h0 = 11.3 cm y orificio de salida de 0.5 cm de diámetro (A0 = 1.96 × 10⁻⁵ m²). La solución analítica para esta geometría es más compleja que la del tanque cuadrado, ya que el área transversal varía linealmente con la altura según AT(h) = π (Rb + α h)² con α = (Rt − Rb) / h0, lo que conduce a una relación implícita t(h):

$$t(h) = \frac{2\pi}{C_d\,A_0\,\sqrt{2g}}\left[ R_b^2\left(\sqrt{h_0}-\sqrt{h}\right) + \frac{2}{3}R_b\,\alpha\left(h_0^{3/2}-h^{3/2}\right) + \frac{1}{5}\alpha^2\left(h_0^{5/2}-h^{5/2}\right) \right]$$

Figura 2. Comparación entre el modelo teórico y los datos experimentales para el vaciado de la jarra troncocónica con agua (izquierda) y aceite de cocina (derecha).

Para el agua, el coeficiente de descarga ajustado es Cd = 0.5899, notablemente cercano al valor de referencia 0.62. Esto sugiere que el orificio de la jarra posee una geometría con bordes más definidos y pared más delgada que el del tanque cuadrado (cuyo Cd = 0.4164), lo que se traduce en una menor contracción de la vena líquida y menores pérdidas hidráulicas. El tiempo de vaciado teórico resultante es tv ≈ 128.4 s.

La Figura 2 (izquierda) muestra que el modelo describe correctamente la tendencia de los datos experimentales a lo largo de todo el intervalo de medición. Se observa que la curva teórica presenta una pendiente variable característica del tronco de cono: el vaciado se acelera hacia el final debido a que el área transversal disminuye con la altura (el radio es menor en la base que en la boca), lo que reduce el volumen remanente y acelera el descenso del nivel del fluido.

Para el aceite de cocina, el coeficiente de descarga obtenido es Cd = 0.4446, con un tiempo de vaciado de tv ≈ 170.3 s. La diferencia temporal entre ambos fluidos (aproximadamente 42 s) es considerablemente mayor que la observada en el tanque cuadrado (5.6 s), lo cual se explica por el efecto combinado de la mayor viscosidad del aceite y la geometría variable del tanque: en un tronco de cono, la sensibilidad del tiempo de vaciado al coeficiente de descarga se ve amplificada por la dependencia no lineal del área transversal con la altura.

Al igual que en el caso del tanque cuadrado, los valores de Cd presentados no son supuestos sino calculados a partir de los datos experimentales mediante la inversión numérica del modelo del tronco de cono, promediando sobre todos los puntos (t, h) registrados por Tracker. El fundamento teórico, la metodología de cálculo y el análisis de incertidumbre se desarrollan en la sección dedicada a la determinación del coeficiente de descarga.

## Referencias

- White, F. M. (2016). *Fluid Mechanics* (8th ed.). McGraw-Hill.
- Cengel, Y. A., & Cimbala, J. M. (2018). *Fluid Mechanics: Fundamentals and Applications* (4th ed.). McGraw-Hill.
- ISO 5167-1:2003. *Measurement of fluid flow by means of pressure differential devices inserted in circular cross-section conduits running full*. International Organization for Standardization.
