#Estime P(Y > 2) con λ = 10, y 1000 repeticiones para la variable Poisson, simulando con
#método de transformada inversa común e inversa mejorado.

import random
from math import exp
import time
def poisson(lamda):
    u = random.random()
    i = 0
    p = exp(-lamda)
    F = p
    while u >= F:
        i += 1
        p *= lamda / i
        F += p
    return i

def poisson_mejorado(lamda):
    p = exp(-lamda)
    F = p
    for j in range(1, int(lamda)+1):
        p *= lamda / j
        F += p
    u = random.random()
    if u >= F:
        j = int(lamda)+1
        while u >= F:
            p *= lamda / j
            F += p
            j += 1
        return j-1

    j = int(lamda)
    while u < F:
        F -= p
        p *= j / lamda
        j -= 1
    return j+1

if __name__ == "__main__":
    print("ejercicio 07".center(100, " "))
    param = 10
    n_sim = 1_000
    for func in [poisson, poisson_mejorado]:
        cont = 0
        start = time.time()
        for _ in range(n_sim):
            sim = func(param)
            cont += int(sim > 2)
        print(f"{func.__name__}")
        print(f"\tP(X > 2)={cont/n_sim}")
        print(f"\ttime {time.time() - start}")
