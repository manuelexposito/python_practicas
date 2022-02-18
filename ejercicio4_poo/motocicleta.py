
from bicicleta import Bicicleta

class Motocicleta(Bicicleta):

    def __init__(self, color, ruedas, tipo, cilindrada, velocidad):
        Bicicleta.__init__(self, color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__(self)\
               + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada) + f"{self.tipo}"

