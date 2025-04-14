#Monter carlo con n = 1000, 5000, 10000 iteraciones
#a) \int _0^1\:\left(1-x^2\right)^{^{\frac{3}{2}}}dx

from random import random
import random
from math import sqrt
from typing import Callable
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
import math
sim = [100, 1000, 10000 , 100000, 1000000]
print("================inciso a)=====================")
def g_a(u):
    return (1-u**2)**(3/2)

def montecarlo(g, nsim):
    """
    Simula el método de Monte Carlo para calcular la integral de a(u).
    g: función a integrar
    nsim: número de simulaciones
    """
    integral = 0
    for _ in range(nsim):
        integral += g(random.uniform(0, 1))
    return integral / nsim
# Test de la función

# Resultado exacto
resultado_exacto, _ = quad(g_a, 0, 1)
print(f"Resultado exacto: {resultado_exacto:.10f}")

# Simulación de Monte Carlo a)
for n in sim:
    resultado_montecarlo = montecarlo(g_a, n)
    print(f"Resultado de Monte Carlo con {n} simulaciones: {resultado_montecarlo:.10f}")


print("================inciso b)=====================")

#b) \int _2^3\:\frac{x}{x^2-1}

def g_b(u):
    return u / (u**2 - 1)

def montecarlo_a_b(g, a, b, nsim):
    """
    Simula el método de Monte Carlo para calcular la integral de g(u) en el intervalo [a, b].
    g: función a integrar
    a: límite inferior de integración
    b: límite superior de integración
    nsim: número de simulaciones
    """
    integral = 0
    for _ in range(nsim):
        integral += g(a + (b - a) * random.uniform(0, 1))
    return (b - a) * integral / nsim
# Test de la función
# Resultado exacto
resultado_exacto, _ = quad(g_b, 2, 3)
print(f"Resultado exacto: {resultado_exacto:.10f}")
# Simulación de Monte Carlo b)
for n in sim:
    resultado_montecarlo = montecarlo_a_b(g_b, 2, 3, n)
    print(f"Resultado de Monte Carlo con {n} simulaciones: {resultado_montecarlo:.10f}")

print("================inciso c)=====================")

#c) \int _0^{\infty }\:x\left(1+x²\right)^{-2}

def g_c(u):
    return u * (1 + u**2)**(-2)

def montecarlo_0_infinito(g, nsim):
    """
    Simula el método de Monte Carlo para calcular la integral de g(u) en el intervalo [0, ∞).
    g: función a integrar
    nsim: número de simulaciones
    """
    def h(y):
        return (1/y**2) * g((1/y) - 1)
    integral = 0
    for _ in range(nsim):
        u = random.uniform(0, 1)
        integral += h(u)
    return integral / nsim

# Test de la función
# Resultado exacto
resultado_exacto, _ = quad(g_c, 0, np.inf)
print(f"Resultado exacto: {resultado_exacto:.10f}")
# Simulación de Monte Carlo c)
for n in sim:
    resultado_montecarlo = montecarlo_0_infinito(g_c, n)
    print(f"Resultado de Monte Carlo con {n} simulaciones: {resultado_montecarlo:.10f}")


print("================inciso d)=====================")

#d) \int _{-\infty }^{\infty }\:e^{-x^2}

# Definimos la función g_d(u) = e^{-u^2}
def f_d(u):
    return math.exp(-u**2)
def g_d(u):
    return 2*math.exp(-u**2)

# Test de la función
# Resultado exacto
# Para la integral de e^{-x^2} en el intervalo [-∞, ∞], el resultado exacto es sqrt(pi)
# usando la función quad de scipy
resultado_exacto, _ = quad(f_d, -np.inf, np.inf)
print(f"Resultado exacto: {resultado_exacto:.10f}")
# Simulación de Monte Carlo d)
for n in sim:
    resultado_montecarlo = montecarlo_0_infinito(g_d, n)
    print(f"Resultado de Monte Carlo con {n} simulaciones: {resultado_montecarlo:.10f}")
    print(f"Error absoluto: {abs(resultado_montecarlo - resultado_exacto):.10f}")

print("================inciso  e)=====================")

#\int _0^1\:\left[\int _0^1\:e^{\left(x+y\right)^2dx}\right]dy

def g_e(x, y):
    return math.exp((x+y)**2)
def montecarlo_e(g, nsim):
    """
    Simula el método de Monte Carlo para calcular la integral de g(u).
    """
    integral = 0
    for _ in range(nsim):
        u = random.uniform(0, 1)
        v = random.uniform(0, 1)
        integral += g(u, v)
    return integral / nsim

# Test de la función
# Resultado exacto
resultado_exacto, _ = quad(lambda y: quad(lambda x: g_e(x, y), 0, 1)[0], 0, 1)

print(f"Resultado exacto: {resultado_exacto:.10f}")
# Simulación de Monte Carlo e)
for n in sim:
    resultado_montecarlo = montecarlo_e(g_e, n)
    print(f"Resultado de Monte Carlo con {n} simulaciones: {resultado_montecarlo:.10f}")
    print(f"Error absoluto: {abs(resultado_montecarlo - resultado_exacto):.10f}")

def sim_5e(n):
    def g(x, y):
        return math.exp((x+y)**2)
    X = [random.uniform(0, 1) for _ in range(n)]
    Y = [random.uniform(0, 1) for _ in range(n)]
    return sum([ g(x, y) for x, y in zip(X, Y) ]) / n

for n in sim:
    print(f"Resultado exacto: {sim_5e(n):.10f}")

print("================inciso f)====================")

#f) \int _0^{\infty }\:\left[\int _0^x\:e^{\left(x+y\right)^2}dx\right]dy

def indicadora(u, v):
    if v < u:
        return 1
    else:
        return 0

def g_f(u, v):
    return math.exp(-(u+v)) * indicadora(u, v)

def montecarlo_f(g, nsim):
    """
    Simula el método de Monte Carlo para calcular la integral de g(u).
    """
    integral = 0
    for _ in range(nsim):
        u = random.uniform(0, 1)
        v = random.uniform(0, 1)
        integral += g_f(1/u-1, 1/v-1) / ((u**2) * (v**2))
    return integral / nsim

# Test de la función
# Resultado exacto
resultado_exacto_f = 0.5
# Simulación de Monte Carlo f)
for n in sim:
    resultado_montecarlo = montecarlo_f(g_f, n)
    print(f"Resultado de Monte Carlo con {n} simulaciones: {resultado_montecarlo:.10f}")
    print(f"Error absoluto: {abs(resultado_montecarlo - resultado_exacto_f):.10f}")

