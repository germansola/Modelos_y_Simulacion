import random
import math
from scipy.integrate import quad

print("================ejercicio 1=====================")

def g(u):
    return math.sqrt(u + math.sqrt(u))

def montecarlo_a_b(g, a, b, nsim):
    """
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


# Resultado de la simulacion
sim = [1000, 10000, 100000]
for i in sim:
    resultado_montecarlo = montecarlo_a_b(g, 1, 7, i)
    print(f"Resultado de Monte Carlo con {i} simulaciones: {resultado_montecarlo:.6f}")

# Resultado exacto
resultado_exacto = quad(g, 1, 7)
print(f"Resultado exacto: {resultado_exacto[0]:.6f}")


print("================ejercicio 2=====================")

def juego():
    suma = 0
    num_sumandos = 0
    while suma <= 1:
        suma += random.uniform(0, 1)
        num_sumandos += 1
    return num_sumandos

# parte b)

def impares(nsim):
    """
    Simula el juego y estima la probabilidad de que el número total de sumandos sea impar.
    nsim: número de simulaciones
    """
    aciertos_impares = 0
    for _ in range(nsim):
        num_sumandos = juego()
        if num_sumandos % 2 == 1:
            aciertos_impares += 1
    return aciertos_impares / nsim


# Test de la función
# Resultado de la simulacion
sim = [100, 1000, 10000]
for i in sim:
    resultado = impares(i)
    print(f"Resultado con {i} simulaciones: {resultado:.6f}")




