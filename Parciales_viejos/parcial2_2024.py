import random
import math

def UrnaX():
    A = [0, 1, 1, 2, 2, 2, 3, 3, 3]
    B = [0, 0, 0, 1, 1, 2, 2, 2, 2, 2]
    U = random.random()
    if U < 0.9:
        return A[int(random.random() * 9)]
    else:
        return B[int(random.random() * 10)]
    return A[I]


def algo_x(p):
    c=1.4
    while True:
        Y = random.randint(0,3)
        u = random.random()
        if u < p[Y] / (c*0.25):
            return Y


prob = [0.13, 0.22, 0.35, 0.3]



def simular_metodos(p,n):
    """
    Simula los métodos de rechazo, transformada inversa y urna para generar una variable aleatoria X.
    p: lista de probabilidades
    n: número de simulaciones
    """
    resultados_rechazo_optimo = []
    resultados_transformada_inversa = []
    resultados_urna = []

    for _ in range(n):
        resultados_rechazo_optimo.append(algo_x(p))
        resultados_urna.append(UrnaX())

    return resultados_rechazo_optimo, resultados_urna

resultados_rechazo_optimo = simular_metodos(prob, 1000)[0]
resultados_urna = simular_metodos(prob, 1000)[1]
# Calcular la media y la varianza de los resultados
media_rechazo_optimo = sum(resultados_rechazo_optimo) / len(resultados_rechazo_optimo)
varianza_rechazo_optimo = sum((x - media_rechazo_optimo) ** 2 for x in resultados_rechazo_optimo) / len(resultados_rechazo_optimo)
media_urna = sum(resultados_urna) / len(resultados_urna)
varianza_urna = sum((x - media_urna) ** 2 for x in resultados_urna) / len(resultados_urna)

print("Resultados de la simulación:")
print("Rechazo óptimo:", resultados_rechazo_optimo)
print("Urna:", resultados_urna)
print("Media Rechazo óptimo:", media_rechazo_optimo)
print("Varianza Rechazo óptimo:", varianza_rechazo_optimo)
print("Media Urna:", media_urna)
print("Varianza Urna:", varianza_urna)

def ejercicio2():
    u = random.random()
    if u <= 2/3:
        return (3*u / 2)**(2/3)
    else:
        return 3*u - 1

def est_E(X, nsim):
    sum = 0
    for _ in range(nsim):
        sum += X()
    return sum / nsim

print("Ejercicio 2")
# estimamos la esperanza con 10000 simulaciones
print("Esperanza:", est_E(ejercicio2, 10000))

# estimar P(X > 4)
def est_P(X, k, nsim): # P(X > k)
    p = 0
    for _ in range(nsim):
        r = X()
        if r > k:
            p += 1
    return p/nsim

print("P(X > 4):", est_P(ejercicio2, 4, 10000))

ejemplo1 = [ejercicio2() for i in range(25)]
print("inciso a:",ejemplo1)


def lamda_t_b(t):
    if 0 <= t <= 3:
        return 5+5*t
    elif 3 <= t <= 5:
        return 20
    elif 5 < t <= 9:
        return 30-2*t
    return None


def poisson_no_homogeneo_adelgazamiento_mejorado(T, lamda_t, intervals, lambdas):
    eventos = []
    j = 0
    t = -math.log(1 - random.random()) / lambdas[j]
    while t <= T:
        if t <= intervals[j]:
            v = random.random()
            if v < lamda_t(t)/lambdas[j]:
                eventos.append(t)
            t += -math.log(1 - random.random()) / lambdas[j]
        else:
            t = intervals[j] + ((t - intervals[j]) * lambdas[j]) / lambdas[j+1]
            j += 1
    return eventos, len(eventos)

if __name__ == "__main__":
    suma = 0
    n_sim = 10_000
    # intervalos para el algoritmo mejorado
    interval_i = [1,2,6,8,9]
    # lamdas para el algoritmo mejorado
    lamdas_i = [10, 15,20, 18, 14]

    for _ in range(n_sim):
        suma += poisson_no_homogeneo_adelgazamiento_mejorado(9, lamda_t_b, interval_i, lamdas_i)[1]
    print("Esperanza de la cantidad de eventos en el intervalo [0,9], con el algoritmo mejorado:", suma/n_sim)

