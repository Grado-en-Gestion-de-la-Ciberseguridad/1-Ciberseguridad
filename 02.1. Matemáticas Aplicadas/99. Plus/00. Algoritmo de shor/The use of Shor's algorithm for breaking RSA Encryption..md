---
cssclasses:
  - justify
  - hbox
title: The use of Shor's algorithm for breaking RSA Encryption.
daft: "false"
tags:
---
#math #school #Trabajo-de-campo 
## RSA encryption:
- "lock data by using a large number and using the two factors of that large number to decrypt the data $N=p*q$"
RSA encryption is a widely used asymmetric cryptographic algorithm that enables secure communication and data protection over insecure channels, such as the Internet. It was invented in 1977 by Ron Rivest, Adi Shamir, and Leonard Adleman, and it derives its name from their initials.

Asymmetric encryption uses a pair of keys: a public key and a private key. The public key is used for encryption, while the private key is used for decryption. The keys are mathematically related in a way that makes it computationally infeasible to deduce the private key from the public key.
## Fourier Transform:
Fourier transform takes a signal, which can be a continuous function or a discrete set of data points, and decomposes it into its constituent frequencies. This transformation is useful in various fields, including signal processing, image processing, audio processing, communication systems, and quantum mechanics.
## Quantum  Fourier transform
the QFT operation takes all possible computational basis states and combines them with complex phase factors, creating interference patterns similar to the classical Fourier Transform. The probabilities of measuring each state in the output are determined by the constructive or destructive interference of the quantum amplitudes.
## Euclid´s algorithm:
The Euclidean algorithm is based on the principle that the greatest common divisor of two numbers does not change if the larger number is replaced by its difference with the smaller number. For example, $21$ is the GCD of $252$ and $105$ (as $252 = 21 × 12$ and $105 = 21 × 5$), and the same number $21$ is also the GCD of $105$ and $252 − 105 = 147$. Since this replacement reduces the larger of the two numbers, repeating this process gives successively smaller pairs of numbers until the two numbers become equal.
## Miller-Rabin primality test:
The Miller-Rabin primality test is a probabilistic algorithm used to determine whether a given number is likely to be prime or composite. It is based on the Miller-Rabin primality test, first proposed by Gary L. Miller in 1976 and later improved by Michael O. Rabin. The test is widely used in practice to efficiently check primality for large numbers.

## RSA encryption breaker based on Shor's algorithm for use in a normal computer:
The current method of breaking RSA encryption is by guessing the factors of N (the number used to encrypt data), by guessing the factors, and by guessing until you get it right.
This is done following these steps:
1.  we start by defining $N$  that you will need to find the two $f$ and $h$ factors to break the encryption.
2. you guess a number, for example, $f$, we don´t need $f$ to be a pure factor of $N$ it could be a number that shares a factor with $N$ since we can use Euclid´s algorithm and find the common factors, and if Euclid´s algorithm found a common factor you could divide N by the common factor to get the other factor and break the encryption, but the possibilities of these are less than 0.05%.
3. we will use a trick to transform our wrong guess "$f$" into two better guesses, by using this formula $f^{P\above{1pt}2}±1$, these formula is based on the mathematical fact that if you grab a pair of hole numbers "a and b" that don't share a factor and multiply one of them "a" by itself enough times you will arrive at "a=some hole number "m"* b +1"
**Demonstration**:
we get a=7 and b=15,

$7^2=3*15+4$ → does not follow $a^P=m*b+1$
$7^3=22*15+13$ → does not follow $a^P=m*b+1$
$7^4=160*15+1$ → $a^P=m*b+1$

so in our example with our number $N$ and or guess $f$ we are guaranteed that $f^P=m*N+1$ if you subtract the 1 from both sides which can be rewritten as $(f^{P\above{1pt}2}+1)*(f^{P\above{1pt}2}-1)=m*N$ which looks a lot more like $N=f*h$. so $(f^{P\above{1pt}2}±1)$ are the new and improved guesses. but since we are dealing with multiple of  $N$ "$m*N$" the terms on the right sides might be multiples of the factors of N but we can use Euclid's algorithm to find the como factors.

**Demonstration**: "following the previous demonstration N=15"
$7^{4\above{1pt}2}+1=50$
$7^{4\above{1pt}2}+1=48$
Neither of these is a factor of 15, but we can find the common factors by using Euclid's algorithm, by which we find 5 and 3
#### but this process has three main problems:
1. one of our guesses might be a multiple of N in which case the other would be a factor of $m$ , which would make both guesses unusable
2.  the power of $p$ might be an odd number in which case we would get a fraction, which is no good since we need hole numbers.
for 37.5% of the time these problems do not happen, which allows for valid guesses that can break the encryption, making it possible to breach the encryption 99% of the time with fewer than 10 tries.
3. now the largest problem is finding $p$ so that we can find a multiple of N+1 ($f^P=m*N+1$) , with normal computational power is the part that takes a long time and energy, more than directly trying to guess N, since in reality the number N is composed of a 1000 digits, unlike in our example were its made out of 2 digits.

