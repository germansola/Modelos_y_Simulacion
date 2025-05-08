from random import random
import numpy as np

#¿Qué distribución tiene la variable simulada por el siguiente algoritmo?
def QueDevuelve(p1,p2):
    X = int(np.log(1-random())/np.log(1-p1))+1
    Y = int(np.log(1-random())/np.log(1-p2))+1
    return min(X,Y)

print(f"QueDevuelve del enunciado: {QueDevuelve(0.05, 0.2)}")

#Escriba otro algoritmo que utilice un único número aleatorio (random()) y que simule una variable con
#la misma distribución que la simulada por QueDevuelve(0.05, 0.2).

def geometrica(p):
    """
    Genera una variable aleatoria X con distribución geométrica de parámetro p.
    """
    u = 1 - random()
    return int(np.log(u) / np.log(1 - p)) + 1

p0 = 1 - (1-0.05) * (1-0.2)
print(f"Nuevo algoritmo con la distribucion obtenida (Geometrica):{geometrica(p0)}")

def est_E(X, p, nsim):
    e = 0
    for _ in range(nsim):
        e += X(p)
    return e/nsim
def est_E2(X, p1,p2, nsim):
    e = 0
    for _ in range(nsim):
        e += X(p1, p2)
    return e/nsim
print(f"Esperanza de la variable QueDevuelve: {est_E2(QueDevuelve, 0.05, 0.2, 10000)}")
print(f"Esperanza de la variable geometrica: {est_E(geometrica, p0, 10000)}")
print("Esperanza teorica de la geometrica: ", 1/p0)

