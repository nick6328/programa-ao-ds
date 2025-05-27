class Calculadora:
    @staticmethod
    def somar(a, b):
        return a + b

    @staticmethod
    def subtrair(a, b):
        return a - b

# Testando os métodos estáticos
print("Soma:", Calculadora.somar(5, 3))
print("Subtração:", Calculadora.subtrair(10, 4))
