import json

# Define a classe Cliente
class Cliente:
    def __init__(self, id, nome, email, pagamentos=None):
        self.id = id
        self.nome = nome
        self.email = email
        self.pagamentos = pagamentos if pagamentos is not None else []

    # Converte o objeto Cliente em um dicionário
    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "pagamentos": self.pagamentos
        }

# Lista de pagamentos (exemplo)
pagamentos_cliente = [
    {"valor": 150.0, "data": "2025-09-01", "metodo": "Cartao de Credito"},
    {"valor": 200.0, "data": "2025-09-10", "metodo": "Pix"},
    {"valor": 75.5, "data": "2025-09-12", "metodo": "Boleto"}
]

# Crie um cliente com pagamentos
cliente = Cliente(1, "Joaquim Silva", "joaquim@email.com", pagamentos_cliente)

# Converta para JSON
cliente_json = json.dumps(cliente.to_dict(), indent=4)

# Imprime os dados em formato JSON
print(cliente_json)
