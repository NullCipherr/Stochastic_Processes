# Dada uma matriz de transição P de uma cadeia de Markov com 6 estados, o código calcula a submatriz 
# de transição para os estados 1 a 4 ao remover os estados 0 e 5. A partir de um estado inicial 
# específico (estado 2), o código determina e armazena as probabilidades de estar em qualquer estado após 2, 3, 4, 5 e 6 passos. 
# Para isso, ele eleva a submatriz de transição a diferentes potências e calcula a probabilidade de atingir os estados a partir do 
# estado inicial, resultando em um dicionário com as probabilidades correspondentes para cada número de passos.

import numpy as np

def calculate_probabilities(P_sub, initial_state, steps):
    """
    Calcula a probabilidade de atingir todos os estados possíveis em uma submatriz após um número específico de transições.

    Parameters:
        P_sub (np.ndarray): Submatriz de transição.
        initial_state (np.ndarray): Vetor de distribuição inicial.
        steps (list of int): Lista de números de passos.

    Returns:
        dict: Dicionário com números de passos como chaves e probabilidades como valores.
    """
    probabilities = {}
    
    for k in steps:
        # Calcula a matriz de transição elevada à potência especificada
        Pk_sub = np.linalg.matrix_power(P_sub, k)
        
        # Calcula a probabilidade de atingir todos os estados
        prob = np.dot(initial_state, Pk_sub).sum()
        
        # Armazena o resultado no dicionário
        probabilities[k] = prob
    
    return probabilities

# Matriz de transição
P = np.array([
    [1, 0, 0, 0, 0, 0],
    [0.5, 0, 0.5, 0, 0, 0],
    [0, 0.5, 0, 0.5, 0, 0],
    [0, 0, 0.5, 0, 0.5, 0],
    [0, 0, 0, 0.5, 0, 0.5],
    [0, 0, 0, 0, 0, 1]
])

# Exclui os estados 0 e 5 para obter a submatriz
P_sub = P[1:5, 1:5]

# Define o estado inicial do vetor para o estado 2
initial_state = np.array([0, 1, 0, 0])

# Número de passos a serem considerados
steps = [2, 3, 4, 5, 6]

# Calcula as probabilidades
probabilities = calculate_probabilities(P_sub, initial_state, steps)

# Exibe as probabilidades
for k, prob in probabilities.items():
    print(f"Probabilidade de atingir todos os estados após {k} passos: {prob}")