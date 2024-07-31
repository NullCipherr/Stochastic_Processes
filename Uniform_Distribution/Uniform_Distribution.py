import numpy as np
import matplotlib.pyplot as plt

"""
Enunciado:
Dada uma distribuição uniforme X ~ U(a, b), encontre:
1. E(X) - Valor esperado de X.
2. Var(X) - Variância de X.
3. F(x) - Função de Distribuição Acumulada (FDA) de X.
4. Faça um gráfico da FDA F(x).
"""

def mean_uniform(a, b):
    """
    Calcula o valor esperado (média) de uma distribuição uniforme U(a, b).
    
    Args:
        a (float): Limite inferior da distribuição uniforme.
        b (float): Limite superior da distribuição uniforme.
    
    Returns:
        float: Valor esperado E(X).
    """
    return (a + b) / 2

def variance_uniform(a, b):
    """
    Calcula a variância de uma distribuição uniforme U(a, b).
    
    Args:
        a (float): Limite inferior da distribuição uniforme.
        b (float): Limite superior da distribuição uniforme.
    
    Returns:
        float: Variância Var(X).
    """
    return ((b - a) ** 2) / 12

def F(x, a, b):
    """
    Calcula a Função de Distribuição Acumulada (FDA) para uma distribuição uniforme U(a, b).
    
    Args:
        x (float): Valor para o qual a FDA deve ser calculada.
        a (float): Limite inferior da distribuição uniforme.
        b (float): Limite superior da distribuição uniforme.
    
    Returns:
        float: Valor da FDA em x.
    """
    if x < a:
        return 0
    elif a <= x <= b:
        return (x - a) / (b - a)
    else:
        return 1

def plot_cdf(a, b):
    """
    Plota a Função de Distribuição Acumulada (FDA) para uma distribuição uniforme U(a, b).
    
    Args:
        a (float): Limite inferior da distribuição uniforme.
        b (float): Limite superior da distribuição uniforme.
    """
    # Valores x para o gráfico
    x_values = np.linspace(a - 2, b + 2, 400)
    y_values = [F(x, a, b) for x in x_values]

    # Plotar o gráfico da função de distribuição acumulada
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values, label='F(x)', color='b')
    plt.title(f'Função de Distribuição Acumulada F(x) para U({a}, {b})')
    plt.xlabel('x')
    plt.ylabel('F(x)')
    plt.axvline(a, color='r', linestyle='--', label=f'a = {a}')
    plt.axvline(b, color='g', linestyle='--', label=f'b = {b}')
    plt.legend()
    plt.grid(True)
    plt.show()

# Definir parâmetros
a = 3
b = 15

# Calcular o valor esperado e a variância
expected_value = mean_uniform(a, b)
variance = variance_uniform(a, b)

# Imprimir resultados
print(f"Valor esperado E(X): {expected_value:.2f}")
print(f"Variância Var(X): {variance:.2f}")

# Gerar o gráfico
plot_cdf(a, b)