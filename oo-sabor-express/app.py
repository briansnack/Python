from modelos.restaurante import Restaurante

restaurante_praca = Restaurante("Praça", "Gourmet")
restaurante_praca.receber_avaliacao("Brian", 10)
restaurante_praca.receber_avaliacao("Lais", 8)
restaurante_praca.receber_avaliacao("Emy", 5)

def main():
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()