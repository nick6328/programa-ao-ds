class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def registrar(self):
        return f"Nome: {self.nome}, Idade: {self.idade} anos"

class Cachorro(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca

    def registrar(self):
        return f"Nome: {self.nome}, Idade: {self.idade} anos, Raça: {self.raca}"

class Gato(Animal):
    def __init__(self, nome, idade, cor):
        super().__init__(nome, idade)
        self.cor = cor

    def registrar(self):
        return f"Nome: {self.nome}, Idade: {self.idade} anos, Cor: {self.cor}"

# Lista de animais atendidos
animais = [
    Cachorro("Rex", 5, "Labrador"),
    Gato("Mimi", 3, "Branco"),
    Cachorro("Bolt", 2, "Poodle"),
]

# Cadastro dos animais usando polimorfismo
for animal in animais:
    print(animal.registrar())
