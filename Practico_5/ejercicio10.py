from random import random
import math

c = 1/math.sqrt(math.pi)

# def Cauchy():
#     while True:
#         u = random()*c # Genera valores entre 0 y c
#         v = (random() - 0.5) * 2 * c # Genera valores entre -c y c
#         if u**2 + v**2 < c**2:
#             return v / u

# NOTAR QUE EN EL ALGORITMO ANTERIOR TODOS LOS c SE PODRIAN SIMPLIFICAR

def Cauchy():
    while True:
        u = random() # Genera valores entre 0 y 1
        v = (random() - 0.5) * 2 # Genera valores entre -1 y 1
        if u**2 + v**2 < 1:
            return v / u


#parte c)

def Cauchy_lambda(lamb):
    return lamb*Cauchy()

# parte d)

def estimacion(X, lamb, Nsim):
    p = 0
    for _ in range(Nsim):
        x = X(lamb)
        if x > -lamb and x < lamb:
            p += 1
    return p/Nsim
#la x es la cauchy
print("-------------------------------Ejercicio 10------------------------------")
print("Estaimacion con 10000 simulaciones de la probabilidad de que \n el valor generado caiga en el interalo de (-lamb, lamb):")
print("Con lambda = 1: p=", estimacion(Cauchy_lambda, 1, 10000))
print("Con lambda = 2.5: p=", estimacion(Cauchy_lambda, 2.5, 10000))
print("Con lambda = 0.3: p=", estimacion(Cauchy_lambda, 0.3, 10000))
