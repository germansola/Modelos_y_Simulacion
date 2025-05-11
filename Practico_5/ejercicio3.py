from random import random
import math
def exp(lamb):
    u = 1 - random()
    return -math.log(u)/lamb

def X():
    u = random()
    if u < 0.5:
        return exp(1/3)
    elif u < 0.8:
        return exp(1/5)
    else:
        return exp(1/7)

ejemplo = [X() for i in range(25)]
print("valores entre 0 e infinito:", ejemplo)

def est_E(X, nsim):
    p = 0
    for _ in range(nsim):
        p += X()
    return p/nsim

print("Estimacion de la esperanza con 10000 simulaciones:", est_E(X, 10000))
