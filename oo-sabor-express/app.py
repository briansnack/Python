from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante("Praça", "Gourmet")
bebida_suco = Bebida("Suco de Melancia", 5, "Grande")
prato_paozinho = Prato("Paozinho", 2, "O melhor pão da cidade")
restaurante_praca.adicionar_bebida_no_cardapio(bebida_suco)
restaurante_praca.adicionar_prato_no_cardapio(prato_paozinho)

def main():
    print(bebida_suco)
    print(prato_paozinho)

if __name__ == "__main__":
    main()