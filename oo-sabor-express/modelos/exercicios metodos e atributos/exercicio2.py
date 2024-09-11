class Restaurante:
    def __init__(self, nome, categoria, capacidade, preco, ativo=False):   
        self.nome = nome 
        self.categoria = categoria
        self.ativo = ativo
        self.capacidade = capacidade
        self.preco = preco
    
meu_restaurante = Restaurante(nome="Praça", categoria="Gourmet", ativo=True , capacidade=150, preco=79.99)

print(f"{meu_restaurante.nome} | {meu_restaurante.categoria} | {meu_restaurante.ativo} | {meu_restaurante.capacidade} | {meu_restaurante.preco}  ")