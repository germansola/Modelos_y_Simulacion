from random import random
import math
import time
# Transformada Inversa
def X_TI(n):
    u = random()
    return u ** (1/n)

# Aceptacion y Rechazo
def X_AR(n):
    while True:
        y = random()
        u = random()
        if u <= y ** (n-1):
            return y


#Usando el ejercicio 5
def X_E5(n):
    u = []
    for _ in range(n):
        u.append(random())
    return max(u)

#Comparacion de los metodos

def sim(X, n, nsim):
    start = time.time()
    for _ in range(nsim):
        X(n)
    end = time.time()
    return (end-start) / nsim

print("Metodo de Aceptacion y Rechazo: \n Tiempo:", sim(X_AR, 1000, 100000) *10000000, "ms")
print("Metodo de Ejercicio 5: \n Tiempo:", sim(X_E5, 1000, 100000) *10000000, "ms")
print("Metodo de Transformada Inversa: \n Tiempo:", sim(X_TI, 1000, 100000) *10000000, "ms")

print("El metodo de Aceptacion y Rechazo es el mas lento, seguido por el de Ejercicio 5 y por ultimo el de Transformada Inversa")



