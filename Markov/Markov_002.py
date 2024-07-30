# Dado uma matriz de transição P de uma cadeia de Markov, o código calcula e imprime as matrizes 
# de transição elevadas à terceira e quarta potências (𝑃3 e P4), e determina as probabilidades de 
# estar no estado 1 após 3 e 4 passos, começando do estado 0. Isso é feito elevando a matriz P às 
# potências apropriadas e extraindo os elementos relevantes das matrizes resultantes.

import numpy as np

# Matriz de transição
P = np.array([
    [0, 0.6, 0.4],
    [0.6, 0, 0.4],
    [0.6, 0.4, 0]
])

P3 = np.linalg.matrix_power(P, 3)

print("P^3")
print(P3)

# Pular linha
print()

P4 = np.linalg.matrix_power(P, 4)
print("P^4")
print(P4)

print()

print("P_X3_1_given_X0_1 and P_X4_1_given_X0_1 ") 
P_X3_1_given_X0_1 = P3[0, 0]
P_X4_1_given_X0_1 = P4[0, 0]

P_X3_1_given_X0_1, P_X4_1_given_X0_1