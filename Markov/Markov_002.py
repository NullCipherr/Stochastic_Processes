# Dado uma matriz de transição P de uma cadeia de Markov, o código calcula e imprime as matrizes 
# de transição elevadas à terceira e quarta potências (𝑃3 e P4), e determina as probabilidades de 
# estar no estado 1 após 3 e 4 passos, começando do estado 0. Isso é feito elevando a matriz P às 
# potências apropriadas e extraindo os elementos relevantes das matrizes resultantes.

import numpy as np

def print_matrix_power(matrix, power):
    """
    Calcula e imprime a matriz elevada à potência especificada.
    
    Parameters:
        matrix (np.ndarray): Matriz de transição.
        power (int): Potência à qual a matriz deve ser elevada.
    """
    # Calcula a matriz elevada à potência especificada
    result = np.linalg.matrix_power(matrix, power)
    
    # Imprime a matriz resultante
    print(f"P^{power}")
    print(result)
    print()  # Linha em branco para separar as saídas

# Matriz de transição
P = np.array([
    [0, 0.6, 0.4],
    [0.6, 0, 0.4],
    [0.6, 0.4, 0]
])

# Imprime a matriz P^3
print_matrix_power(P, 3)

# Imprime a matriz P^4
print_matrix_power(P, 4)