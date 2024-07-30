# Dado uma matriz de transição 𝑃 de uma cadeia de Markov, o código calcula 
# e imprime as probabilidades de estar no estado 2 em diferentes momentos (X3, X4) 
# a partir de diferentes estados iniciais (X1, X0), elevando a matriz P a diferentes potências (2, 3, 4) 
# para determinar as probabilidades de transição correspondentes.

import numpy as np

# Matriz de transição
P = np.array([[0.1, 0.2, 0.7],
              [0.2, 0.2, 0.6],
              [0.6, 0.1, 0.3]])

# Probabilidade de X3 = 2 dado X1 = 1
P_X3_2_given_X1_1 = np.linalg.matrix_power(P, 2)[1, 2]

# Probabilidade de X3 = 2 dado X0 = 1
P_X3_2_given_X0_1 = np.linalg.matrix_power(P, 3)[1, 2]

# Probabilidade de X4 = 2 dado X0 = 1
P_X4_2_given_X0_1 = np.linalg.matrix_power(P, 4)[1, 2]

print(f"P(X3 = 2 | X1 = 1) = {P_X3_2_given_X1_1}")
print(f"P(X3 = 2 | X0 = 1) = {P_X3_2_given_X0_1}")
print(f"P(X4 = 2 | X0 = 1) = {P_X4_2_given_X0_1}")