# Implemente dos métodos para simular una variable geométrica Geom(p):
# a) Usando transformada inversa y aplicando la fórmula recursiva para P(X = i).
from random import random
import time
import numpy as np
def geometrica_transformada_inversa(p):
    """
    Genera una variable aleatoria X con distribución geométrica de parámetro p usando transformada inversa.
    """
    u = random()
    return int(np.log(1 - u) / np.log(1 - p)) + 1

def geometrica_rec(p):
    u = random()
    i = 1
    prob = p
    F = prob
    while u >= F:
        i += 1
        prob *= (1 - p)
        F = F + prob
    return i

# b) Simulando ensayos con probabilidad de éxito p hasta obtener un éxito.
# Compare la eficiencia de estos algoritmos para p = 0,8 y para p = 0,2.
# Para cada caso, realice 10000 simulaciones y calcule el promedio de los valores obtenidos. Comparar estos
# valores con el valor esperado de la distribución correspondiente. Si están alejados, revisar el código.

def ensayo(p):
    """
    Simula un ensayo con probabilidad de éxito p.
    """
    u = random()
    if u <= p:
        return 1 # Éxito
    else:
        return 0 # Fracaso

def geom(p):
    c = 0
    r = ensayo(p)
    while r == 0:
        c += 1
        r = ensayo(p)
    return c + 1 # Retorna el número de ensayos hasta el primer éxito

#Comparacion de los algoritmos

def sim(X,p,nsim):
    start = time.time()
    for _ in range(nsim):
        X(p)
    end = time.time()
    return end - start

def est_E(X, p, nsim):
    e = 0
    for _ in range(nsim):
        e += X(p)
    return e/nsim


print("Ejercicio 9")
p1 = 0.8
p2 = 0.2
nsim = 10000
print("-------------------------------Comparacion de los algoritmos para p = 0.8------------------------------")
print("esperanza teorica de la geometrica: ", 1/p1)
print("esperanza de la variable geometrica rec: ", est_E(geometrica_rec, p1, nsim))
print("esperanza de la variable geometrica transformada inversa: ", est_E(geometrica_transformada_inversa, p1, nsim))
print("esperanza de la variable geometrica ensayo: ", est_E(geom, p1, nsim))
print("eficiencia de los algoritmos")
print(f"Transformada inversa: {sim(geometrica_transformada_inversa, p1, nsim)}")
print(f"Recursiva: {sim(geometrica_rec, p1, nsim)}")
print(f"Ensayo: {sim(geom, p1, nsim)}")

print("-------------------Comparacion de los algoritmos para p = 0.2-----------------------------")
print("Esperanza teorica de la geometrica: ", 1/p2)
print("Esperanza de la variable geometrica rec: ", est_E(geometrica_rec, p2, nsim))
print("Esperanza de la variable geometrica transformada inversa: ", est_E(geometrica_transformada_inversa, p2, nsim))
print("Esperanza de la variable geometrica ensayo: ", est_E(geom, p2, nsim))
print(f"Transformada inversa: {sim(geometrica_transformada_inversa, p2, nsim)}")
print(f"Recursiva: {sim(geometrica_rec, p2, nsim)}")
print(f"Ensayo: {sim(geom, p2, nsim)}")

