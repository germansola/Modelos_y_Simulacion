#Para U1,U2,... variables aleatorias uniformemente distribuídas en el intervalo (0,1), se define:
#N = Mínimo(
#n :
#n
#∑
#i=1
#Ui > 1
#)
#Es decir, N es igual a la cantidad de números aleatorios que deben sumarse para exceder a 1.
#a) Estimar E[N] generando n valores de N y completar la siguiente tabla:
#n 100 1000 10000 100000 1000000
#E[N]

from random import random

for N in [100, 1000, 10000, 100000, 1000000]:
    contadores = []
    for iter in range(N):
        suma = 0
        contador = 0
        while suma <= 1:
            suma += random()
            contador += 1
        contadores.append(contador)

    estimacion_esp = sum(contadores) / N
    print(f"para {N} experimentos mi aprox es {estimacion_esp}")

from math import exp
print(f"e = {exp(1)}")