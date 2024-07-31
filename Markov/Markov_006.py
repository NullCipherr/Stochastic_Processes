import numpy as np

"""
Quando um dígito binário é transferido através de um sistema de
comunicação, ele passa por vários estágios. Em cada estágio existe uma
probabilidade p de que o dígito seja transmitido com erro. Seja Xn o dígito
que é a saída no enésimo estágio. Então, {Xn: n>=0} é uma cadeia de Markov.
Determine:
a) A matriz de probabilidade de transição.
b) Se o dígito enviado é 0, qual a probabilidade que nenhum erro ocorra até o
segundo estágio.
c) Se o dígito enviado é 0, qual a probabilidade de uma mensagem correta
ser recebida do estágio 2 ao estágio 4.
"""

def transition_matrix(p):
    """
    Cria a matriz de transição para a cadeia de Markov.

    Parameters:
        p (float): Probabilidade de erro na transmissão.

    Returns:
        np.ndarray: Matriz de transição.
    """
    return np.array([
        [1 - p, p],
        [p, 1 - p]
    ])

def probability_no_error_until_stage(P, initial_state, stages):
    """
    Calcula a probabilidade de não ocorrer erro até um determinado estágio.

    Parameters:
        P (np.ndarray): Matriz de transição.
        initial_state (np.ndarray): Vetor de distribuição inicial.
        stages (int): Número de estágios.

    Returns:
        float: Probabilidade de não ocorrer erro até o estágio especificado.
    """
    P_stages = np.linalg.matrix_power(P, stages)
    return np.dot(initial_state, P_stages[0, :]).sum()

def probability_correct_message(P, initial_state, start_stage, end_stage):
    """
    Calcula a probabilidade de receber uma mensagem correta do estágio inicial ao estágio final.

    Parameters:
        P (np.ndarray): Matriz de transição.
        initial_state (np.ndarray): Vetor de distribuição inicial.
        start_stage (int): Estágio inicial.
        end_stage (int): Estágio final.

    Returns:
        float: Probabilidade de receber uma mensagem correta entre os estágios especificados.
    """
    P_stages = np.linalg.matrix_power(P, end_stage - start_stage + 1)
    return np.dot(initial_state, np.dot(P_stages, initial_state))

# Probabilidade de erro
p = 0.1  # Exemplo: 10% de erro

# Matriz de transição
P = transition_matrix(p)

# Estado inicial (dígito 0)
initial_state = np.array([1, 0])  # Começa com 100% de probabilidade no estado 0

# a) Matriz de probabilidade de transição
print("Matriz de probabilidade de transição:")
print(P)

# b) Probabilidade de nenhum erro ocorrer até o segundo estágio
prob_no_error_2 = probability_no_error_until_stage(P, initial_state, stages=2)
print(f"Probabilidade de nenhum erro ocorrer até o segundo estágio: {prob_no_error_2}")

# c) Probabilidade de uma mensagem correta ser recebida do estágio 2 ao estágio 4
prob_correct_message_2_to_4 = probability_correct_message(P, initial_state, start_stage=2, end_stage=4)
print(f"Probabilidade de uma mensagem correta ser recebida do estágio 2 ao estágio 4: {prob_correct_message_2_to_4}")