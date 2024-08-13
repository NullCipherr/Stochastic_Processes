# Exercicios
#
# ● Faça os estados 4 e 5 colapsarem num novo estado absorvente (digamos, no estado 4), e reescreva a matriz de probabilidades de transição (Q).
# ● Encontre a probabilidade de que após 6 passos, o processo atinja o estado 4 dado que iniciou no estado 0. Dito de outra forma, 
# qual a probabilidade do processo ser absorvido no máximo em 6 passos. Mais especicamente, Q6(04).
# ● Qual a probabilidade do processo ser absorvido exatamente no sexto passo? Ou seja, Q6(04) - Q5(04).

import numpy as np

# Matriz de transição Q após colapsar estados 4 e 5
Q = np.array([
    [0.6, 0.08, 0.08, 0.08, 0.16],
    [0.5, 0.1, 0.1, 0.1, 0.2],
    [0.4, 0.12, 0.12, 0.12, 0.24],
    [0.3, 0.14, 0.14, 0.14, 0.28],
    [0.0, 0.0, 0.0, 0.0, 1.0]
])

# Calculando Q^6
Q6 = np.linalg.matrix_power(Q, 6)

# Calculando Q^5
Q5 = np.linalg.matrix_power(Q, 5)

# Probabilidade de absorção em até 6 passos
prob_abs_6 = Q6[0, 4]

# Probabilidade de absorção exatamente no 6º passo
prob_exact_6 = Q6[0, 4] - Q5[0, 4]

print(f"Probabilidade de absorção em até 6 passos: {prob_abs_6:.4f}")
print(f"Probabilidade de absorção exatamente no 6º passo: {prob_exact_6:.4f}")