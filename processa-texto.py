# Lista com 10 títulos de livros
colecao_livros = [
    "Cem Anos de Solidão",
    "Dom Casmurro",
    "O Pequeno Príncipe",
    "Orgulho e Preconceito",
    "A Revolução dos Bichos",
    "O Senhor dos Anéis",
    "A Menina que Roubava Livros",
    "Grande Sertão: Veredas",
    "Harry Potter e a Pedra Filosofal",
    "Memórias Póstumas de Brás Cubas"
]

# Solicita uma palavra-chave ao usuário
busca = input("Digite uma palavra-chave para buscar nos títulos: ").lower()

# Filtra títulos que contêm a palavra-chave
resultados = [livro for livro in colecao_livros if busca in livro.lower()]

# Exibe os resultados
if resultados:
    print("\nTítulos encontrados:")
    for titulo in resultados:
        print("-", titulo)
else:
    print("\nNenhum título corresponde à sua busca.")
