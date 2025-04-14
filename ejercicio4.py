#Un supermercado posee 3 cajas. Por una cuestión de ubicación, el 40% de los clientes eligen la
#caja 1 para pagar, el 32% la caja 2, y el 28% la caja 3. El tiempo que espera una persona para ser atendida
#en cada caja distribuye exponencial con medias de 3, 4 y 5 minutos respectivamente.
#a) ¿Cuál es la probabilidad de que un cliente espere menos de 4 minutos para ser atendido?
#b) Si el cliente tuvo que esperar más de 4 minutos. ¿Cuál es la probabilidad de que el cliente haya elegido
#cada una de las cajas?
#c) Simule el problema y estime las probabilidades anteriores con 1000 iteraciones.

#parte c)
import random
import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple

def tiempo_espera() -> float:
    """
    Simula el tiempo de espera en una caja.
    """
    count = 0
    for i in range(1000):
        U = random.uniform(0, 1)
        if U < 0.4:
            # Caja 1
            tiempo = random.expovariate(1/3)
        elif U < 0.72:
            # Caja 2
            tiempo = random.expovariate(1/4)
        else:
            # Caja 3
            tiempo = random.expovariate(1/5)

        if tiempo < 4:
            count += 1
    return count / 1000
print(tiempo_espera())


def simulacion_b() -> List[float]:
    """
    Simula el tiempo de espera en una caja y estima la probabilidad de que el cliente haya elegido
    cada una de las cajas dado que esperó más de 4 minutos.
    """
    count_caja1 = 0
    count_caja2 = 0
    count_caja3 = 0
    total = 0

    for i in range(1000):
        U = random.uniform(0, 1)
        if U < 0.4:
            # Caja 1
            tiempo = random.expovariate(1/3)
            if tiempo > 4:
                count_caja1 += 1
        elif U < 0.72:
            # Caja 2
            tiempo = random.expovariate(1/4)
            if tiempo > 4:
                count_caja2 += 1
        else:
            # Caja 3
            tiempo = random.expovariate(1/5)
            if tiempo > 4:
                count_caja3 += 1

        if tiempo > 4:
            total += 1

    return [count_caja1 / total, count_caja2 / total, count_caja3 / total]
print(simulacion_b())
