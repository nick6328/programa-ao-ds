import numpy as np
import matplotlib.pyplot as plt

# Parâmetros da simulação
anos = 10
simulacoes = 10  # Ajuste para melhor visualização do gráfico
retorno_medio = 0.07  # 7% ao ano
desvio_padrao = 0.20  # 20% de volatilidade
valor_inicial = 1000  # Valor inicial da carteira

# Gerar simulações
plt.figure(figsize=(10, 6))
for _ in range(simulacoes):
    valores = [valor_inicial]
    for _ in range(anos):
        retorno_anual = np.random.normal(retorno_medio, desvio_padrao)
        novo_valor = valores[-1] * (1 + retorno_anual)
        valores.append(novo_valor)
    plt.plot(range(anos + 1), valores, alpha=0.7)

# Configurações do gráfico
plt.xlabel('Anos')
plt.ylabel('Valor da Carteira')
plt.title('Simulação de Monte Carlo para Investimento em Ações')
plt.grid(True)
plt.show()
