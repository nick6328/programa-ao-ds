import functools

class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def __repr__(self):
        return f'{self.nome}: {self.nota}'

def comparar_alunos(a, b):
    return (a.nota > b.nota) - (a.nota < b.nota)

# Criando a lista de alunos com entrada do usuário
alunos = []
for i in range(3):
    nome = input(f"Informe o nome do aluno {i+1}: ")
    nota = int(input(f"Informe a nota de {nome}: "))
    alunos.append(Aluno(nome, nota))

# Ordenando os alunos pela nota
alunos_ordenados = sorted(alunos, key=functools.cmp_to_key(comparar_alunos))

print("\nAlunos ordenados:")
print(alunos_ordenados)
