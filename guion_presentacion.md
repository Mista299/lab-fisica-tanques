## Guión para presentación del póster — 10 minutos (3 personas)

El póster se lee de izquierda a derecha en 3 columnas. Seguimos ese orden.

---

### Persona 1 — Columna izquierda (~3:30 min)

**[0:00 - 0:30] Título y presentación**
Buenos días, somos Maria Fernanda, Xiomara y Michael. Presentamos "Vaciado de Tanques y Determinación del Coeficiente de Descarga", del Laboratorio Integrado de Física, tutoría del profesor David Gómez.

**[0:30 - 1:15] Resumen y Objetivos**
Estudiamos el vaciado de dos geometrías —un tanque rectangular de 7×8 cm y una jarra troncocónica— usando agua y aceite de cocina. El objetivo fue determinar experimentalmente el coeficiente de descarga Cd, que corrige la diferencia entre el modelo ideal de Torricelli y el comportamiento real. Grabamos cada ensayo en video y extrajimos los datos con Tracker, obteniendo cientos de puntos de altura contra tiempo.

**[1:15 - 2:15] Marco Teórico**
La ecuación de Torricelli predice que la velocidad de salida es raíz de 2gh. El caudal ideal sería Ao por esa velocidad. Pero en la práctica el caudal real es menor por dos efectos: la vena contracta —el chorro se estrecha al salir del orificio— y la fricción. El coeficiente de descarga Cd recoge ambos efectos. Por conservación de masa, el caudal de salida iguala la disminución del volumen, lo que da la ecuación diferencial general: A de h por dh/dt igual a menos Cd por Ao por raíz de 2gh.

**[2:15 - 3:30] Modelado Matemático**
Esta ecuación se resuelve distinto según la geometría. Para el tanque rectangular, el área es constante y la solución es explícita: h de t igual a raíz de h0 menos k por t, todo al cuadrado. De aquí despejamos Cd directamente. Para la jarra troncocónica, el área varía con la altura: A de h es pi por r0 más alpha por h al cuadrado. Al integrar se obtiene una solución implícita: t en función de h, que no puede invertirse. Para graficar evaluamos t para distintos valores de h. El Cd se calcula como el promedio de los valores obtenidos para cada punto experimental. La incertidumbre se reporta combinando la estadística con la propagación de errores instrumentales. Mi compañera les explicará el montaje.

---

### Persona 2 — Columna central (~3:00 min)

**[3:30 - 4:15] Metodología Experimental**
Estos son nuestros dos montajes reales. El tanque rectangular mide 7 por 8 centímetros de base, 25 de altura, con orificio circular de 0.25 centímetros cuadrados. La jarra tiene 11.3 centímetros de altura, radio en la base de 5.7, en la boca de 6.15, con orificio de 5 milímetros de diámetro. Para cada uno grabamos el vaciado con agua y con aceite, cuatro videos en total. Los datos de altura contra tiempo se extrajeron cuadro por cuadro con Tracker.

**[4:15 - 5:15] Resultados — Gráficas**
Aquí están las cuatro gráficas. En cada una, la curva continua es el modelo teórico usando el Cd que calculamos, y los puntos azules o rojos son los datos de Tracker. Vean la coincidencia: el modelo y el experimento se alinean en todo el rango cuando se utiliza el Cd correcto. En el tanque rectangular el vaciado completo toma entre 121 y 127 segundos. En la jarra, entre 128 y 170 segundos —el aceite tarda mucho más en la jarra que en el tanque cuadrado porque la geometría variable amplifica el efecto de la viscosidad.

**[5:15 - 6:30] Tabla de resultados**
Esta tabla resume todo. Para el tanque rectangular: Cd de 0.4164 en agua y 0.3983 en aceite. Para la jarra: 0.5899 en agua y 0.4446 en aceite. Tres observaciones: todos los Cd están por debajo del valor ideal de 0.62 —nuestros orificios no son perfectos—; el aceite siempre da un Cd menor por su mayor viscosidad; y la jarra tiene un Cd más alto, lo que indica un orificio de mejor calidad. Mi compañero cerrará con el análisis de incertidumbre y las conclusiones.

---

### Persona 3 — Columna derecha (~3:30 min)

**[6:30 - 7:00] Cálculo de Cd desde Tracker**
¿Cómo obtuvimos estos números? Para cada punto de Tracker —un par tiempo-altura— despejamos Cd de la fórmula de su geometría. Luego promediamos todos los valores válidos, entre 580 y 1200 por experimento. Las fórmulas de despeje están aquí en el póster y los cálculos completos en la hoja vinculada de GitHub.

**[7:00 - 8:30] Análisis de Incertidumbre**
Pero un número sin incertidumbre no está completo. Tenemos dos fuentes. La tipo A es estadística: con tantos puntos, la desviación estándar dividida por raíz de N da valores muy pequeños, del orden de 0.001. La tipo B es instrumental: ¿qué tan bien medimos las dimensiones? Usamos regla de ±1 milímetro y calibre de ±0.05 milímetros. Propagamos esos errores por las fórmulas de Cd. Vean la tabla: uB es siempre unas diez veces mayor que uA. Por ejemplo, en el tanque cuadrado con agua, uA es 0.0011 pero uB es 0.0112. La combinada queda en 0.0112, dominada completamente por lo instrumental. La enseñanza es clara: grabar el doble de video no mejoraría casi nada; en cambio, usar un calibre más preciso sí reduciría el error significativamente.

**[8:30 - 9:30] Conclusiones**
Cuatro conclusiones, una por cada punto del póster.

Primero: el Cd como parámetro de ajuste. Sin el coeficiente de descarga, el modelo de Torricelli predice vaciados que no se parecen en nada a la realidad. Todos nuestros Cd quedaron por debajo del valor ideal de 0.62, y esa diferencia es justo la que corrige las pérdidas por contracción de la vena líquida y fricción en el orificio real.

Segundo: efecto de la geometría del orificio. La jarra troncocónica dio un Cd de 0.5899 en agua, muy cercano al ideal de 0.62, lo que indica que su orificio tiene bordes bien definidos. El tanque rectangular en cambio dio 0.4164, reflejando mayores pérdidas hidráulicas —su orificio no estaba tan bien fabricado.

Tercero: efecto de la viscosidad. En ambas geometrías el aceite dio un Cd menor que el agua —aproximadamente 0.40 a 0.44 frente a 0.42 a 0.59—. Esto es consistente con la física: un fluido más viscoso genera más pérdidas por fricción al pasar por el orificio.

Cuarto: la incertidumbre. La componente instrumental —regla de ±1 mm y calibre de ±0.05 mm— domina completamente sobre la estadística, que es del orden de 0.001. La lección práctica es que mejorar la precisión al medir las dimensiones del tanque y del orificio tendría mucho más impacto que grabar más video o tomar más datos.

**[9:30 - 10:00] Cierre**
Caracterizamos el Cd para dos geometrías y dos fluidos, validamos el modelo de Torricelli con el Cd experimental, y cuantificamos rigurosamente la incertidumbre. Quedamos atentos a sus preguntas. Gracias.
