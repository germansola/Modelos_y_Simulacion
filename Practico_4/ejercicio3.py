#Se lanzan simultáneamente un par de dados legales y se anota el resultado de la suma de ambos.
#El proceso se repite hasta que todos los resultados posibles: 2,3,...,12 hayan aparecido al menos una vez.
#Estudiar mediante una simulación la variable N, el número de lanzamientos necesarios para cumplir el
#proceso. Cada lanzamiento implica arrojar el par de dados.

# Describa la estructura lógica del algoritmo que permite simular en computadora el número de lanzamientos necesarios para cumplir el proceso.

import math
import random
import numpy as np
import seaborn as sns
from time import time

def udiscreta(n):
    u = random.random()
    return int(u * n) + 1

def simulate(X,n_sim,ddof=0,**kwargs):
    """
    Parameters:
    -----------
    X : callable
        A function (or callable object) that generates a single simulated value when called with **kwargs.
    n_sim : int
        Number of simulations to run.
    ddof : int, optional (default=0)
        Delta degrees of freedom for variance and standard deviation calculations.
        If ddof=0 (default), computes population variance/std.
        If ddof=1, computes sample variance/std (unbiased estimator).
    **kwargs : dict
        Additional keyword arguments passed to the function X.

    Returns:
    --------
    s : ndarray
        Array of all simulated values (shape: (n_sim,)).
    mean_sim : float
        Mean of the simulated values.
    median_sim : float
        Median of the simulated values.
    var_sim : float
        Variance of the simulated values (with specified ddof).
    std_sim : float
        Standard deviation of the simulated values (with specified ddof).
    """
    s = np.empty(n_sim)
    for i in range(n_sim):
      s[i]=X(**kwargs)
    mean_sim = np.mean(s)
    median_sim = np.median(s)
    var_sim = np.var(s,ddof=ddof)
    std_sim = np.std(s,ddof=ddof)
    return s,mean_sim,median_sim,var_sim,std_sim

def dices_trial():
  """
  Simulates rolling two fair 6-sided dice and returns their sum.
  """
  return udiscreta(6) + udiscreta(6)

def N():
  """
  Counts how many trials are needed until all sums from 2 to 12 appear at least once.
  """
  s = set()
  i = 0
  while len(s)<11:
    i += 1
    t = dices_trial()
    s.add(t)
  return i

# b) Mediante una implementación en computadora,
#
# 1. Estime el valor medio y la desviación estándar del número de lanzamientos, repitiendo el algoritmo: 100, 1000, 10000 y 100000 veces.
#
# 2.Estime la probabilidad de que sea por lo menos 15 y la probabilidad de que sea a lo sumo 9, repitiendo el algoritmo: 100, 1000, 10000 y 100000.

for k in [int(x) for x in [1e2,1e3,1e4,1e5]]:
  initial_t = time()
  s,mean,_,_,std = simulate(N,
                            n_sim=k)
  print(f'| n_sim = {k}|')
  print(f'|tiempo = {round(time()-initial_t,5)}|')
  p_15 = np.sum(s >= 15)/k
  p_9 = np.sum(s <= 9)/k
  print(f'     media = {mean}')
  print(f'desviación = {std}')
  print(f'  P(N>=15) = {p_15}')
  print(f'   P(N<=9) = {p_9}')
  print('-----------------------------')
s,mean,_,_,std = simulate(N, n_sim=int(1e3))
binwidth = 12
sns.histplot(s,
             binwidth=binwidth,
             );

