from modelos.restaurante import Restaurante

restaurante_praca = Restaurante("Praça", "Gourmet")
restaurante_mexiacano = Restaurante("Mexican Food", "Mexicana")
restaurante_japones = Restaurante("Japa", "Japonesa")

restaurante_mexiacano.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()