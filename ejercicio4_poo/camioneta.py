

from coche import Coche

class Camioneta(Coche):

    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        Coche.__init__(self, color, ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return super().__str__(self)\
               + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)\
               + f"{self.carga}"
