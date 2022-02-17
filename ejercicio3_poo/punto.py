
from cmath import sqrt
import math

class Punto():
    
    
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def cuadrante(self):
        
        if self.x > 0 and self.y > 0:
            return "Primer cuadrante"
        if self.x < 0 and self.y > 0:
            return "Segundo cuadrante"
        if self.x < 0 and self.y < 0:
            return "Tercer cuadrante"
        if self.x > 0 and self.y < 0:
            return "Cuarto cuadrante"
        else:
            return "Origen"
            
    def vector(self, punto):
        
        return {self.x - punto.x}, {self.y - punto.y}
    
    def distancia(self, punto):
        
        op = (self.x - punto.x)**2 + (self.y - punto.y)**2
        
        return math.sqrt(op)