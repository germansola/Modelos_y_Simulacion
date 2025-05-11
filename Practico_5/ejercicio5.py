#a) Considere que es sencillo generar una variable aleatoria a partir de cualquiera de las distribuciones Fi
# ,
# i = 1,...,n. Explique cómo generar variables aleatorias a partir de las siguientes distribuciones:
# i) FM(x) =
# n
# ∏
# i=1
# Fi(x)
# ii) Fm(x) = 1−
# n
# ∏
# i=1
# (1−Fi(x))
# Sugerencia: Si Xi
# , i = 1,...,n, son variables aleatorias independientes, donde Xi
# tiene distribución Fi
# ,
# ¿cuál variable aleatoria tiene como distribución a F en cada caso?
# b) Genere una muestra de 10 valores de las variables M y m con distribuciones FM y Fm si Xi son
# exponenciales independientes con parámetros 1, 2 y 3 respectivamente.

from random import random
import math
from numpy import min, max
import numpy as np

def generar_exponencial(lamb):
    u = 1-random()
    return -math.log(u)/lamb

#Maximo
def FM():
    v =[generar_exponencial(1), generar_exponencial(2), generar_exponencial(3)]
    return float(max(v))
#Minimo
def Fm():
    v =[generar_exponencial(1), generar_exponencial(2), generar_exponencial(3)]
    return float(min(v))

# Como el minimo entre exponenciales tinee distribucion exponencial, con parametro igual a la suma de parametros
#directamente podemos hacer

def m2(): #es lo mismo que Fm
    return generar_exponencial(1+2+3)

# Generamos 10 valores de M y m
m_values = [FM() for _ in range(10)]
print("Valores de M:", m_values)
m_values2 = [Fm() for _ in range(10)]
print("Valores de m:", m_values2)
m_values3 = [m2() for _ in range(10)]
print("Valores de m2:", m_values3)

#para comprobar que hicimos bien
def est_E(X, nsim):
    sum = 0
    for _ in range(nsim):
        sum += X()
    return sum / nsim

print("estimacion de la esperanza con 10000 simulaciones:", est_E(FM, 10000))
print("estimacion de la esperanza con 10000 simulaciones:", est_E(Fm, 10000))
print("estimacion de la esperanza con 10000 simulaciones:", est_E(m2, 10000))



