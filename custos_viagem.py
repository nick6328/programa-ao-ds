class Veiculo:
    def __init__(self, nome, custo_por_km):
        self.nome = nome
        self.custo_por_km = custo_por_km

    def calcular_custo(self, distancia):
        return self.custo_por_km * distancia

class Carro(Veiculo):
    pass  # Usa o mesmo método da classe pai

class Bicicleta(Veiculo):
    def calcular_custo(self, distancia):
        return 0  # Bicicletas não têm custo por km

class Caminhao(Veiculo):
    pass  # Usa o mesmo método da classe pai

def calcular_custo_total(veiculos, distancia):
    custo_total = 0
    for veiculo in veiculos:
        custo_total += veiculo.calcular_custo(distancia)
        print(f"{veiculo.nome}: R${veiculo.calcular_custo(distancia):.2f}")
    print(f"Custo total da viagem: R${custo_total:.2f}")

# Lista de veículos
veiculos = [
    Carro("Carro", 0.5),
    Bicicleta("Bicicleta", 0.0),
    Caminhao("Caminhão", 1.2),
]

# Calcular custo total para 200 km
calcular_custo_total(veiculos, 200)
