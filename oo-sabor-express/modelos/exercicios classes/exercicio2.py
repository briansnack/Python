class ContaBancaria:
    def __init__(self, titular="", saldo=0, ativo=False):
        self.titular = titular
        self.saldo = saldo
        self.ativo = ativo

    def __str__(self):
        return f"Olá {self.titular}! Seu saldo é de {self.saldo} reais."

        
# Criando instâncias da classe Pessoa
titular1 = ContaBancaria(titular="Alice", saldo=25, ativo=False)
titular2 = ContaBancaria(titular="Luiza", saldo=30, ativo=False)

print(titular1)
print(titular2)