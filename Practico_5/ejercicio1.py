import random
import math

def x_a():
    u = random.uniform(0, 1)
    if u<=0.25:
        return 2*(math.sqrt(u) + 1)
    else: return 6-2*(math.sqrt(3-3*u))

ejemplo1 = [x_a() for i in range(25)]
print("inciso a:",ejemplo1)


def x_b():
    u = random.uniform(0, 1)
    if u <= 3/5:
        return  (1/3) * (math.sqrt(3) * math.sqrt((35*u)*27) - 9)
    else:
        return (((35*u)-19)**(1/3)) / (2**(1/3))

ejemplo2 = [x_b() for i in range(25)]
print("inciso b:", ejemplo2)


