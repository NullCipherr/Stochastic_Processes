# Dada uma matriz de transição P de uma cadeia de Markov com 6 estados, o código calcula a submatriz 
# de transição para os estados 1 a 4 ao remover os estados 0 e 5. A partir de um estado inicial 
# específico (estado 2), o código determina e armazena as probabilidades de estar em qualquer estado após 2, 3, 4, 5 e 6 passos. 
# Para isso, ele eleva a submatriz de transição a diferentes potências e calcula a probabilidade de atingir os estados a partir do 
# estado inicial, resultando em um dicionário com as probabilidades correspondentes para cada número de passos.

import numpy as np

# Matriz de transição
P = np.array([[1, 0, 0, 0, 0, 0],
 [0.5, 0, 0.5, 0, 0, 0],
 [0, 0.5, 0, 0.5, 0, 0],
 [0, 0, 0.5, 0, 0.5, 0],
 [0, 0, 0, 0.5, 0, 0.5],
 [0, 0, 0, 0, 0, 1]])

# Exclui os estados 0 e 5 para obtermos a submatriz
P_sub = P[1:5, 1:5]

# Define o estado inicial do vetor para o estado 2
initial_state = np.array([0, 1, 0, 0])

# Numero de passos k
steps = [2, 3, 4, 5, 6]

probabilities = {}

# Calcula a probabilidade para cada passo
for k in steps:
  Pk_sub = np.linalg.matrix_power(P_sub, k)
  prob = np.dot(initial_state, Pk_sub).sum()
  probabilities[k] = prob

probabilities