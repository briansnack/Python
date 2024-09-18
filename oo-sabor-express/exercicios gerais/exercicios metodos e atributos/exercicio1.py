class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

meu_carro = Carro(modelo="Kwid", cor="Prata", ano=2022)

print(f"{meu_carro.modelo} | {meu_carro.cor} | {meu_carro.ano}")
