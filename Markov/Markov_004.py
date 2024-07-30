# Dada uma matriz de transição 𝑃 de uma cadeia de Markov com 4 estados, o código calcula a matriz de transição 
# após 4 passos (𝑃4) e determina a probabilidade de não atingir o estado 3 após 4 transições, começando no estado 0. 
# Para isso, ele eleva a matriz 𝑃 à quarta potência e soma as probabilidades de permanecer nos estados 0, 1 e 2 após 4 passos.

import numpy as np

def calculate_probability_of_not_reaching_state(P, initial_state, target_state, steps):
    """
    Calcula a probabilidade de não atingir o estado alvo após um número específico de transições.

    Parameters:
        P (np.ndarray): Matriz de transição.
        initial_state (int): Estado inicial.
        target_state (int): Estado alvo.
        steps (int): Número de transições.

    Returns:
        float: Probabilidade de não atingir o estado alvo.
    """
    # Calcula a matriz de transição elevada à potência especificada
    P_steps = np.linalg.matrix_power(P, steps)
    
    # Calcula a probabilidade de não atingir o estado alvo
    prob_not_reaching = np.sum(P_steps[initial_state, :]) - P_steps[initial_state, target_state]
    
    return prob_not_reaching

# Matriz de transição
P = np.array([
    [0.4, 0.3, 0.2, 0.1],
    [0, 0.6, 0.2, 0.2],
    [0, 0, 0.7, 0.3],
    [0, 0, 0, 1]
])

# Calcula a probabilidade de não atingir o estado 3 após 4 transições, começando no estado 0
prob_nao_atingir_3 = calculate_probability_of_not_reaching_state(P, initial_state=0, target_state=3, steps=4)

# Imprime o resultado
print(f"Probabilidade de não atingir o estado 3 após 4 transições: {prob_nao_atingir_3}")