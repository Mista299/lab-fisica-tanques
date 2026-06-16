## Guión para presentación del póster — 10 minutos (3 personas)

---

### Persona 1 — Introducción y Marco Teórico (~3:00 min)

**[0:00 - 0:30] Título y contexto**
Buenos días, somos Maria Fernanda, Xiomara y Michael. Presentamos nuestro proyecto "Vaciado de Tanques y Determinación del Coeficiente de Descarga", desarrollado en el Laboratorio Integrado de Física bajo la tutoría del profesor David Gómez.

**[0:30 - 1:15] Resumen y Objetivos**
El problema que abordamos es simple de enunciar pero rico en física: ¿cuánto tarda en vaciarse un tanque por un agujero en el fondo? Estudiamos dos geometrías —un tanque rectangular y una jarra troncocónica— usando agua y aceite de cocina. Nuestro objetivo fue determinar experimentalmente el coeficiente de descarga Cd, que es el parámetro que corrige la diferencia entre la teoría ideal y el comportamiento real del fluido.

**[1:15 - 2:30] Marco Teórico**
La ecuación de Torricelli, derivada de Bernoulli, predice que la velocidad de salida es raíz de 2gh. Pero en la práctica el caudal real es menor por dos razones: la vena contracta —el chorro se estrecha al salir— y la fricción en el orificio. El coeficiente de descarga Cd cuantifica ambos efectos.

**[2:30 - 3:00] Ecuación de vaciado**
Por conservación de masa, el caudal que sale debe igualar la disminución del volumen almacenado. Esto da la ecuación diferencial: A(h) por dh/dt igual a menos Cd por Ao por raíz de 2gh. Esta ecuación se resuelve distinto según la geometría. Mi compañera les explicará cómo.

---

### Persona 2 — Metodología y Modelado (~3:00 min)

**[3:00 - 3:45] Montaje experimental**
Trabajamos con dos recipientes reales. El tanque rectangular mide 7 por 8 centímetros de base y 25 de altura, con un orificio circular de 0.25 centímetros cuadrados. La jarra troncocónica tiene 11.3 centímetros de altura, radio en la base de 5.7 y en la boca de 6.15 centímetros, con un orificio de 5 milímetros de diámetro. Para cada montaje grabamos videos del vaciado y extrajimos los datos con Tracker, obteniendo cientos de puntos de altura contra tiempo.

**[3:45 - 4:45] Solución matemática para cada geometría**
Para el tanque rectangular, la sección es constante, así que la ecuación diferencial tiene solución explícita: h de t es igual a raíz de h0 menos k por t, todo al cuadrado. Esta fórmula permite despejar Cd directamente.

Para la jarra, el área varía con la altura: el radio en función de h es r0 más alpha por h. Al integrar, la solución es implícita: obtenemos t en función de h, pero no se puede despejar h de t algebraicamente. Para graficar, evaluamos la fórmula para distintos valores de h entre 0 y h0.

**[4:45 - 5:30] Cálculo del Cd**
¿Cómo obtuvimos el Cd? Para cada punto de Tracker —un par de tiempo y altura— despejamos Cd de la fórmula correspondiente. Luego promediamos todos los valores. Pero una medición sin incertidumbre no está completa: por eso también calculamos el error asociado a cada Cd. Mi compañero les explicará ese análisis.

**[5:30 - 6:00] Análisis de incertidumbre — parte conceptual**
La incertidumbre total tiene dos fuentes. La tipo A es estadística: como tenemos entre 580 y 1200 puntos, podemos calcular la desviación estándar de todos los Cd y dividirla por raíz de N. La tipo B es instrumental: ¿qué tan bien medimos el tanque y el orificio? Usamos regla de ±1 milímetro y calibre de ±0.05 milímetros. Propagamos esos errores a través de las fórmulas de Cd para cada geometría. El resultado se combina como raíz de uA al cuadrado más uB al cuadrado. Mi compañero les mostrará los números.

---

### Persona 3 — Resultados y Conclusiones (~4:00 min)

**[6:00 - 6:45] Resultados — gráficas**
Aquí vemos las cuatro gráficas. En cada una, la curva continua es el modelo teórico con el Cd que calculamos, y los puntos son los datos de Tracker. El ajuste es muy bueno en todos los casos: la teoría y el experimento coinciden cuando se usa el Cd correcto.

**[6:45 - 7:30] Tabla de Cd y tabla de incertidumbre**
Los valores obtenidos: para el tanque rectangular, el Cd del agua es 0.4164 y el del aceite 0.3983. Para la jarra, 0.5899 en agua y 0.4446 en aceite. Todos los Cd están por debajo del ideal de 0.62, porque nuestros orificios no son perfectos. El aceite siempre da un Cd menor que el agua por su mayor viscosidad. Y la jarra tiene un Cd más alto, indicando un mejor orificio.

Ahora miren la tabla de incertidumbre: en todos los casos uB —la instrumental— es diez veces mayor que uA —la estadística—. Por ejemplo, en el tanque cuadrado con agua, uA es 0.0011 pero uB es 0.0112. La incertidumbre combinada queda completamente dominada por qué tan bien medimos las dimensiones, no por cuántos datos tomamos. Dicho de otra forma: podríamos grabar el doble de video y no mejoraríamos casi nada; en cambio, un mejor calibre sí reduciría el error.

**[7:30 - 8:15] ¿Por qué este método y no el del volumen?**
Alguien podría preguntarse por qué no usamos el método más simple de recolectar el volumen descargado y dividir por el tiempo. Ese método da un solo valor de Cd y asume que la altura no cambia durante la medición, lo cual es falso. Nuestro enfoque con Tracker nos da cientos de puntos por experimento, no asume altura constante y nos permite hacer estadística real. Además eliminamos una fuente de error: ya no necesitamos medir el volumen recolectado.

**[8:15 - 9:00] Conclusiones**
Tres conclusiones. Una: el Cd no es un valor de libro; depende del montaje y hay que medirlo. Dos: Tracker es una herramienta muy efectiva para este tipo de experimentos. Tres: la mayor fuente de error no es estadística sino instrumental —la precisión de la regla y el calibre—. Si quisiéramos mejorar los resultados, convendría más usar instrumentos más precisos que grabar más video.

**[9:00 - 10:00] Cierre y preguntas**
En resumen, caracterizamos el coeficiente de descarga para dos geometrías y dos fluidos, validando el modelo de Torricelli cuando se incorpora el Cd experimental, y cuantificamos rigurosamente la incertidumbre asociada. Quedamos atentos a sus preguntas. Gracias.
