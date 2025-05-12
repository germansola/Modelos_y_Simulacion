from random import random
from random import uniform
import math
import time


#transformada inversa
def X_TI():
    return math.e**random()

#aceptacion y rechazo
def X_AR():
    while True:
        y = uniform(1, math.e)
        u = random()
        if u < 1/y:
            return y

def sim(X, nsim):
    start = time.time()
    for i in range(nsim):
        X()
    end = time.time()
    return (end-start)/nsim
print("Metodo de Aceptacion y Rechazo: \n Tiempo:", sim(X_AR, 100000) * 10000000, "ms")
print("Metodo de Transformada Inversa: \n Tiempo:", sim(X_TI, 100000) * 10000000, "ms")

def est_E(X, nsim):
    p = 0
    for _ in range(nsim):
        p += X()
    return p/nsim

print("Estimación de la Esperanza con 100000 simulaciones:")
print("Metodo de Aceptacion y Rechazo: \n E(X):", est_E(X_AR, 100000))
print("Metodo de Transformada Inversa: \n E(X):", est_E(X_TI, 100000))

def est_P(X, k, nsim): # P(X <= k)
    p = 0
    for _ in range(nsim):
        r = X()
        if r <= k:
            p += 1
    return p/nsim

print("Estimación de P(X<=2) con 100000 simulaciones:")
print("Metodo de Aceptacion y Rechazo: \n P(X<=2):", est_P(X_AR, 2, 100000))
print("Metodo de Transformada Inversa: \n P(X<=2):", est_P(X_TI, 2, 100000))

