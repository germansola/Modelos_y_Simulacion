#. Escriba un programa que calcule el número de eventos y sus tiempos de arribo en las primeras
#T unidades de tiempo de un proceso de Poisson homogéneo con parámetro λ.

from random import random
import math

def eventosPoisson(lamb, T):
    t = 0
    NT = 0
    Eventos = []
    while t < T:
        u = 1 - random()
        t += -math.log(u) / lamb
        if t <= T:
            Eventos.append(t)
            NT += 1
    return NT, Eventos

