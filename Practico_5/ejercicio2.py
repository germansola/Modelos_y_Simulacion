import random
import math

#Estime la media de cada variable con 10.000 repeticiones, usando los parámetros a = 2, µ =
#2, k = 2, λ = 1, β = 2. Busque en la web los valores de las esperanzas para cada variable
#con estos parámetros (cuidado con las parametrizaciones) y compare los valores obtenidos.

def metodo_distribucion_pareto(a):
    u = random.uniform(0, 1)
    return (1-u) ** (-1 / a)

def metodo_distribucion_weibull(lamb, beta):
    u = random.uniform(0, 1)
    return lamb * ((-math.log(1-u)) ** (1 / beta))


def est_E(X, nsim):
    sum = 0
    for _ in range(nsim):
        sum += X()
    return sum / nsim

# Definimos los parámetros
a = 2
mu = 2
k = 2
lamb = 1
beta = 2

# valores de la esperanzas de cada variable real

esperanza_pareto = a / (a - 1)
esperanza_weibull = lamb * math.gamma(1 + (1 / beta))

# Estimamos la esperanza
met_estimacion_pareto = est_E(lambda: metodo_distribucion_pareto(a), 10000)
met_estimacion_weibull = est_E(lambda: metodo_distribucion_weibull(lamb,beta), 10000)
# Imprimimos los resultados
print("Esperanza de la distribución de Pareto (teórica):", esperanza_pareto)
print("Esperanza de la distribución de Pareto (estimada):", met_estimacion_pareto)
print("Esperanza de la distribución de Weibull (teórica):", esperanza_weibull)
print("Esperanza de la distribución de Weibull (estimada):", met_estimacion_weibull)
