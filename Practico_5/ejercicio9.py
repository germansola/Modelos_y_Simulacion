#Escriba tres programas para generar un variable aleatoria normal patrón, usando
#a) generación de variables exponenciales según el ejemplo 5 f del libro Simulacion de S. M. Ross,
#b) el método polar,
#c) el método de razón entre uniformes.

from random import random, NV_MAGICCONST
import math
#definimos la simulacion de una variable aleatoria exponencial

def exponencial(lamb):
    u = 1 - random()
    return -math.log(u) / lamb

#definimo simulacion variable normal hecho con el metodo de aceptacion y rechazo

def normal_rechazo(mu: float = 0.0, sigma: float = 1.0):
    while True:
        y1 = exponencial(1)
        y2 = exponencial(1)
        if y2 >= ((y1 - 1) ** 2) / 2:
            u = random()
            if u <= 1/2:
                return y1 * sigma + mu
            return -y1 * sigma + mu

#definimos simulacion variable normal hecho con el metodo polar
def metodo_polar(mu: float = 0.0, sigma: float = 1.0):
    Rcuadrado = -2 * math.log(1 - random())
    theta = 2 * math.pi * random()
    x = math.sqrt(Rcuadrado) * math.cos(theta)
    y = math.sqrt(Rcuadrado) * math.sin(theta)
    return x * sigma + mu, y * sigma + mu

#definimos simulacion variable normal hecho con el metodo de razon entre uniformes

def metodo_razon_uniformes(mu: float = 0.0, sigma: float = 1.0):
    NV_MAGICONST = 4 * math.exp(-0.5) / math.sqrt(2.0)
    while True:
        u1 = random()
        u2 = 1.0 - random()
        z = NV_MAGICONST * (u1 - 0.5) / u2
        zz = z * z / 4.0
        if zz <= -math.log(u2):
            break
    return z * sigma + mu

#definimos la funcion de simulacion
def sim(X, nsim):
    start = time.time()
    for i in range(nsim):
        X()
    end = time.time()
    return (end-start)/nsim

if __name__ == "__main__":

    n_sim = 10_000
    for func in [normal_rechazo, lambda: metodo_polar()[1], metodo_razon_uniformes]:
        suma = 0
        suma_quadrado = 0
        for _ in range(n_sim):
            sim = func()
            suma += sim
            suma_quadrado += sim**2

        esperanza = suma/n_sim
        desviacion = math.sqrt((suma_quadrado/n_sim) - ((suma/n_sim)**2))
        print(f"{func.__name__ if func.__name__ != '<lambda>' else 'metodo_polar'}")
        print(f"\tesperanza: {round(esperanza, 4)}")
        print(f"\tdesviacion: {round(desviacion, 4)}")