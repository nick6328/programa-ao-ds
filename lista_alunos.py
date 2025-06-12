# Lista de alunos (nome, nota)
alunos = [
    ("Carlos", 8.5),
    ("Ana", 9.2),
    ("Bruno", 7.8),
    ("Mariana", 9.5),
    ("Eduardo", 8.9)
]

# Ordenação por nome (modifica a lista original)
alunos.sort(key=lambda x: x[0])

print("Ordenados por nome:")
print(alunos)

# Ordenação por nota em ordem decrescente (gera uma nova lista)
alunos_por_nota = sorted(alunos, key=lambda x: x[1], reverse=True)

print("\nOrdenados por nota decrescente:")
print(alunos_por_nota)
