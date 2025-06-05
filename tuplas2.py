# Solicita ao usuário que insira as coordenadas geográficas
entrada = input("Digite a latitude e longitude separadas por vírgula: ")

# Converte a entrada em uma tupla de coordenadas
coordenadas = tuple(map(float, entrada.split(",")))

# Desempacota a tupla em latitude e longitude
latitude, longitude = coordenadas

# Exibe as coordenadas
print("\nCoordenadas geográficas:")
print(f"Latitude: {latitude}")
print(f"Longitude: {longitude}")
