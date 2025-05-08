#(a) Desarrolle un método para generar una variable aleatoria X cuya distribución de probabilidad está
# dada por:
# P(X = j) = \left(\frac{1}{2}\right)^{j+1}+\frac{1}{4}\cdot \left(\frac{2}{3}\right)^j
# , j = 1,2,...
# (b) Estime E(X) con 1000 repeticiones y compare con la esperanza exacta.

import random
import numpy as np

def P_X(j):
    """
    Función de masa de probabilidad para la variable aleatoria X.
    """
    return (1/2)**(j+1) + (1/4) * (2/3)**j

def transformada_inversa(nsim):
    """
    Genera una variable aleatoria X usando el método de la transformada inversa.
    """
    u = random.random()
    p = 0
    j = 1
    while p < u:
        p += P_X(j)
        j += 1
    return j - 1

def est_E(nsim):
    """
    Estima la esperanza de la variable aleatoria X.
    """
    e = 0
    for _ in range(nsim):
        e += transformada_inversa(nsim)
    return e / nsim


if __name__ == "__main__":
    nsim = 1000
    print(f"Esperanza estimada de X: {est_E(nsim)}")
    print("esperanza exacta: 2.5 ")
    # Esperanza exacta calculada a partir de la fórmula de la esperanza para la distribución dada.
    # La fórmula de la esperanza para una variable aleatoria discreta es E(X) = sum(i * P(X=i)).
    # En este caso, se puede calcular la esperanza exacta utilizando la fórmula de la distribución dada.
    # La esperanza exacta se calcula como 1/(1/2 - (1/4)*(2/3)), que es el resultado de la suma infinita de la serie.
    # La fórmula se deriva de la serie geométrica y la convergencia de la misma.


