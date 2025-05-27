class Biblioteca:
    def __init__(self):
        self.livros = []  # Lista para armazenar os livros

    def adicionar_livro(self, titulo, autor, ano):
        livro = (titulo, autor, ano)  # Criando uma tupla com os dados do livro
        self.livros.append(livro)  # Adicionando automaticamente à lista

    def mostrar_colecao(self):
        for livro in self.livros:
            print(f'Título: {livro[0]}, Autor: {livro[1]}, Ano: {livro[2]}')

# Criando a biblioteca
biblioteca = Biblioteca()

# Adicionando livros à coleção
biblioteca.adicionar_livro("1984", "George Orwell", 1949)
biblioteca.adicionar_livro("Dom Casmurro", "Machado de Assis", 1899)
biblioteca.adicionar_livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)

# Exibindo a coleção de livros
print("\nColeção de Livros:")
biblioteca.mostrar_colecao()
