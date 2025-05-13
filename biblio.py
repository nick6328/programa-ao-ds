class Livro:
    def __init__(self, titulo, autor, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas

    def __str__(self):
        return f"Livro: {self.titulo}\nAutor: {self.autor}\nPáginas: {self.num_paginas}"

# Solicita ao usuário os dados do livro
titulo = input("Digite o título do livro: ")
autor = input("Digite o nome do autor: ")
num_paginas = input("Digite o número de páginas: ")

# Cria um objeto da classe Livro
livro = Livro(titulo, autor, num_paginas)

# Exibe a descrição formatada do livro
print("\nDetalhes do livro cadastrado:")
print(livro)
