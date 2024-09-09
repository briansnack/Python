class Restaurante:
    def __init__(self, nome, categoria):   
        self.nome = nome 
        self.categoria = categoria
        self.ativo = False
    
restaurante_praca = Restaurante("Praça", "Gourmet")
restaurante_pizza = Restaurante("Pizza Express", "Italiana")

restaurantes = [restaurante_praca, restaurante_pizza]

# dir mostra todos os atributos da classe
print(vars(restaurante_praca))
print(vars(restaurante_pizza))