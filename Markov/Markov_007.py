import numpy as np

"""
Dada uma cadeia de Markov com a matriz de transição P e um vetor de probabilidades iniciais P_X0, calcule a probabilidade de uma sequência específica de estados ocorrer.

Considere os seguintes elementos:
- Matriz de transição P
- Vetor de probabilidades iniciais P_X0
- Sequência desejada de estados

Calcule a probabilidade de que a sequência de estados especificada ocorra, começando com a probabilidade inicial de cada estado.
"""

def create_transition_matrix():
    """
    Cria a matriz de transição para a cadeia de Markov.

    Returns:
        np.ndarray: Matriz de transição.
    """
    return np.array([
        [0.5, 0.2, 0.2, 0.1],
        [0.3, 0.3, 0.2, 0.2],
        [0.3, 0.2, 0.2, 0.3],
        [0.0, 0.0, 0.0, 1.0]
    ])

def initial_probabilities():
    """
    Define as probabilidades iniciais para cada estado.

    Returns:
        np.ndarray: Vetor de probabilidades iniciais.
    """
    return np.array([0.5, 0.3, 0.2, 0])

def calculate_sequence_probability(P, P_X0, sequence):
    """
    Calcula a probabilidade de uma sequência específica de estados.

    Parameters:
        P (np.ndarray): Matriz de transição.
        P_X0 (np.ndarray): Vetor de probabilidades iniciais.
        sequence (list): Sequência desejada de estados.

    Returns:
        float: Probabilidade da sequência de estados.
    """
    prob = 0
    num_states = len(P_X0)
    
    for i in range(num_states):
        p = P_X0[i]
        for j in range(len(sequence)):
            if j == 0:
                p *= P[i, sequence[j]]
            else:
                p *= P[sequence[j-1], sequence[j]]
        prob += p
    
    return prob

def main():
    """
    Função principal para calcular e imprimir a probabilidade da sequência desejada.
    """
    # Cria a matriz de transição
    P = create_transition_matrix()
    
    # Define as probabilidades iniciais
    P_X0 = initial_probabilities()
    
    # Sequência desejada de estados
    sequence = [0, 1, 0, 2]
    
    # Calcula a probabilidade da sequência
    prob = calculate_sequence_probability(P, P_X0, sequence)
    
    # Imprime o resultado
    print(f"A probabilidade calculada é: {prob:.6f}")

# Executa a função principal
if __name__ == "__main__":
    main()