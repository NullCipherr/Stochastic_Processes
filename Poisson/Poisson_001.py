import math
from scipy.stats import poisson

"""
Enunciado:
A quantidade de requisições para um certo servidor é um Processo de Poisson com lambda = 2 requisições/segundo.
Seja N(t) o número de requisições que chegam até o tempo t, calcule P[N(1)=2 | N(3)=6].
"""

def calculate_poisson_probability(rate, k):
    """
    Calcula a probabilidade de observar exatamente k eventos em um intervalo com a taxa de Poisson fornecida.
    
    Args:
        rate (float): Taxa de Poisson para o intervalo.
        k (int): Número de eventos desejados.
    
    Returns:
        float: Probabilidade de observar exatamente k eventos.
    """
    return poisson.pmf(k, rate)

def main():
    # Definindo os parâmetros
    lambda_rate = 2  # Taxa de Poisson (requisições por segundo)
    t1 = 1          # Tempo 1 segundo
    t3 = 3          # Tempo 3 segundos

    # Parâmetros da distribuição de Poisson
    lambda_t1 = lambda_rate * t1  # Parâmetro para N(1)
    lambda_t3 = lambda_rate * t3  # Parâmetro para N(3)
    
    # Calculando as probabilidades
    # P[N(1) = 2]
    P_N1_2 = calculate_poisson_probability(lambda_t1, 2)
    
    # P[N(3) = 6]
    P_N3_6 = calculate_poisson_probability(lambda_t3, 6)
    
    # P[N(3) - N(1) = 4 | N(1) = 2]
    # Isso é equivalente à probabilidade de 4 eventos entre t1 e t3 dado N(1) = 2
    P_N32_4_given_N1_2 = calculate_poisson_probability(lambda_rate * (t3 - t1), 4)
    
    # Probabilidade conjunta P[N(1) = 2 e N(3) = 6]
    P_joint = P_N1_2 * P_N32_4_given_N1_2
    
    # Probabilidade condicional P[N(1) = 2 | N(3) = 6]
    P_conditional = P_joint / P_N3_6
    
    # Imprimir resultados
    print(f"Probabilidade de N(1) = 2: {P_N1_2:.6f}")
    print(f"Probabilidade de N(3) = 6: {P_N3_6:.6f}")
    print(f"Probabilidade condicional P[N(1) = 2 | N(3) = 6]: {P_conditional:.6f}")

# Executar a função principal
if __name__ == "__main__":
    main()