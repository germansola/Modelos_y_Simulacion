#Implemente cuatro métodos para generar una variable X que toma los valores del 1 al 10,
#con probabilidades p1 = 0,11, p2 = 0,14, p3 = 0,09, p4 = 0,08, p5 = 0,12, p6 = 0,10, p7 = 0,09, p8 =
#0,07, p9 = 0,11, p10 = 0,09 usando:
#a) Método de rechazo con una uniforme discreta, buscando la cota c más baja posible.
#b) Método de rechazo con una uniforme discreta, usando c = 3.
#c) Transformada inversa.
#d) Método de la urna: utilizar un arreglo A de tamaño 100 donde cada valor i está en exactamente pi ∗ 100
#posiciones. El método debe devolver A[k] con probabilidad 0,01. ¿Por qué funciona?

import random
import numpy as np
import matplotlib.pyplot as plt
from math import exp
import math
import time
def rechazo_uniforme_optimo(p):
    """
    Genera un valor de X usando el método de rechazo con una uniforme discreta.
    La cota c se calcula como el máximo de las probabilidades dividido la probabilidad de la uniforme (1/10).
    """
    c = max(p) / (1/10)  # Cota c óptima
    while True:
        Y = random.randint(1, 10)  # Genera Y ~ Uniforme discreta en {1, 2, ..., 10}
        U = random.random()  # Genera U ~ Uniforme(0, 1)
        if U <= p[Y-1] / (c * (1/10)):
            return Y
def rechazo_uniforme_c3(p):
    """
    Genera un valor de X usando el método de rechazo con una uniforme discreta y c = 3.
    """
    c = 3
    while True:
        Y = random.randint(1, 10)
        U = random.random()
        if U <= p[Y-1] / (c * (1/10)):
            return Y

def transformada_inversa(p, optimizado: bool = True):
    """
    Genera una variable aleatoria X con probabilidades p usando el método de la transformada inversa.
    p: lista de probabilidades
    o: indica si esta optimizado
    """
    if optimizado:
        # ordenamos de mayor a menor las probabilidades
        p = sorted(p, reverse=True)
    # calculamos la función de distribución acumulada
    i = 0
    u = random.random()
    acumulador = p[0]
    while u > acumulador:
        i += 1
        acumulador += p[i]

    # devolvemos el valor correspondiente a la probabilidad acumulada
    return i + 1  # +1 porque los índices empiezan en 0 y los valores de X empiezan en 1


def metodo_urna(p):
    """
    Genera una variable aleatoria X con probabilidades p usando el método de la urna.
    p: lista de probabilidades
    """
    urna_lista = []
    for i in range(len(p)):
        # Multiplicamos cada probabilidad por 100 para obtener la cantidad de veces que aparece el valor i+1
        urna_lista.append(int(p[i] * 100))
    urna = []
    for ind in range(len(urna_lista)):
        urna += urna_lista[ind] * [ind + 1]

    i = int(random.random() * len(urna))
    return urna[i]  # Retorna el valor correspondiente a la probabilidad acumulada

def simular_metodos(p,n):
    """
    Simula los métodos de rechazo, transformada inversa y urna para generar una variable aleatoria X.
    p: lista de probabilidades
    n: número de simulaciones
    """
    resultados_rechazo_optimo = []
    resultados_rechazo_c3 = []
    resultados_transformada = []
    resultados_urna = []

    for _ in range(n):
        resultados_rechazo_optimo.append(rechazo_uniforme_optimo(p))
        resultados_rechazo_c3.append(rechazo_uniforme_c3(p))
        resultados_transformada.append(transformada_inversa(p))
        resultados_urna.append(metodo_urna(p))

    return resultados_rechazo_optimo, resultados_rechazo_c3, resultados_transformada, resultados_urna

def graficar_histograma(resultados, metodo):
    """
    Grafica el histograma de los resultados obtenidos por cada método.
    resultados: lista de resultados
    metodo: nombre del método
    """
    plt.hist(resultados, bins=10, density=True, alpha=0.5, color='blue', edgecolor='black')
    plt.title(f"Histograma de resultados - {metodo}")
    plt.xlabel("Valores")
    plt.ylabel("Frecuencia")
    plt.xticks(range(1, 11))
    plt.grid(axis='y', alpha=0.75)
    plt.show()
def calcular_tiempos(p, n):
    """
    Calcula el tiempo de ejecución de cada método.
    :param p: lista de probabilidades
    :param n: número de simulaciones
    :return: tiempos de ejecución de cada método
    """
    tiempos = {}
    start_time = time.time()
    simular_metodos(p, n)
    tiempos['simular_metodos'] = time.time() - start_time

    start_time = time.time()
    for _ in range(n):
        rechazo_uniforme_optimo(p)
    tiempos['rechazo_uniforme_optimo'] = time.time() - start_time

    start_time = time.time()
    for _ in range(n):
        rechazo_uniforme_c3(p)
    tiempos['rechazo_uniforme_c3'] = time.time() - start_time

    start_time = time.time()
    for _ in range(n):
        transformada_inversa(p)
    tiempos['transformada_inversa'] = time.time() - start_time

    start_time = time.time()
    for _ in range(n):
        metodo_urna(p)
    tiempos['metodo_urna'] = time.time() - start_time

    return tiempos
# Probabilidades
p = [0.11, 0.14, 0.09, 0.08, 0.12, 0.10, 0.09, 0.07, 0.11, 0.09]
n = 1000000  # Número de simulaciones
resultados_rechazo_optimo, resultados_rechazo_c3, resultados_transformada, resultados_urna = simular_metodos(p, n)
# Graficar histogramas
graficar_histograma(resultados_rechazo_optimo, "Rechazo Uniforme Óptimo")
graficar_histograma(resultados_rechazo_c3, "Rechazo Uniforme c=3")
graficar_histograma(resultados_transformada, "Transformada Inversa")
graficar_histograma(resultados_urna, "Método de la Urna")
# Calcular tiempos de ejecución
tiempos = calcular_tiempos(p, n)
print("Tiempos de ejecución:")
for metodo, tiempo in tiempos.items():
    print(f"{metodo}: {tiempo:.6f} segundos")
# Comparar resultados
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
frecuencias_rechazo_optimo = [resultados_rechazo_optimo.count(i) / n for i in valores]
frecuencias_rechazo_c3 = [resultados_rechazo_c3.count(i) / n for i in valores]
frecuencias_transformada = [resultados_transformada.count(i) / n for i in valores]
frecuencias_urna = [resultados_urna.count(i) / n for i in valores]
# Graficar frecuencias
plt.plot(valores, frecuencias_rechazo_optimo, label='Rechazo Uniforme Óptimo', marker='o')
plt.plot(valores, frecuencias_rechazo_c3, label='Rechazo Uniforme c=3', marker='o')
plt.plot(valores, frecuencias_transformada, label='Transformada Inversa', marker='o')
plt.plot(valores, frecuencias_urna, label='Método de la Urna', marker='o')
plt.title("Frecuencias de resultados")
plt.xlabel("Valores")
plt.ylabel("Frecuencia")
plt.xticks(valores)
plt.legend()
plt.grid()
plt.show()

