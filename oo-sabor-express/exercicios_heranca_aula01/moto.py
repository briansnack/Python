from veiculo import Veiculo

# Exercício 5 e 6
class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self._tipo = tipo

    def ligar(self):
        self._ligado = True

    def __str__(self):
        status = "ligado" if self._ligado else "desligado"
        return f"{self._marca} {self._modelo} - Tipo: {self._tipo} - Status: {status}"