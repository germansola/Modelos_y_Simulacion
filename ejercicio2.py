#Se propone el siguiente juego en el cual todas las variables aleatorias que se generan son
#independientes e idénticamente distribuidas U(0,1): Se simula la variable aleatoria U. Si U <1/2, se suman
#dos nuevos números aleatorios W1 +W2. Pero si U ≥1/2, se suman tres números aleatorios. El resultado de
#la suma, en cualquiera de los casos, es una variable aleatoria X. Se gana en el juego si X ≥ 1.
#a) ¿Cuál es la probabilidad de ganar?.
#b) Implementar un algoritmo en computadora que estime la probabilidad de ganar, esto es, la fracción
#de veces que se gana en n realizaciones del juego. Completar la siguiente tabla:
#n 100 1000 10000 100000 1000000
#P[X ≥ 1]

#parte b)

import random

def juego(n):
    """
    Simula el juego descrito en el enunciado.
    n: número de simulaciones
    """
    ganadas = 0
    for _ in range(n):
        U = random.uniform(0, 1)
        if U < 0.5:
            W1 = random.uniform(0, 1)
            W2 = random.uniform(0, 1)
            X = W1 + W2
        else:
            W1 = random.uniform(0, 1)
            W2 = random.uniform(0, 1)
            W3 = random.uniform(0, 1)
            X = W1 + W2 + W3

        if X >= 1:
            ganadas += 1
    print(ganadas)
    return ganadas / n

# Probabilidades para diferentes valores de n
n_values = [100, 1000, 10000, 100000, 1000000]
probabilidades = {}
for n in n_values:
    probabilidad = juego(n)
    probabilidades[n] = probabilidad
    print(f"n={n}: P[X >= 1] = {probabilidad:.4f}")


def jugar() -> bool:
    """
    Se propone el siguiente juego en el cual todas las variables aleatorias que se generan son
    independientes e idénticamente distribuidas U(0,1): Se simula la variable aleatoria U. Si U <1/2,
    se suman dos nuevos números aleatorios W1 +W2. Pero si U >= 1/2, se suman tres números aleatorios.
    El resultado de la suma, en cualquiera de los casos, es una variable aleatoria X.
    Se gana en el juego si X ≥ 1.
    """

    w0 = random.random()
    w1 = random.random()
    w2 = random.random()
    w3 = random.random()

    if w0 < 0.5:
        x = w1 + w2
    else:
        x = w1 + w2 + w3

    return x >= 1


if __name__ == "__main__":

    # Ejercicio a:
    # ¿Cuál es la probabilidad de ganar?.
    # resuelto en notas

    # Ejercicio b:
    # Implementar un algoritmo en computadora que estime la probabilidad de ganar, esto es, la fracción
    # de veces que se gana en n realizaciones del juego

    for n in [100, 1000, 10000, 100000, 1000000]:
        wins = 0
        for i in range(n):
            wins = wins + 1 if jugar() else wins
        print(f"n={n:<12} wins={wins:<12} ratio={wins / n}")
