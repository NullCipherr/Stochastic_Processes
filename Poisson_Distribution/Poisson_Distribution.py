import numpy as np
from scipy.stats import poisson

"""
Enunciado:
Distribuição de Poisson

No experimento de Rutherford contou-se o número de partículas alfa emitidas por uma substância radioativa em 2608 intervalos de 7.5 segundos. As frequências observadas são:

_______________
k       n(k)
_______________
0        57
1       203
2       383
3       525
4       532
5       408
6       273
7       139
8        45
9        27
>9      16
_______________

Obter as frequências esperadas para cada valor de k e para k > 9 usando a distribuição de Poisson.
"""

# Dados fornecidos
intervalos = 2608
total_emissoes = 10086  # Soma das frequências observadas
lambda_ = total_emissoes / intervalos  # Taxa média de Poisson

# Frequências observadas
frequencias_observadas = [57, 203, 383, 525, 532, 408, 273, 139, 45, 27, 16]

# Cálculo das frequências esperadas
# Frequências esperadas para k = 0 a 9
frequencias_esperadas = [intervalos * poisson.pmf(k, lambda_) for k in range(10)]

# Adicionar a frequência esperada para k >= 10
frequencias_esperadas.append(intervalos * (1 - poisson.cdf(9, lambda_)))

# Salvar frequências esperadas em um arquivo de texto
np.savetxt('frequencias_esperadas.txt', frequencias_esperadas, fmt='%.2f')

print("Frequências esperadas foram calculadas e salvas em 'frequencias_esperadas.txt'.")