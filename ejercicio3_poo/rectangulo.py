

class Rectangulo():
    
    
    def __init__(self, punto_inicial = (0,0), punto_final = (0,0)):
       self.punto_inicial = punto_inicial
       self.punto_final = punto_final
        
    
    
    def base(self):
        
        #anchura, altura = self.punto_inicial.vector(self.punto_final)
 
        return self.punto_inicial.x - self.punto_final.x
    
    
    
    def altura(self):
        
        return self.punto_inicial.y - self.punto_final.y
        
    
    def area(self, base, altura):
        
        
        
        return base * altura / 2