from abc import ABC, abstractmethod

# Exercício 1 e 2
class Veiculo(ABC):
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo
        self._ligado = False

    @abstractmethod
    def ligar(self):
        pass

    def __str__(self):
        status = "ligado" if self._ligado else "desligado"
        return f"{self._marca} {self._modelo} - Status: {status}"