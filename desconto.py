# Solicita o preço do produto
preco = float(input("Digite o preço do produto: "))

# Solicita o código de desconto
codigo = input("Digite o código de desconto (A, B ou C): ").upper()

# Define os descontos baseados no código
descontos = {
    "A": 0.10,  # 10% de desconto
    "B": 0.20,  # 20% de desconto
    "C": 0.30   # 30% de desconto
}

# Verifica se o código é válido e calcula o preço final
if codigo in descontos:
    desconto = descontos[codigo]
    preco_final = preco * (1 - desconto)
    print(f"O preço final com desconto é: R${preco_final:.2f}")
else:
    print("Código de desconto inválido.")
