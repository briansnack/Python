class Restaurante:  
    nome = "" 
    categoria = ""
    ativo = False
    
restaurante_praca = Restaurante()
restaurante_praca.nome = "Praça"
restaurante_praca.categoria = "Italiana"

restaurante_pizza = Restaurante()

restaurantes = [restaurante_praca, restaurante_pizza]

# dir mostra todos os atributos da classe
print(vars(restaurante_praca))