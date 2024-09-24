class Restaurante:
    def __init__(self, nome, categoria, ativo=False):   
        self.nome = nome 
        self.categoria = categoria
        self.ativo = ativo
        self.capacidade = 50
        self.preco = 19.9

    def __str__(self):
        return f"{self.nome} | {self.categoria} | Ativo: {self.ativo} | Capacidade: {self.capacidade} | Preço: {self.preco}"

novo_restaurante = Restaurante(nome="Pizza", categoria="Italiana")

print(novo_restaurante)