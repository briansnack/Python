# Exercício 7, 8 e 9
from carro import Carro
from moto import Moto

# Instanciando carros
carro1 = Carro("Toyota", "Corolla", 4)
carro2 = Carro("Chevrolet", "Monza", 2)
carro3 = Carro("Volkswagen", "Golf", 4)

# Instanciando motos
moto1 = Moto("Harley-Davidson", "Street 750", "Esportiva")
moto2 = Moto("Honda", "CB 500", "Casual")
moto3 = Moto("Yamaha", "Mt-09", "Esportiva")

# Ligando veículos
carro1.ligar()
carro3.ligar()
moto1.ligar()

# Exibindo veículos
print("Carros:")
print(carro1)
print(carro2)
print(carro3)

print("\nMotos:")
print(moto1)
print(moto2)
print(moto3)