from math import log
from random import random
#escribimos el poisson homogeneo primero y principal
def poisson_homogeneo(lam, T):
    t = -log(1 - random())/ lam #momento de la llegada
    eventos = []
    while t <= T:
        eventos.append(t)
        t += -log(1 - random())/ lam
    return eventos, len(eventos)
#ahi los eventos de llegada y la cantidad de llegada

def llegada_aficionados():
    #quiero simular un experimento de llegadas
    tiempos, num_buses = poisson_homogeneo(5, 1) #genero la cantidad de colectivos que estan llegando t = 1 hora
    aficionados = 0
    for i in range(num_buses):
        aficionados += int(21 * random() + 20) #me aseguro que sea un numero entre 20 y 40
    return aficionados

#150 es la esperanza teorica
# esperanza = 5 (esperanza de la poisson en 1hr) * 30 (esperanza de la uniforme discreta entre 20 y 40) = 150

#ahora quiero estimar la esperanza
numeros = []
tiradas = 100000
for i in range(tiradas):
    numeros.append(llegada_aficionados())

print(sum(numeros)/tiradas)



