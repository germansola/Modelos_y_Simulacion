from random import random
import math

def lamba_t_i(t)
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

def poisson_no_homogeneo_adelgazamiento(T, lamda, lamda_t):
    eventos = []
    u = 1 - random()
    t = -math.log(u) / lamda
    while t <= T:
        v = random()
        if v < lamda_t(t)/lamda:
            eventos.append(t)
        t += -math.log(1 - random()) / lamda
    return eventos, len(eventos)


if __name__ == "__main__":
    suma_i = 0

    n_sim = 10_000

    for _ in range(n_sim):
        suma_i = poisson_no_homogeneo_adelgazamiento()