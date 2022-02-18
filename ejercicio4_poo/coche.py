from vehiculo import Vehiculo

class Coche(Vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindrada):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f"Color: {self.color}, ruedas: {self.ruedas}, velocidad: {self.velocidad}, cilindrada: {self.cilindrada}"


