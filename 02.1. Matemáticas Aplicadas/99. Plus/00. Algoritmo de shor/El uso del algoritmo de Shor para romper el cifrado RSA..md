---
cssclasses:
  - justify
  - hbox
title: El uso del algoritmo de Shor para romper el cifrado RSA.
daft: "false"
tags:
---
#math #school #Trabajo-de-campo 
## RSA encryption:
- "Encripta datos utilizando un número grande y los dos factores de ese número grande para desencriptar los datos $N=p*q$."

La encriptación RSA es un algoritmo criptográfico asimétrico ampliamente utilizado que permite la comunicación segura y la protección de datos en canales inseguros, como Internet. Fue inventado en 1977 por Ron Rivest, Adi Shamir y Leonard Adleman, y su nombre proviene de sus iniciales.
El cifrado asimétrico utiliza un par de claves: una clave pública y una clave privada. La clave pública se utiliza para encriptar, mientras que la clave privada se utiliza para desencriptar. Las claves están relacionadas matemáticamente de tal manera que es computacionalmente inviable deducir la clave privada a partir de la clave pública.

RSA se utiliza amplia mente para la comunicación segura y firmas digitales, lo que lo convierte en un componente fundamental de los sistemas criptográficos modernos. Sin embargo, puede ser computacionalmente intensivo, especialmente para números muy grandes, y también se utilizan comúnmente algoritmos criptográficos alternativos como la Criptografía de Curva Elíptica (ECC) para abordar estos desafíos computacionales.

## Algoritmo de Shor:
El algoritmo de Shor es un algoritmo cuántico desarrollado por Peter Shor en 1994. Su principal aplicación es factorizar números enteros grandes de manera eficiente, lo que tiene implicaciones significativas en la criptografía. El algoritmo de Shor utiliza propiedades de la computación cuántica, como la superposición y la interferencia, para encontrar los factores primos de un número compuesto mucho más rápido que los algoritmos clásicos. Esto puede comprometer sistemas criptográficos basados en la factorización de números enteros, como el cifrado RSA. En resumen, el algoritmo de Shor es un avance importante en la informática cuántica con importantes implicaciones en la seguridad de la información.

## Transformada de Fourier:
La transformada de Fourier toma una señal, que puede ser una función continua o un conjunto discreto de puntos de datos, y la descompone en sus frecuencias constituyentes. Esta transformación es útil en varios campos, incluyendo el procesamiento de señales, procesamiento de imágenes, procesamiento de audio, sistemas de comunicación y mecánica cuántica.

## Transformada cuántica de Fourier:
La operación QFT toma todos los posibles estados de base computacional y los combina con factores de fase complejos, creando patrones de interferencia similares a la Transformada de Fourier clásica. Las probabilidades de medir cada estado en la salida están determinadas por la interferencia constructiva o destructiva de las amplitudes cuánticas.

## Algoritmo de Euclides:
El algoritmo de Euclides se basa en el principio de que el máximo común divisor de dos números no cambia si el número más grande se reemplaza por su diferencia con el número más pequeño. Por ejemplo, $21$ es el máximo común divisor de $252$ y $105$ (ya que $252 = 21 × 12$ y $105 = 21 × 5$), y el mismo número $21$ también es el máximo común divisor de $105$ y $252 − 105 = 147$. Repitiendo este proceso conduce a pares de números cada vez más pequeños hasta que los dos números se vuelven iguales.

## Test de primalidad de Miller-Rabin:
El test de primalidad de Miller-Rabin es un algoritmo probabilístico utilizado para determinar si un número dado es probablemente primo o compuesto. Está basado en el test de primalidad de Miller-Rabin, propuesto por Gary L. Miller en 1976 y posteriormente mejorado por Michael O. Rabin. El test se utiliza ampliamente en la práctica para verificar la primalidad de números grandes de manera eficiente.

## Desencriptador de RSA basado en el algoritmo de Shor para su uso en una computadora normal:
El método actual para desencriptar RSA es adivinando los factores de $N$ (el número utilizado para encriptar datos), adivinando los factores y repitiendo hasta que se acierte.

