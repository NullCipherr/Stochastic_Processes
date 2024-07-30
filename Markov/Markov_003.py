# Dada uma matriz de transição 𝑃 de uma cadeia de Markov com 3 estados, onde P representa as probabilidades de 
# transição entre esses estados, calcule a matriz de transição após 3 passos (P3) e determine a distribuição de 
# probabilidades dos estados após 3 passos partindo de uma distribuição inicial uniforme 𝜋0.

import numpy as np

# Matriz de transição
P = np.array([
    [0.1, 0.2, 0.7],
    [0.9, 0.1, 0],
    [0.1, 0.8, 0.1]
])

P3 = np.linalg.matrix_power(P, 3)

print("P^3")
print(P3)

# Pular linha
print()

pi_0 = np.array([1/3, 1/3, 1/3])

print("pi^0")
print(pi_0)

# Pular linha
print()

pi_3 = np.dot(pi_0, P3)
print("pi^3")
print(pi_3)