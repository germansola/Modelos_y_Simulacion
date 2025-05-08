#a) Desarrolle el método de la Transformada Inversa y el de Rechazo para generar una variable aleatoria
# X cuya distribución de probabilidad está dada por:
# P(X = i) =
# λ
# i
# i!
# e
# −λ
# k
# ∑
# j=0
# λ
# j
# j!
# e
# −λ
# (i = 0,..., k)
# b) Estime P(X > 2) con k = 10 y λ = 0,7, y 1000 repeticiones. Compare con el valor exacto.
# c) Generalice el problema escribiendo un pseudocódigo para el metodo de rechazo para cualquier variable aleatoria truncada usando como soporte a la variable original (con “cualquier variable aleatoria
# truncada” nos referimos a una variable como la vista en el inciso (a) pero ahora truncada en cualquier
# parte i = a,...,b).

import math
import numpy as np
from random import random
from time import time

from sympy.polys.benchmarks.bench_solvers import F_abc


def poisson(lamda):
    """
    Poisson sin optimizar del teorico
    """
    u = random()
    i = 0
    p = math.exp(-lamda)
    F = p
    while u >= F:
        i += 1
        p *= lamda / i
        F += p
    return i

# Comienza las funciones del ejercicio
#poisson sobre la poisson de todas las sumatorias hasta k
def PY(lamb,i):
    """
    P(Y=i)
    Es la funcion de masa de Poisson pmf
    :param lamb:
    :param i:
    :return:
    """
    p = math.exp(-lamb) #e^-lambda
    for j in range(1, i+1):
        p *= lamb / j
    return p

def sumatoria(lamb, k):
    """
    Constante que va en el denominador
    Es la funcion de distribucion acumulada de una Poisson cdf
    """
    p = math.exp(-lamb)
    S = p
    for j in range(1, k+1):
        p *= lamb / j
        S += p
    return S

#si yo ahora quiero agarrar el valor i-esimo de esta variable aleatoria teniendo en cuenta que sumo hasta cierto k

def PX(lamb, k, i):
    """
    P(X=i) (i=1, ..., k)
    :param lamb:
    :param k:
    :param i:
    :return:
    """
    return PY(lamb, i) / sumatoria(lamb, k)

def poisson_truncada(lamb,k):
    """
    Con transformada inversa
    :param lamb:
    :param k:
    :return:
    """
    u = random()
    i = 0
    S = sumatoria(lamb, k)
    p = math.exp(-lamb) / S
    F = p
    while u >= F:
        i += 1
        p *= lamb / i
        F += p
    return i

def poisson_truncada_mej(lamb,k):
    """
    Con transformada inversa mejorada
    :param lamb:
    :param k:
    :return:
    """
    S = sumatoria(lamb, k)
    p = math.exp(-lamb) / S
    F = p
    for j in range(min(int(lamb),k)):
        p *= lamb / j
        F += p
    j = int(lamb)
    u = random()
    if u < F:
        while u < F:
            F -= p
            p *= j / lamb
            j -= 1
        return j + 1
    else:
        while u >= F:
            j += 1
            p *= lamb / j
            F += p
    return j

def est_P(X, lamd, k, i, n_sim=100): # P(X>i)
    c = 0
    for _ in range(n_sim):
        r = X(lamd, k)
        if r > i:
            c += 1
    return c / n_sim

#ACEPTACION Y RECHAZO
def poisson_ayr(lamb, k):
    """
    Con el metodo de aceptacion y rechazo
    :param lamb:
    :param k:
    :return:
    """
    y = poisson(lamb)
    u = random()
    S = sumatoria(lamb, k)
    c = 1/S
    qy = PY(lamb, y)
    while u >= PX(lamb, k, y) / (c * qy):
        y = poisson(lamb)
        qy = PY(lamb, y)
        u = random()
    return y

def poisson_ayr_mej(lamb, k):
    while True:
        y = poisson(lamb)
        if y <= k:
            return y

print("Estimacion de P(X>2) con 1000 simulaciones")
print(f"T. Inversa:{est_P(poisson_truncada, 0.7, 10, 2, n_sim=1000)}")
print(f"T. Inversa MEJORADA:{est_P(poisson_truncada_mej, 0.7, 10, 2, n_sim=1000)}")
print("--------------------------------------------------------------------------------------")
print(f"Estimacion usando Aceptacion y Rechazo: {est_P(poisson_ayr, 0.7, 10, 2, n_sim=1000)}")
print(f"Metodo Mejorado: {est_P(poisson_ayr_mej, 0.7, 10, 2, n_sim=1000)}")
print("--------------------------------------------------------------------------------------------")
print(f"Valor exacto P(X>2) = {1 - (PX(0.7, k=10, i=0) + PX(0.7, k=10, i=1) + PX(0.7, k=10, i=2))}")

#Si quiero comparar el tiempo de corrida de las distintas funciones de Transf Inversa
print("--------------------------------------------------------------------------------------------")
start = time()
est_P(poisson_truncada, 0.7, 10, 2, n_sim=10000)
print(f"Tiempo de corrida comun: {time() - start:.5f}")
start = time()
est_P(poisson_truncada_mej, 0.7, 10, 2, n_sim=10000)
print(f"Tiempo de corrida mejorada: {time() - start:.5f}")
start = time()
est_P(poisson_ayr, 0.7, 10, 2, n_sim=10000)
print(f"Tiempo de corrida Aceptacion y Rechazo: {time() - start:.5f}")
start = time()
est_P(poisson_ayr_mej, 0.7, 10, 2, n_sim=10000)
print(f"Tiempo de corrida Aceptacion y Rechazo mejorado: {time() - start:.5f}")
