from random import random
import math
import time

from Practico_5.ejercicio10 import Cauchy_lambda
from ejercicio10 import estimacion
from ejercicio10 import Cauchy
# Transformada Inversa
def Cauchy_TI(lamb):
    u = random()
    return lamb * math.tan(math.pi * (u - 0.5)) # Cauchy(0,1) = lambda * tan(pi*(U-0.5))



print("---------------------------Ejercicio 11-----------------------------")
print("Estimacion con 10000 simulaciones de la probabilidad de que \n el valor generado caiga en el interalo de (-lamb, lamb):")
print("Con lambda = 1: p=", estimacion(Cauchy_TI, 1, 10000))
print("Con lambda = 2.5: p=", estimacion(Cauchy_TI, 2.5, 10000))
print("Con lambda = 0.3: p=", estimacion(Cauchy_TI, 0.3, 10000))

#Comparar eficiencia de los dos algoritmos

def sim(X, lamb, nsim):
    start = time.time()
    for i in range(nsim):
        X(lamb)
    end = time.time()
    return (end-start)/nsim
print("Metodo de cauchy normal: \n Tiempo:", sim(Cauchy_lambda,1, 100000) * 10000000, "ms")
print("Metodo de Transformada Inversa: \n Tiempo:", sim(Cauchy_TI, 1, 100000) * 10000000, "ms")

#Graficar eficiencia entre los dos metodos
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

# Definir el rango de valores de lambda
lambdas = np.linspace(0.1, 5, 100)
# Definir el número de simulaciones
nsim = 100000
# Calcular los tiempos de simulación para cada lambda
tiempos_lambda = [sim(Cauchy_lambda, lamb, nsim) for lamb in lambdas]
tiempos_TI = [sim(Cauchy_TI, lamb, nsim) for lamb in lambdas]
# Crear un DataFrame para facilitar la visualización
df = pd.DataFrame({
    'Lambda': lambdas,
    'Tiempo_Cauchy': tiempos_lambda,
    'Tiempo_TI': tiempos_TI
})
# Crear la gráfica
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='Lambda', y='Tiempo_Cauchy', label='Cauchy Normal', color='blue')
sns.lineplot(data=df, x='Lambda', y='Tiempo_TI', label='Transformada Inversa', color='orange')
plt.title('Eficiencia de Métodos de Simulación para Diferentes Valores de Lambda')
plt.xlabel('Lambda')
plt.ylabel('Tiempo de Simulación (s)')
plt.legend()
plt.grid()
plt.show()

