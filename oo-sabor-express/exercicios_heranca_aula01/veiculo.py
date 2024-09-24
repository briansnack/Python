# Exercício 1
class Veiculo:
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo
        self._ligado = False

# Exercício 2
    def __str__(self):
        status = "ligado" if self._ligado else "desligado"
        return (f"{self._marca}  {self._modelo} Status: {status}")