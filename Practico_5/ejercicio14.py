from random import random
import math

def lamba_t_i(t):
    return 3 + (4/(t+1))

def lamba_t_ii(t):
    return (t-2)**2 - (5*t) + 17

def lamba_t_iii(t):
    if 2 <= t <= 3:
        return (t/2) - 1
    elif 3 <= t <= 6:
        return 1 - (t/6)
    return 0

#a)

def poisson_no_homogeneo_adelgazamiento(T, lamda, lamda_t): #T es el extremo derecho del intervalo, lamda es la tasa de llegada (si valuo T en la funcion me lo da hasta donde llega
    eventos = []
    u = 1 - random()
    t = -math.log(u) / lamda
    while t <= T:
        v = random()
        if v < lamda_t(t)/lamda:
            eventos.append(t)
        t += -math.log(1 - random()) / lamda
    return eventos, len(eventos)

#b)
def exponential(lamda):
    u = random()
    return -math.log(u)/lamda
def poisson_no_homogeneo_adelgazamiento_mejorado(T, lamda_t, intervals, lambdas):
    eventos = []
    j = 0
    t = -math.log(1 - random()) / lambdas[j]
    while t <= T:
        if t <= intervals[j]:
            v = random()
            if v < lamda_t(t)/lambdas[j]:
                eventos.append(t)
            t += -math.log(1 - random()) / lambdas[j]
        else:
            t = intervals[j] + ((t - intervals[j]) * lambdas[j]) / lambdas[j+1]
            j += 1
    return eventos, len(eventos)



if __name__ == "__main__":
    suma_i = 0
    suma_ii = 0
    suma_iii = 0
    n_sim = 10_000
    suma_i_m = 0
    suma_ii_m = 0
    suma_iii_m = 0
    # intervalos para el algoritmo mejorado
    interval_i = [1, 2, 3]
    interval_ii = [2, 4, 5]
    interval_iii = [3, 4, 6]
    # lamdas para el algoritmo mejorado
    lamdas_i = [5, 13/3, 7]
    lamdas_ii = [21, 7, 1]
    lamdas_iii = [1/2, 1/2, 1/3]


    for _ in range(n_sim):
        suma_i += poisson_no_homogeneo_adelgazamiento(3,7,lamba_t_i)[1]
        suma_i_m += poisson_no_homogeneo_adelgazamiento_mejorado(3, lamba_t_i, interval_i, lamdas_i)[1]
        suma_ii += poisson_no_homogeneo_adelgazamiento(5,21,lamba_t_ii)[1]
        suma_ii_m += poisson_no_homogeneo_adelgazamiento_mejorado(5, lamba_t_ii, interval_ii, lamdas_ii)[1]
        suma_iii += poisson_no_homogeneo_adelgazamiento(6,1/2,lamba_t_iii)[1]
        suma_iii_m += poisson_no_homogeneo_adelgazamiento_mejorado(6, lamba_t_iii, interval_iii, lamdas_iii)[1]


    print("i)")
    print("Esperanza de la cantidad de eventos en el intervalo [0,3], con el algoritmo comun:", suma_i/n_sim)
    print("Esperanza de la cantidad de eventos en el intervalo [0,3], con el algoritmo mejorado:", suma_i_m/n_sim)
    print("ii)")
    print("Esperanza de la cantidad de eventos en el intervalo [0,5], con el algoritmo comun:", suma_ii/n_sim)
    print("Esperanza de la cantidad de eventos en el intervalo [0,5], con el algoritmo mejorado:", suma_ii_m/n_sim)
    print("iii)")
    print("Esperanza de la cantidad de eventos en el intervalo [0,6], con el algoritmo comun:", suma_iii/n_sim)
    print("Esperanza de la cantidad de eventos en el intervalo [0,6], con el algoritmo mejorado:", suma_iii_m/n_sim)


