from veiculo import Veiculo

# Exercício 3 e 4
class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self._portas = portas

    def ligar(self):
        self._ligado = True

    def __str__(self):
        status = "ligado" if self._ligado else "desligado"
        return f"{self._marca} {self._modelo} - Portas: {self._portas} - Status: {status}"