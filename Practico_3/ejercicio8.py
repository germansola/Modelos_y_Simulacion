#8. Para U1,U2,... números aleatorios, se define:
#N = Máximo(
#n :
#n
#∏
#i=1
#Ui ≥ e
#−3
#)
#donde:
#0
#∏
#i=1
#Ui = 1. Mediante n simulaciones determinar:
# a) n 100 1000 10000 100000 1000000
# E[N]
#b) P(N = i) para i = 0,1,2,3,4,5,6, usando n = 1000000.

import random
import numpy as np
from math import exp

def estimar_E_N(n):
    """
    Estima E[N] generando n valores de N.
    n: número de simulaciones
    """
    contadores = []
    for _ in range(n):
        producto = 1
        contador = 0
        while producto >= exp(-3):
            producto *= random.uniform(0, 1)
            contador += 1
        contadores.append(contador)

    estimacion_esp = sum(contadores) / n
    return estimacion_esp

# Probabilidades para diferentes valores de n
n_values = [100, 1000, 10000, 100000, 1000000]
for n in n_values:
    estimacion = estimar_E_N(n)
    print(f"para {n} experimentos mi aprox es {estimacion:.8f}")


#parte b)

def P_N_i(n, i):
    """
    Estima P(N = i) generando n valores de N.
    n: número de simulaciones
    i: valor para el cual se quiere calcular la probabilidad
    """
    contadores = []
    for _ in range(n):
        producto = 1
        contador = 0
        while producto >= exp(-3):
            producto *= random.uniform(0, 1)
            contador += 1
        contadores.append(contador)
    return contadores.count(i) / n

# Probabilidades para diferentes valores de i
i_values = [0, 1, 2, 3, 4, 5, 6]
n = 1000000
for i in i_values:
    probabilidad = P_N_i(n, i)
    print(f"P(N = {i}) con {n} experimentos es {probabilidad:.8f}")
