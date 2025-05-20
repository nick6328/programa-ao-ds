# Solicita um número inteiro positivo n
n = int(input("Digite a quantidade de números que deseja inserir na lista: "))

# Cria uma lista vazia
lista = []

# Lê n números inteiros e os adiciona à lista
for _ in range(n):
    num = int(input("Digite um número inteiro: "))
    lista.append(num)

# Solicita um número inteiro x
x = int(input("Digite o número que deseja verificar na lista: "))

# Verifica se x está na lista
if x in lista:
    print(f"O número {x} está na lista.")
else:
    print(f"O número {x} não está na lista.")
