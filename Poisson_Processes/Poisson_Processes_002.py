import sympy as sp

"""
Enunciado:
Um carrinho de cachorro quente abre às 8h. A partir desse horário, os clientes parecem chegar, em média, a uma taxa cada vez maior até às 11h, ou seja, começa com 5 clientes por hora (às 8h) e chega a 20 clientes por hora (às 11h). Das 11h às 13h, a taxa parece ser constante em 20 clientes por hora. Entretanto, a chegada de clientes parece cair de hora em hora a partir das 13h até as 17h, momento em que atinge a taxa de 12 clientes por hora. Se assumirmos que o número de clientes que chegam durante períodos de tempo disjuntos são independentes:

a) Qual um bom modelo probabilístico para esse sistema?
b) Qual a probabilidade de nenhum cliente chegar entre 8h30 e 9h30?
c) Qual o valor esperado neste período (8h30 a 9h30)?
"""

# Define variável de tempo t globalmente
t = sp.symbols('t')

def define_lambda(t):
    """
    Define a função lambda(t) para o intervalo de 8h às 11h.
    A taxa lambda(t) aumenta linearmente de 5 para 20 clientes por hora.
    
    Args:
        t (sympy.Symbol): A variável de tempo.
    
    Returns:
        sympy.Expr: A função lambda(t).
    """
    return 5 + 5 * (t - 8)

def calculate_integral_lambda(lambda_t, start_time, end_time):
    """
    Calcula a integral da função lambda(t) sobre um intervalo de tempo.
    
    Args:
        lambda_t (sympy.Expr): A função lambda(t).
        start_time (float): O início do intervalo de tempo.
        end_time (float): O fim do intervalo de tempo.
    
    Returns:
        sympy.Expr: O valor da integral.
    """
    return sp.integrate(lambda_t, (t, start_time, end_time))

def calculate_prob_no_customer(integral_lambda):
    """
    Calcula a probabilidade de nenhum cliente chegar usando a fórmula de Poisson.
    
    Args:
        integral_lambda (sympy.Expr): O valor da integral lambda(t).
    
    Returns:
        sympy.Expr: A probabilidade de nenhum cliente chegar.
    """
    return sp.exp(-integral_lambda)

def main():
    """
    Função principal que organiza o fluxo do programa, chama as funções e imprime os resultados.
    """
    # Definir variável de tempo t
    t = sp.symbols('t')

    # Definir a função lambda(t) para o intervalo de 8h às 11h
    lambda_t = define_lambda(t)

    # Calcular a integral de lambda(t) de 8h30 a 9h30
    integral_lambda = calculate_integral_lambda(lambda_t, 8.5, 9.5)

    # Calcular a probabilidade de nenhum cliente chegar
    prob_no_customer = calculate_prob_no_customer(integral_lambda)

    # Valor esperado no intervalo de 8h30 a 9h30
    expected_value = integral_lambda

    # Avaliar resultados
    prob_no_customer_value = prob_no_customer.evalf()
    expected_value_value = expected_value.evalf()

    # Imprimir resultados
    print(f"Valor esperado no intervalo de 8h30 a 9h30: {expected_value_value:.2f}")
    print(f"Probabilidade de nenhum cliente chegar entre 8h30 e 9h30: {prob_no_customer_value:.6f}")

# Executa a função principal
if __name__ == "__main__":
    main()