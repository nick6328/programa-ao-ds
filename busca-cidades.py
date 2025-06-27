# a) Lista de cidades
cidades = [
    "Curitiba", "São Paulo", "Rio de Janeiro", "Belo Horizonte",
    "Fortaleza", "Salvador", "Manaus", "Porto Alegre"
]

# b) Solicita entrada do usuário
busca = input("Digite uma letra ou sequência de caracteres para buscar cidades: ").lower()

# c) Filtra cidades que contêm a sequência (ignorando maiúsculas/minúsculas)
resultado = [cidade for cidade in cidades if busca in cidade.lower()]

# d) Exibe o resultado
if resultado:
    print("Cidades encontradas:")
    for cidade in resultado:
        print("-", cidade)
else:
    print("Nenhuma cidade corresponde à sua busca.")
