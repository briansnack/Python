class ContaBancaria:
    def __init__(self, titular="", saldo=0, ativo=False):
        self.titular = titular
        self.saldo = saldo
        self.ativo = ativo

    def __str__(self):
        return f"Olá {self.titular}! Seu saldo é de {self.saldo} reais."

    def ativar_conta(self):
        self.ativo=True
    
# Criando instâncias da classe Pessoa
titular1 = ContaBancaria(titular="Alice", saldo=25, ativo=False)
titular2 = ContaBancaria(titular="Luiza", saldo=30, ativo=False)

# Ativando a conta de titular1 
titular1.ativar_conta()

print(titular1)
print(titular2)
print("\n")
print(f"A conta de {titular1.titular} está ativa? {titular1.ativo}")
print(f"A conta de {titular2.titular} está ativa? {titular2.ativo}")