
from vehiculo import Vehiculo

class Bicicleta(Vehiculo):

    def __init__(self, color, ruedas, tipo):
        Vehiculo.__init__(self, color, ruedas)
        self.tipo = tipo

    def __str__(self):
        #return super().__str__(self)\ + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada) + f"{self.tipo}"
        return f'Bicicleta : {}'