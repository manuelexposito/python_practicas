
from bicicleta import Bicicleta

class Motocicleta(Bicicleta):

    def __init__(self, color, ruedas, tipo, cilindrada, velocidad):
        Bicicleta.__init__(self, color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f"Color: {self.color}, ruedas: {self.ruedas}, tipo: {self.tipo}, cilindrada: {self.cilindrada}, velocidad: {self.velocidad}"

