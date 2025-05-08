#Implemente dos métodos para generar una binomial Bin(n,p)
#I) Usando transformada inversa.
#II) Simulando n esnayos conprobabilidad de exito p y contando el numero de exitos
#Para amos metodos:
#a) Compare la eficiencia de ambos algoritmos para n=10 y p=0.3, evaluando el tiempo necesario para realizar 10000 simulaciones.
#b) Estime el valor con mayor ocurrecnia y la proporcion de vecces que se obtuvieron los valores 0 y 10 respectivamente.
#c) Compare estos valores con las probablidades teoricas de la binomial. Si estan aleados, revise el codigo.

import random
import time

def binomial_transformada_inversa1(n, p):
    c = p / (1 - p)
    prob = (1 - p) ** n
    F = prob

    for j in range(int(n*p)):
        prob *= c * (n - j) / (j + 1)
        F += prob
    j = int(n*p)
    u = random.random()
    if u < F:
        while u < F:
            prob *= c * (n - j) / (j + 1)
            F -= prob
            j -= 1
        return j + 1
    else:
        while u >= F:
            prob *= c * (n - j) / (j + 1)
            F += prob
            j += 1
    return j

print([binomial_transformada_inversa1(10, 0.5) for _ in range(25)])
print(binomial_transformada_inversa1(10, 0.5))


#Implemente dos metodos para generar una binomail Bin(n,p):
#I) Usando trasnformada inversa.
#II) Simulando n ensayos con probabilidad de exito p y contando el numero de exitos.


def binomial_transformada_inversa(n, p):
    c = p / (1 - p)
    prob = (1 - p) ** n
    F = prob
    u = random.random()
    i = 0
    while u >= F:
        prob *= c * (n - i) / (i + 1)
        F += prob
        i += 1
    return i
print([binomial_transformada_inversa(10, 0.3) for _ in range(25)])
print('Transformada inversa:', binomial_transformada_inversa(10, 0.3))

def binomial_simulacion(n, p):
    exitos = 0
    for i in range(n):
        if random.random() < p:
            exitos += 1
    return exitos

print('Simulación:', binomial_simulacion(10, 0.3))

# a) Compare la eficiencia de ambos algoritmos para n = 10 y p = 0,3, evaluadno el tiempo necesario para arealizar 10000 simulaciones.

def eficiencia(n, p, iteraciones):
    start_time = time.time()
    for i in range(iteraciones):
        binomial_transformada_inversa(n, p)
    elapsed_time = time.time() - start_time
    start_time = time.time()
    for i in range(iteraciones):
        binomial_simulacion(n, p)
    elapsed_time2 = time.time() - start_time
    if elapsed_time < elapsed_time2:
        print('Transformada inversa es más eficiente.')
    else:
        print('Simulación es más eficiente.')
    return elapsed_time, elapsed_time2

print('Eficiencia:', eficiencia(10, 0.3, 10000))

# b) Estime el valor con mayor ocurrencia y la proporcion de veces que se obtuieron los valores 0 y 10 respectivamente.

def estimar_valores(n, p, iteraciones):
    valores = []
    ceros = 0
    diez = 0
    for i in range(iteraciones):
        valor = binomial_transformada_inversa(n, p)
        valores.append(valor)
        if valor == 0:
            ceros += 1
        if valor == n:
            diez += 1
    return max(set(valores), key=valores.count), ceros/iteraciones, diez/iteraciones

print('Estimación:', estimar_valores(10, 0.3, 10000))
if __name__ == '__main__':
    pass