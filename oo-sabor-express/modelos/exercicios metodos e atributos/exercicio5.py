print("Clientes:\n")
class Cliente:
    clientes = []
    
    def __init__(self, nome, sexo, altura, idade):
        self.nome = nome
        self.sexo = sexo
        self.altura = altura
        self.idade = idade
        Cliente.clientes.append(self)
        
    def __str__(self):
        return f"{self.nome} | {self.categora}"
    
    def listar_clientes():
        for cliente in Cliente.clientes:
            print(f"{cliente.nome} | {cliente.sexo} | {cliente.altura} | {cliente.idade}")
            
clienteH = Cliente("Marcelo", "Masculino", 1.65, 21)
clienteM = Cliente("Maria", "Feminino", 1.70, 20)