# Shor's algorithm in quantum computers
Now this is where Quantum computation makes this problem of finding p null, unlike normal computation which gives only one answer for a given input, a quantum computation can simultaneously calculate a lot of possible answers for a single input by using a quantum superposition while all of the wrong answers destructively interfere with each other, these are were Shor's algorithm comes in handy, here is how:

at these point we have mage a guess $g$ and we are traying to find $p$ so that $g^p=m*N+1$, were a $p$  that follows that is really likely to share factors with $N$
$$ g→ p→ g^{P\above{1pt}2}±1$$

This is where we set up a quantum computer that takes a number "$x$" as input and rises $g$ to the power of $x$ "$g^x$" and then calculates how much bigger of a multiple of N it is.
$$
|x> → |g^x|→ |x,g^x> → |>m*N|→|x,+r>
$$
here is where it differs from a normal computer, since there is a quantum computer we can input a superposition of numbers that our guess could be raised to and then check how much bigger each of the power is than a multiple of $N$
$$
|1>+|2>+|3>+... →|g^x|→ |1,g^1>+|2,g^2>+|3,g^3>+...→|m*N|→|1,+17>+|2,+5>+|3,+92>+...
$$
we can't just measure this superposition to get the answer since we would get a single random element of the superposition, so we have to get all of the non $p$ answers to destructively interfere and cancel out living us with only $p$, these can be done by another mathematical observation.
$$
g^x=m*n+r → g^{x+p}=m_2*N+r 
$$
**Demonstration:**
$$g^p=m*N+1$$
$$↓$$
$$g^{42}=m_1*N+3$$
$$↓$$
$$g^{42+p}=m_2*N+3$$
$$↓$$
$$g^{42+2p}=m_3*N+3$$
$$↓$$
<p style="text-align: center;">these continues infinitely</p>
$$g^{p+42}=g^p*g^{42}=(m*N+1)(m_1*N+3)$$

⚠️ these shows the repeating property of $p$, were if we take another power"$x$" and add or subtract $p$ the amount more than a multiple of $N$ "$+r$" will be the same. So if we do the superposition measuring only the amount more than a multiple of $N$, we will get a  random amount more than a multiple of $N$ as the output , let's say "$+3$" , this means that we will be left with a superposition of only the powers that could have left a remainder "$r$" of $3$:
$$
|2,+3>+|12,+3>+|22,+3>+...
$$
from these we can observe that they repeat with a frequency of ${1\above{1pt}p}$, here we can use **Quantum Fourier Transform** to calculate the frequency of  ${1\above{1pt}p}$
This is done by inputting the superposition that we are left with, and the Quantum Fourier Transform will transform them into waves that will interfere with each other resulting in the quantum state of ${1\above{1pt}p}$, which can be inverted to find $p$ , and if $p$ is even we calculate $g^{P\above{1pt}2}±1$, and as long as we don't get a exact multiple of $N$, we are guaranteed to get a number that shares factors with $N$, and therefore we can use  Euclid´s algorithm to find the factors and be able to decrypt the data

https://youtu.be/lvTqbM5Dq4Q?t=554
____
## "RSA" Encryption:
RSA (Rivest-Shamir-Adleman) is a widely used cryptographic algorithm for encryption and decryption, named after its inventors. It relies on the mathematical properties of large prime numbers to provide secure communication over insecure channels. Here's a brief summary of how RSA encryption and decryption work:

1. Key Generation:
    
    - Choose two distinct large prime numbers, p and q.
    - Compute the modulus $n = p * q$.
    - Compute Euler's totient function $φ(n) = (p - 1) * (q - 1)$.
    - Select a public exponent e, which is typically a small prime, such as $65537 (2^16 + 1)$
    - or 3. e must be greater than 1 and less than φ(n).
    - Calculate the private exponent d, which is the modular multiplicative inverse of e modulo $φ(n$). In other words, $(e * d) mod φ(n) = 1$.
2. Encryption:
    
    - Convert the plaintext message into a numerical representation M, where M is an integer such that 0 < M < n.
    - Use the recipient's public key (n, e) to encrypt the message.
    - Calculate the ciphertext C ≡ M^e (mod n), where "^" represents exponentiation and "mod" is the modulus operation.
3. Decryption:
    
    - The recipient uses their private key (n, d) to decrypt the ciphertext C.
    - Calculate the original message M ≡ C^d (mod n), where "^" represents exponentiation and "mod" is the modulus operation.

It's important to note that the security of RSA relies on the difficulty of factoring large composite numbers (n) into their prime factors (p and q). As long as the primes are large enough, the algorithm is secure against brute-force attacks.

RSA is widely used for secure communication and digital signatures, making it a fundamental component of modern cryptographic systems. However, it can be computationally intensive, especially for very large numbers, and alternative cryptographic algorithms like Elliptic Curve Cryptography (ECC) are also commonly used to address these computational challenges.


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
- https://sites.math.washington.edu/~morrow/336_16/2016papers/tristan.pdf | [[Algoritmo de shor/Documents/Quantum Computing and Shor’s Algorithm.pdf|Quantum Computing and Shor’s Algorithm]]
- [[Algoritmo de shor/Documents/Shor's_algorithms.pdf|Shor's_algorithms]]
- 