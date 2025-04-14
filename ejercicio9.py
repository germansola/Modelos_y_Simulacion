#Un juego consiste en dos pasos. En el primer paso se tira un dado convencional. Si sale 1 o
#6 tira un nuevo dado y se le otorga al jugador como puntaje el doble del resultado obtenido en esta nueva
#tirada; pero si sale 2, 3, 4 o 5 en la primer tirada, el jugador debería tirar dos nuevos dados, y recibiría como
#puntaje la suma de los dados. Si el puntaje del jugador excede los 6 puntos entonces gana.
#a) Realizar un cálculo teórico de la probabilidad de que un jugador gane.
#b) Estime la probabilidad de que un jugador gane mediante una simulación.

# parte b

from random import randint
import numpy as np

def juego_simulacion(nsim):
    p = 0
    for i in range(nsim):
        n = randint(1, 6)
        if n == 1 or n == 6:
            x = 2 * randint(1, 6)
            if x > 6:
                p += 1
        else:
            x = randint(1, 6) + randint(1, 6)
            if x > 6:
                p += 1
    return p / nsim
# Probabilidades para diferentes valores de n
n_values = [100, 1000, 10000, 100000]
probabilidades = {}
for n in n_values:
    probabilidad = juego_simulacion(n)
    probabilidades[n] = probabilidad
    print(f"n={n}: P[X > 6] = {probabilidad:.4f}")
    print(f"n={n}: P[X > 6] = {probabilidad:.4f} (error: {abs(probabilidad - 0.5):.4f})")