Esto se hace siguiendo estos pasos:
1. Empezamos definiendo $N$, del que necesitaremos encontrar los dos factores $f$ y $h$ para desencriptar los datos.
2. Elegimos un numero aleatorio un número, por ejemplo, $f$. No necesitamos que $f$ sea un factor puro de $N$; podría ser un número que comparta un factor con $N$, ya que podemos usar el algoritmo de Euclides para encontrar los factores comunes, y si el **[[#Algoritmo de Euclides]]** encuentra un factor común, podríamos dividir N por el factor común para obtener el otro factor y desencriptar los datos. Sin embargo, las posibilidades de que esto suceda son inferiores al 0,005%.
3. Utilizaremos una formula matematica para transformar nuestra suposición incorrecta "$f$" en dos suposiciones mejores, utilizando esta fórmula $f^{P\above{1pt}2}±1$. Esta fórmula se basa en el hecho matemático de que si tomas un par de números enteros "a y b" que no comparten un factor y multiplicas uno de ellos "a" por sí mismo suficientes veces "$P$", llegarás a "$a^P = m* b +1$", donde $m$ es un número entero

Demostración: Tomamos a=7 y b=15,
$7^2=3*15+4$ → no sigue la forma $a^P=m*b+1$
$7^3=22*15+13$ → no sigue la forma $a^P=m*b+1$
$7^4=160*15+1$ → $a^P=m*b+1$

Por lo tanto, en nuestro ejemplo con nuestro número N y nuestra suposición $f$, estamos garantizados que $f^P=m*N+1$. Si restamos $1$ de ambos lados, se puede reescribir como $(f^{P\above{1pt}2}+1)*(f^{P\above{1pt}2}-1)=m*N$, que se parece mucho a $N=f*h$. Por lo tanto, $(f^{P\above{1pt}2}±1)$ son las nuevas y mejoradas suposiciones. Pero como estamos tratando con múltiplos de N "$m*N$", los términos en los lados podrían ser múltiplos de los factores de N, pero podemos usar el **[[#Algoritmo de Euclides]]** para encontrar los factores comunes.

Demostración: "siguiendo la demostración anterior, P=4"
$7^{4\above{1pt}2}+1=50$
$7^{4\above{1pt}2}-1=48$
Ninguno de estos es un factor de 15, pero podemos encontrar los factores comunes utilizando el algoritmo de Euclides, y así encontramos 5 y 3.

Pero este proceso tiene tres problemas principales:
1. Una de nuestras suposiciones podría ser un múltiplo de $N$, en cuyo caso la otra sería un factor de $m$, lo que haría que ambas suposiciones fueran inútiles.
2. La potencia de $p$ podría ser un número impar, en cuyo caso obtendríamos una fracción, que no es útil ya que necesitamos números enteros.
3. El problema más grande es encontrar $p$ para poder encontrar un múltiplo de N+1 ($f^P=m*N+1$). Con el poder computacional normal, esta parte requiere mucho tiempo y energía, más que intentar adivinar N directamente, ya que en realidad el número N está compuesto por 1000 dígitos, a diferencia de nuestro ejemplo en el que tiene solo 2 dígitos.

# Algoritmo de Shor en Ordenadores cuánticos
Aquí es donde la computación cuántica hace que este problema de encontrar $P$ sea nulo. A diferencia de la computación normal, que solo proporciona una respuesta para una entrada dada, una computadora cuántica puede calcular simultáneamente muchas respuestas posibles para un solo numero utilizando una superposición cuántica, mientras que todas las respuestas incorrectas interfieren destructivamente entre sí. Aquí es donde entra en juego el algoritmo de Shor, así es cómo funciona:

En este punto, hemos hecho una suposición g y estamos tratando de encontrar p para que $g^p=m*N+1$, donde p que sigue esa propiedad es muy probable que comparta factores con N.
$$ g→ p→ g^{P\above{1pt}2}±1$$
Aquí es donde configuramos una computadora cuántica que toma un número "$x$" como entrada y eleva $g$ a la potencia de $x$ "$g^x$" y luego calcula cuántas veces N es un múltiplo más grande de lo que obtuvimos.
$$
|x> → |g^x|→ |x,g^x> → |>m*N|→|x,+r>
$$
Aquí es donde difiere de un ordenador normal, ya que con un ordenador cuántico podemos ingresar una superposición de números a los que podría elevarse nuestra suposición, y luego verificar cuánto más grande es cada potencia que un múltiplo de $N$.
$$
|1>+|2>+|3>+... →|g^x|→ |1,g^1>+|2,g^2>+|3,g^3>+...→|m*N|→|1,+17>+|2,+5>+|3,+92>+...
$$
No podemos medir simplemente esta superposición para obtener la respuesta, ya que obtendríamos un solo elemento aleatorio de la superposición. Entonces, tenemos que obtener todas las respuestas no $p$ para que interfieran destructivamente y se cancelen, dejándonos solo con $p$. Esto se puede hacer mediante otra observación matemática.
$$
g^x=m*n+r → g^{x+p}=m_2*N+r 
$$
Demostración:
$$g^p=m*N+1$$
$$↓$$
$$g^{42}=m_1*N+3$$
$$↓$$
$$g^{42+p}=m_2*N+3$$
$$↓$$
$$g^{42+2p}=m_3*N+3$$
$$↓$$
<p style="text-align: center;">Esto continúa infinitamente</p>

$$g^{p+42}=g^p*g^{42}=(m*N+1)(m_1*N+3)$$

⚠️ Esto muestra la propiedad repetitiva de p, donde si tomamos otro poder "$x$" y sumamos o restamos p, la cantidad más grande que un múltiplo de $N$ "$+r$" será la misma. Entonces, si hacemos la superposición midiendo solo la cantidad más grande que un múltiplo de $N$, obtendremos una cantidad aleatoria más grande que un múltiplo de $N$ como resultado, por ejemplo, "$+3$", lo que significa que nos quedará una superposición de solo las potencias que podrían haber dejado un residuo "$r$" de $3$:
$$
|2,+3>+|12,+3>+|22,+3>+...
$$
A partir de esto, podemos observar que se repiten con una frecuencia de ${1\above{1pt}p}$. Aquí es donde podemos usar la **[[#Transformada cuántica de Fourier]]** para calcular la frecuencia de ${1\above{1pt}p}$. 

Esto se logra ingresando la superposición que nos queda, y la **[[#Transformada cuántica de Fourier]]** la transformará en ondas que interferirán entre sí de una forma destructiva, lo que resultará en el estado cuántico de ${1\above{1pt}p}$, podemos invertir esto para encontrar p, y si p es par, calculamos $g^{P\above{1pt}2}±1$, y siempre y cuando no obtengamos un múltiplo exacto de $N$, estamos garantizados de obtener un número que comparte factores con N, y por lo tanto podemos usar el **[[#Algoritmo de Euclides]]** para encontrar los factores y desencriptar los datos.
____
# Citations:
- Skosana, U., & Tame, M. (2021). Demonstration of Shor’s factoring algorithm for N 21 on IBM quantum processors. _Scientific Reports_, _11_(1). https://www.nature.com/articles/s41598-021-95973-w.pdf?pdf=button%20sticky
- GeeksforGeeks. (2023). RSA Algorithm in Cryptography. _GeeksforGeeks_. https://www.geeksforgeeks.org/rsa-algorithm-cryptography/
- Tyson, M. (2022, February 24). _Understand the RSA encryption algorithm_. InfoWorld. https://www.infoworld.com/article/3650488/understand-the-rsa-encryption-algorithm.html
- _Cracking short RSA keys_. (n.d.). Stack Overflow. https://stackoverflow.com/questions/4078902/cracking-short-rsa-keys
- Blanda, V. a. P. B. S. (2014, April 30). _Shor’s Algorithm – Breaking RSA Encryption |_. https://blogs.ams.org/mathgradblog/2014/04/30/shors-algorithm-breaking-rsa-encryption/
- Qiskit. (2021, July 2). _The Story of Shor’s Algorithm, Straight From the Source | Peter Shor_ [Video]. YouTube. https://www.youtube.com/watch?v=6qD9XElTpCE
- _Shor’s algorithm - IBM Quantum_. (n.d.). IBM Quantum. https://quantum-computing.ibm.com/composer/docs/iqx/guide/shors-algorithm
- Sahil-4555/RSA-Encryption: (n.d.). GitHub. https://github.com/Sahil-4555/RSA-Encryption (base para el script de python)
- Qiskit. (2020, September 1). _10. Shor’s algorithm II: From Factoring to Period-Finding, Writing the Quantum Program - Part 1_ [Video]. YouTube. https://www.youtube.com/watch?v=YpcT8u2a2jc
- Qiskit. (2020, September 1). _11. Shor’s algorithm II: From Factoring to Period-Finding, Writing the Quantum Program - Part 2_ [Video]. YouTube. https://www.youtube.com/watch?v=dscRoTBPeso




