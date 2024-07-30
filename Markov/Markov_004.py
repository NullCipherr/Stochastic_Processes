# Dada uma matriz de transição 𝑃 de uma cadeia de Markov com 4 estados, o código calcula a matriz de transição 
# após 4 passos (𝑃4) e determina a probabilidade de não atingir o estado 3 após 4 transições, começando no estado 0. 
# Para isso, ele eleva a matriz 𝑃 à quarta potência e soma as probabilidades de permanecer nos estados 0, 1 e 2 após 4 passos.

import numpy as np

# Matriz de transição
P = np.array([[0.4, 0.3, 0.2, 0.1],
              [0, 0.6, 0.2, 0.2],
              [0, 0, 0.7, 0.3],
              [0, 0, 0, 1]])

# Calculando P^4
P_4 = np.linalg.matrix_power(P, 4)

# Probabilidade de não atingir o estado 3 após 4 transições, começando no estado 0
prob_nao_atingir_3 = P_4[0, 0] + P_4[0, 1] + P_4[0, 2]

print(f"Probabilidade de não atingir o estado 3 após 4 transições: {prob_nao_atingir_3}")