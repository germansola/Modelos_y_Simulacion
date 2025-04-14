#Es posible aproximar el valor de π calculando el área de un círculo de radio 1 centrado en 0.
#Para eso, se necesitan generar N puntos aleatorios en la caja [−1,1]×[−1,1] y contar la cantidad de veces
#que los mismos caen dentro del círculo. El cociente entre este número y N, multiplicado por 4 (el área del
#cuadrado donde está contenido el círculo) es una aproximación de π.
#Completar la siguiente tabla con los valores obtenidos para distintos N y compararlos con numpy.pi o
#math.pi:
#n π
#1000
#10000
#100000

import random
import math
import numpy as np

def valorPi(nSim):
    enCirculo = 0
    for _ in range(nSim):
        u = 2 * random.uniform(0, 1) - 1
        v = 2 * random.uniform(0, 1) - 1
        if u**2 + v**2 <= 1:
            enCirculo += 1
    return 4 * enCirculo / nSim

# Probabilidades para diferentes valores de n
n_values = [1000, 10000, 100000]
probabilidades = {}
for n in n_values:
    probabilidad = valorPi(n)
    probabilidades[n] = probabilidad
    # Comparar con el valor de pi de numpy
    pi_numpy = np.pi
    pi_math = math.pi
    print(f"n={n}: π ≈ {probabilidad:.6f} (numpy.pi: {pi_numpy:.6f}, math.pi: {pi_math:.6f})")
    print(f"n={n}: π ≈ {probabilidad:.4f} (error: {abs(probabilidad - math.pi):.4f})")
