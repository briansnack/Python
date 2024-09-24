# Exercício 3
from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self._portas = portas
        
# Exercício 4
    def __str__(self):
        status = "ligado" if self._ligado else "desligado"
        return (f"{self._marca}  {self._modelo} - Portas: {self._portas} - Status: {status}")