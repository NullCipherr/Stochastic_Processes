# Dada uma matriz de transição 𝑃 de uma cadeia de Markov com 3 estados, onde P representa as probabilidades de 
# transição entre esses estados, calcule a matriz de transição após 3 passos (P3) e determine a distribuição de 
# probabilidades dos estados após 3 passos partindo de uma distribuição inicial uniforme 𝜋0.

import numpy as np

def print_matrix(matrix, title):
    """
    Imprime a matriz com um título.

    Parameters:
        matrix (np.ndarray): Matriz a ser impressa.
        title (str): Título para a matriz.
    """
    print(title)
    print(matrix)
    print()  # Linha em branco para separar as saídas

def print_vector(vector, title):
    """
    Imprime o vetor com um título.

    Parameters:
        vector (np.ndarray): Vetor a ser impresso.
        title (str): Título para o vetor.
    """
    print(title)
    print(vector)
    print()  # Linha em branco para separar as saídas

# Matriz de transição
P = np.array([
    [0.1, 0.2, 0.7],
    [0.9, 0.1, 0],
    [0.1, 0.8, 0.1]
])

# Calcula a matriz P^3
P3 = np.linalg.matrix_power(P, 3)

# Imprime a matriz P^3
print_matrix(P3, "P^3")

# Vetor de distribuição inicial
pi_0 = np.array([1/3, 1/3, 1/3])

# Imprime o vetor pi^0
print_vector(pi_0, "pi^0")

# Calcula o vetor pi^3 = pi^0 * P^3
pi_3 = np.dot(pi_0, P3)

# Imprime o vetor pi^3
print_vector(pi_3, "pi^3")