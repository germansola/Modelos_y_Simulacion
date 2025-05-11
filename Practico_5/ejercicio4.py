#Desarrolle un método para generar la variable aleatoria con función de distribución
# F(x) = \int _0^{\infty }\:x^ye^{-y}dy
# Piense en el método de composición del ejercicio anterior. En particular, sea F la función de distribución
# de X y suponga que la distribución condicional de X dado Y = y es
# P(X ≤ x|Y = y) = x^y, 0 ≤ x ≤ 1.
from random import random
import math

def X():
    y = -math.log(1-random())
    u = random()
    return u**(1/y)

#sample
ejemplo = [X() for i in range(25)]

print("valores:", ejemplo)

