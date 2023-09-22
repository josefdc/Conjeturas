
# Repositorio de Conjeturas Matemáticas 🧮✨

Este repositorio contiene implementaciones y simulaciones relacionadas con famosas conjeturas matemáticas. A continuación, se presenta una breve descripción de cada conjetura y su respectivo archivo.

## Conjetura de Collatz 🌀

La Conjetura de Collatz, también conocida como la conjetura 3n + 1, es un problema sin resolver en matemáticas que ha intrigado y confundido a matemáticos durante muchos años. Se relaciona con secuencias definidas a partir de cualquier número entero positivo inicial.

### Historia y Origen
La Conjetura de Collatz, también conocida por otros nombres, es un enigma en el área de las matemáticas propuesto por primera vez en 1937 por el matemático alemán Lothar Collatz.

### Descripción Detallada
1. Comienza con cualquier número entero positivo \( n \).
2. Si \( n \) es par, divídelo por 2 (\( n/2 \)).
3. Si \( n \) es impar, multiplica por 3 y suma 1 (\( 3n + 1 \)).
4. Repite el proceso hasta llegar a 1.

La conjetura sostiene que siempre llegarás al número 1, sin importar con qué número entero positivo comiences.

### Curiosidades
- Aunque ha sido probada para números grandes, aún no se ha probado ni refutado para todos los números enteros positivos.
- El matemático Paul Erdős comentó sobre la conjetura: "Las matemáticas no están aún listas para enfrentar problemas tan complicados".
- Hay secuencias que son especialmente largas antes de llegar a 1. Por ejemplo, el número 27 toma 111 pasos y pasa por 9232 antes de reducirse a 1.

- Archivo relacionado: [collatz_conjecture.py](collatz_conjecture.py)

## Conjetura de Birch y Swinnerton-Dyer 🌐

La **Conjetura de Birch y Swinnerton-Dyer** es una de las conjeturas más intrigantes en la teoría de números. En esencia, relaciona propiedades de las curvas elípticas (un tipo especial de curvas) con la cantidad de soluciones que estas pueden tener.

### Historia y Origen

La conjetura lleva el nombre de Bryan Birch y Peter Swinnerton-Dyer, quienes, en la década de 1960, utilizando computadoras tempranas, observaron un patrón interesante entre ciertas curvas elípticas y sugirieron que podría ser cierto para todas ellas. Esta observación llevó a la formulación de la conjetura.

### Descripción Detallada

Imagínate una curva con una ecuación especial en un plano. Ahora, imagina que estás buscando puntos específicos en esa curva que cumplan ciertas propiedades (puntos racionales). La **Conjetura de Birch y Swinnerton-Dyer** sugiere que hay una relación entre la cantidad de estos puntos especiales y ciertas características de la función matemática asociada a la curva.

Si bien esto puede sonar abstracto, el descubrimiento de esta relación potencial ha sido fundamental en la teoría de números y ha llevado a una profunda investigación en el campo.

### Importancia

Las curvas elípticas no solo son importantes en la teoría de números, sino que también juegan un papel crucial en áreas como la criptografía, donde ayudan a proteger la información en internet.

La **Conjetura de Birch y Swinnerton-Dyer** es tan significativa que se ha incluido en la famosa lista de **Problemas del Milenio**, cuya solución conlleva un premio de un millón de dólares.

### Curiosidades

- Aunque se han demostrado algunos casos especiales, la conjetura en su totalidad sigue siendo un misterio.
- El matemático Andrew Wiles, conocido por resolver el Último Teorema de Fermat, también ha trabajado en problemas relacionados con curvas elípticas.

- Archivo relacionado: [elliptic_curve.py](elliptic_curve.py)


## Conjetura de Kepler 🍊
Propuesta por Johannes Kepler en 1611, esta conjetura afirma que la forma más eficiente de apilar esferas es la disposición que comúnmente vemos en los supermercados. Fue verificada computacionalmente y finalmente demostrada en 2017.
- Archivo relacionado: [fcc_packing_simulation.py](fcc_packing_simulation.py)

## Conjetura de los Números Primos Gemelos 👥
Esta conjetura sostiene que existen infinitos números primos p tales que p + 2 también es primo. Estos pares se conocen como "primos gemelos".
- Archivo relacionado: [twin_primes.py](twin_primes.py)

---

Espero que encuentres este repositorio útil e intrigante. ¡Disfruta explorando el maravilloso mundo de las conjeturas matemáticas! 🌟
