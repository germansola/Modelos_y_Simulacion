import time
from random import random
from random import uniform
import math
import numpy as np
def f_x(x):
    if 0 <= x <= 1:
        return x
    elif 1 <= x < 2:
        return 2 - x
    return 0

def suma_uniformes():
    return random() + random()



#transformada inversa
def X_TI():
    u = random()
    if u <= 1/2:
        return math.sqrt(2*u)
    else:
        return 2 - (math.sqrt(2)*math.sqrt(1-u))

#aceptacion y rechazo

def g_x(x):
    return 1/2 # 1/b-a

def aceptacion_rechazo():
    c = 2
    while True:
        y = uniform(0, 2)
        u = random()
        if u < f_x(y) / (c * g_x(y)):
            return y


#Compare la eficiencia de los tres algoritmos. Para cada caso, estimar el valor esperado promediando
#10.000 valores simulados, ¿Para qué valor x0 se cumple que P(X > x0) = 0.125?


def sim(X, nsim):
    start = time.time()
    for i in range(nsim):
        X()
    end = time.time()
    return (end-start)/nsim
print("Metodo de Aceptacion y Rechazo: \n Tiempo:", sim(aceptacion_rechazo, 100000) * 10000000, "ms")
print("Metodo de Transformada Inversa: \n Tiempo:", sim(X_TI, 100000) * 10000000, "ms")
print("Metodo de Suma de Uniformes: \n Tiempo:", sim(suma_uniformes, 100000) * 10000000, "ms")

def est_E(X, nsim):
    p = 0
    for _ in range(nsim):
        p += X()
    return p/nsim
print("Estimación de la Esperanza con 100000 simulaciones:")
print("Metodo de Aceptacion y Rechazo: \n E(X):", est_E(aceptacion_rechazo, 100000))
print("Metodo de Transformada Inversa: \n E(X):", est_E(X_TI, 100000))
print("Metodo de Suma de Uniformes: \n E(X):", est_E(suma_uniformes, 100000))

#d) Compare la proporción de veces que el algoritmo devuelve un número mayor que x0=3/2 con esta probabilidad.

def est_P(X, k, nsim): # P(X > x0)
    p = 0
    for _ in range(nsim):
        r = X()
        if r > k:
            p += 1
    return p/nsim

print("Estimación de P(X>3/2) con 100000 simulaciones:")
print("Metodo de Aceptacion y Rechazo: \n P(X>3/2):", est_P(aceptacion_rechazo, 3/2, 100000))
print("Metodo de Transformada Inversa: \n P(X>3/2):", est_P(X_TI, 3/2, 100000))
print("Metodo de Suma de Uniformes: \n P(X>3/2):", est_P(suma_uniformes, 3/2, 100000))




x0 = 1.5

# Calcular la proporción de veces que X > x0 para cada método
def proporciones(nsim):
    p1 = 0
    p2 = 0
    p3 = 0
    for _ in range(nsim):
        r1 = aceptacion_rechazo()
        r2 = X_TI()
        r3 = suma_uniformes()
        if r1 > x0:
            p1 += 1
        if r2 > x0:
            p2 += 1
        if r3 > x0:
            p3 += 1
    return p1/nsim, p2/nsim, p3/nsim
proporciones = proporciones(100000)
print("Proporción de veces que X > 3/2:")
print("Metodo de Aceptacion y Rechazo: \n P(X>3/2):", proporciones[0])
print("Metodo de Transformada Inversa: \n P(X>3/2):", proporciones[1])
print("Metodo de Suma de Uniformes: \n P(X>3/2):", proporciones[2])
