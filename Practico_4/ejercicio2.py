#Se desea construir una aproximación de:
#N
#∑
#k=1
#exp
#k
#N
#
#donde N = 10000 .
#a) Escriba un algoritmo para estimar la cantidad deseada.
#b) Obtenga la aproximación sorteando 100 números aleatorios.
#c) Escriba un algoritmo para calcular la suma de los primeros 100 términos, y compare el valor exacto
#con las dos aproximaciones, y el tiempo de cálculo.

import random
import numpy as np
from math import exp

def estimacion_a():
    """
    Estima la suma de N términos de la forma exp(k/N) para k = 1, 2, ..., N.
    n: número de simulaciones
    """
    N = 10000
    suma = 0
    for k in range(1, N + 1):
        suma += exp(k / N)
    return suma
print("estimacion_a():", estimacion_a())

def estimacion_con_aleatorios(n):
    """
    Estima la suma de N términos de la forma exp(k/N) para k = 1, 2, ..., N utilizando números aleatorios.
    n: número de simulaciones
    """
    N = 10000
    suma_aleatoria = 0
    for _ in range(n):
        k = random.randint(1, N)
        suma_aleatoria += exp(k / N)
    return suma_aleatoria / n * N

def otra_estimacion_con_aleatorios():
    suma = 0
    nsim = 100
    for _ in range(nsim):
        u = int(random.uniform(0, 1) * 10000) + 1
        suma += exp(u / 10000)
    return suma / nsim * 10000

print("estimacion_con_aleatorios(100):", estimacion_con_aleatorios(100))
print("otra_estimacion_con_aleatorios():", otra_estimacion_con_aleatorios())

def suma_100_terminos():
    """
    Calcula la suma de los primeros 100 términos de la forma exp(k/N) para k = 1, 2, ..., 100.
    """
    N = 100
    suma_100 = 0
    for k in range(1, N + 1):
        suma_100 += exp(k / N)
    return suma_100

print("suma_100_terminos():", suma_100_terminos())

# Comparación de resultados
suma_100 = suma_100_terminos()
estimacion_a = estimacion_a()
estimacion_aleatoria = estimacion_con_aleatorios(100)
print(f"Comparación de resultados:")
print(f"Suma de los primeros 100 términos: {suma_100:.10f}")
print(f"Estimación a partir de la suma: {estimacion_a:.10f}")
print(f"Estimación a partir de números aleatorios: {estimacion_aleatoria:.10f}")
# Comparación de tiempos de cálculo
import time
start_time = time.time()
suma_100 = suma_100_terminos()
end_time = time.time()
print(f"Tiempo de cálculo para la suma de los primeros 100 términos: {end_time - start_time:.10f} segundos")
#start_time = time.time()
#estimacion_a = estimacion_a()
#end_time = time.time()
#print(f"Tiempo de cálculo para la estimación a partir de la suma: {end_time - start_time:.10f} segundos")
start_time = time.time()
estimacion_aleatoria = estimacion_con_aleatorios(100)
end_time = time.time()
print(f"Tiempo de cálculo para la estimación a partir de números aleatorios: {end_time - start_time:.10f} segundos")
# Comparación de tiempos de cálculo





def g(i):
    return np.exp(i/10000)

def sum_aprox_MC(Nsim):
    start = time.time()
    suma = 0
    for _ in range(Nsim):
        u = int(random.random() * 100000) + 1
        suma += g(u)
    result = suma / Nsim * 100000
    end = time.time()
    return result, end-start

def sum_exact(n):
    start = time.time()
    suma = 0
    for i in range(1, n+1):
        suma += g(i)
    end = time.time()
    return suma, end-start

print("exact:", sum_exact(10000))
exact = sum_exact(10000)
print("MC1:", sum_aprox_MC(100))
print("MC2:", sum_aprox_MC(1000))
MC1 = sum_aprox_MC(100)
MC2 = sum_aprox_MC(1000)

