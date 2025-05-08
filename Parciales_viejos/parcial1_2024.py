#Se desea determinar mediante Monte Carlo el valor de la integral
#\int _1^{\infty }\:\frac{1}{x^2\ln \left(x+1\right)}dx
#a) Explicar y fundamentar cómo se estima mediante simulación el valor de esta integral por el método de
#Monte Carlo. Asumir que esta integral es convergente.
#b) ▶ Escribir un programa monte carlo(N) que estime el valor de la integral con N simulaciones. Utilizar
#el programa para completar la siguiente tabla. Completar la tabla con 6 decimales.
#Numero de sim.
#1 000
#10 000
#100 000
#Integral

#parte b)

import random
import math
from typing import List, Tuple
import numpy as np



def g_u(u):
    return 1/(u+1)**2 * math.log(u+1)

def monte_0_inf(g, nsim):

    def h(y):
        return (1 / y**2) * g_u(1/y - 1)
    integral = 0
    for _ in range(nsim):
        u = random.uniform(0, 1)
        integral += h(u)
    return integral / nsim

# Test de la función

# Resultado exacto
resultado_exacto = 1
# Simulación de Monte Carlo
sim = [1000, 10000, 100000]
for n in sim:
    resultado_montecarlo = monte_0_inf(g_u, n)
    print(f"Resultado de Monte Carlo con {n} simulaciones: {resultado_montecarlo:.10f}")

