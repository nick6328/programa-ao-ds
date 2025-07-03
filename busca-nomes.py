# Lista com pelo menos 8 nomes
nomes = ["Ana", "Bruno", "Carla", "Daniel", "Elaine", "Felipe", "Gabriela", "Henrique"]

# Solicita ao usuário uma letra ou sequência
sequencia = input("Digite uma letra ou sequência para filtrar os nomes: ").lower()

# Filtra os nomes com base na sequência, ignorando maiúsculas/minúsculas
nomes_filtrados = [nome for nome in nomes if sequencia in nome.lower()]

# Exibe os resultados
if nomes_filtrados:
    print("\nNomes encontrados:")
    for nome in nomes_filtrados:
        print(f"- {nome}")
else:
    print("\nNenhum nome encontrado com essa sequência.")
