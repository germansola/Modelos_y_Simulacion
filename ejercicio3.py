#Las máquinas tragamonedas usualmente generan un premio cuando hay un acierto. Supongamos que se genera el acierto con el siguiente esquema: se genera un número aleatorio, y
#i) si es menor a un tercio, se suman dos nuevos números aleatorios
#ii) si es mayor o igual a un tercio, se suman tres números aleatorios .
#Si el resultado de la suma es menor o igual a 2, se genera un acierto.
#a) ¿Cuál es la probabilidad de acertar?.
#b) Implementar un algoritmo en computadora que estime la probabilidad de acertar, esto es, la fracción
#de veces que se acierta en n realizaciones del juego. Completar la siguiente tabla:
#n 100 1000 10000 100000 1000000
#P[X ≤ 2]

#parte b)

import random
import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple

def tragamonedas(n: int) -> float:
    """
    Simula el juego de la tragamonedas.
    n: número de simulaciones
    """
    aciertos = 0
    for _ in range(n):
        U = random.uniform(0, 1)
        if U < 1/3:
            W1 = random.uniform(0, 1)
            W2 = random.uniform(0, 1)
            X = W1 + W2
        else:
            W1 = random.uniform(0, 1)
            W2 = random.uniform(0, 1)
            W3 = random.uniform(0, 1)
            X = W1 + W2 + W3

        if X <= 2:
            aciertos += 1

    return aciertos / n

# Probabilidades para diferentes valores de n
n_values = [100, 1000, 10000, 100000, 1000000]
probabilidades = {}
for n in n_values:
    probabilidad = tragamonedas(n)
    probabilidades[n] = probabilidad
    print(f"n={n}: P[X <= 2] = {probabilidad:.4f}")
# Graficar los resultados
plt.figure(figsize=(10, 6))
plt.plot(n_values, list(probabilidades.values()), marker='o')
plt.xscale('log')
plt.xlabel('Número de simulaciones (n)')
plt.ylabel('Probabilidad de acertar')
plt.title('Probabilidad de acertar en la tragamonedas')
plt.grid(True)
plt.xticks(n_values, rotation=45)
plt.show()
