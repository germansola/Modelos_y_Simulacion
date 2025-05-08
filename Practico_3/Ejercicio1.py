from math import gcd as mcd
import math
#a) Determinar el periodo de la secuencia de von Neumann generada a partir de la semilla:

def periodo_von_neumann(x):
    contador = 1
    lista_generada = [x]
    for i in range(10000):
        x = (x**2 // 100) % 10000
        if x in lista_generada:
            break
        lista_generada.append(x)
        contador += 1
    return contador

print(periodo_von_neumann(3009))
print("---------------------")
print(periodo_von_neumann(7600))
print("---------------------")
print(periodo_von_neumann(1234))
print("---------------------")
print(periodo_von_neumann(4321))

#b) Dar el valor de c y de a para que cada generador tenga periodo maximo.
# yi+1 = 5yi +c mod´ (2^5), xi+1 = axi mod´ (31)
# considerar el generador zi = yi +xi mod´ (2^5) y calcular su período.
#Representar en tres gráficos separados pares (yi, yi+1), (xi, xi+1) y (zi,zi+1).
import matplotlib.pyplot as plt
import numpy as np
import random

def generador_nuevo(a, c):
    """
    Generador de números pseudoaleatorios utilizando un generador lineal congruencial
    Pueden cambiar y x por cualquier semilla que se les ocurra
    """
    y = 1
    x = 1
    z = (y + x) % 32
    ys = [y]
    xs = [x]
    zs = [z]

    for i in range(1000):
        y = (5 * y + c) % 32
        x = (a * x) % 31
        z = (y + x) % 32
        ys.append(y)
        xs.append(x)
        zs.append(z)

    return ys, xs, zs

# Test generador_nuevo
ys, xs, zs = generador_nuevo(12, 9)

# Graficar los resultados
plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
plt.plot(ys[:-1], ys[1:], 'o')
plt.title('yi vs yi+1')
plt.xlabel('yi')
plt.ylabel('yi+1')
plt.grid()
plt.subplot(1, 3, 2)
plt.plot(xs[:-1], xs[1:], 'o')
plt.title('xi vs xi+1')
plt.xlabel('xi')
plt.ylabel('xi+1')
plt.grid()
plt.subplot(1, 3, 3)
plt.plot(zs[:-1], zs[1:], 'o')
plt.title('zi vs zi+1')
plt.xlabel('zi')
plt.ylabel('zi+1')
plt.grid()
plt.tight_layout()
plt.show()

#c) Indicar en cuáles de los siguientes casos el generador
#yi+1 = ayi +c mod´ (M)
#genera una secuencia de período máximo.
#• a = 125, c = 3, M = 2^9
#• a = 123, c = 3, M = 2^9
#• a = 5, c = 0, M = 71
#• a = 7, c = 0, M = 71

def generador_congruencia_lineal_randMixto(a, y, c,m):
    """
    Dada una semilla, retorna ((a*y)+c) mod M
    """
    return (a*y+c) % m
print("\n")

print("c)")

def is_congruencial_periodo_maximo(a, c, m):
    """
    Determina si el generador congruencial tiene periodo máximo
    """

    def descomponer_en_primos(n):
        """
        Descompone un número en sus factores primos
        """
        factores = []
        for i in range(2, n + 1):
            while n % i == 0:
                factores.append(i)
                n //= i
        return factores

    # si el generador es multiplicativo (c = 0), entonces u nbuen generado no deberia alcanzar nunca el valor 0,
    # de lo contrario la secuencia degenaria e una sucesion infinita de ceros. Por lo tanto, para obtener un perido maximo,
    # esto es K=M, necesariamente debe ser un generador mixt
    #por lo tanto:
    if c == 0:
        return False
    # el maximo comun divisor entre c y M es 1: (c,M) = 1.
    if mcd(c, m) != 1:
        return False
    # a congruente 1 mod p, para cualquier factor primo p de M.
    for p in descomponer_en_primos(m):
        if (a % p) != 1:
            return False
    # Si 4 divide a M, entonces a congruente 1 mod 4.
    if (m % 4 == 0) and (a % 4 != 1):
        return False
    return True
# Test de los generadores
generadores = [
    (125, 3, 512),
    (123, 3, 512),
    (5, 0, 71),
    (7, 0, 71)
]
for a, c, m in generadores:
    if is_congruencial_periodo_maximo(a, c, m):
        print(f"El generador con a={a}, c={c}, M={m} tiene periodo máximo.")
    else:
        print(f"El generador con a={a}, c={c}, M={m} no tiene periodo máximo.")

print("\n")
print("d)")

def randu(a, M):
    x = 1
    lista = [x]
    for i in range(50000):
        x = (a * x) % M
        lista.append(x)
    
    return lista

a = 2**16+3 #7**5
M = 2**31 # 2 ** 31 - 1
lista = randu(a, M)

xs = lista[0::3]
ys = lista[1::3]
zs = lista[2::3]

# Plot 3D de los puntos generados con ternas (u_i, u_i+1, u_i+2)
# Rotarlo para encontrar los hiperplanos
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(xs, ys, zs, c='r', marker='o')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()

# Estimacion de puntos que entran en una esfera de radio M/10
# en el cubo de lado 
# Esto deberia darnos cercano a el cociente volumen de la esfera / volumen del cubo
contador = 0
for i in range(0, int(50001 / 3)):
    if (xs[i] - M / 2)**2 + (ys[i] - M / 2)**2 + (zs[i] - M / 2)**2 <= (M / 10)**2:
        contador += 1

print(f"Estimacion de puntos en la esfera: {contador / (50001 / 3)}")
print(4 * math.pi / 3000)
