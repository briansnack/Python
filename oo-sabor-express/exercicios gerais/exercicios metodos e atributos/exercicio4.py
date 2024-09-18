class Restaurante:
    def __init__(self, nome, categoria,  capacidade, preco, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.capacidade = capacidade
        self.nota_avaliacao = preco
        self.ativo = ativo

    def __str__(self):
        return f'{self.nome} | {self.categoria}'

restaurante_formatado = Restaurante(nome="Bom Sabor", categoria="Tradicional",capacidade=100, preco=50)
print(restaurante_formatado)