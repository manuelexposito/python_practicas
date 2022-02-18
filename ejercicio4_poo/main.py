
from vehiculo import Vehiculo
from coche import Coche
from bicicleta import Bicicleta
from camioneta import Camioneta
from motocicleta import Motocicleta
from tipo import Tipo

# Crea al menos un objeto de cada subclase y añádelos a una lista llamada vehiculos.
c1 = Coche("Rojo", 4, 200, 200)
b1 = Bicicleta("Azul", 2, "urbana")
c2 = Camioneta("Blanca", 4, 120, 200, 200)
m1 = Motocicleta("Verde", 2, "deportiva", 200, 200)

lista_vehiculos = (c1, b1, c2, m1)

# Realiza una función llamada catalogar() que reciba la lista de vehiculos y los
# recorra mostrando el nombre de su clase y sus atributos.
def catalogar(lista):

    for c in lista:
        print(c.__str__())


catalogar(lista_vehiculos)

'''
Modifica la función catalogar() para que reciba un argumento optativo ruedas,
haciendo que muestre únicamente los que su número de ruedas
concuerde con el valor del argumento. También debe mostrar
un mensaje "Se han encontrado {} vehículos con {} ruedas:
"únicamente si se envía el argumento ruedas.
 Ponla a prueba con 0, 2 y 4 ruedas como valor.
 
'''

def catalogar2(lista, ruedas= None):
    
    found_vehicle = []
    
    if ruedas != None:
        
        for c in lista:
            if c.ruedas == ruedas:
                found_vehicle.append(c)
        print(f"Se han encontrado {len(found_vehicle)} vehículos con {ruedas} ruedas.")
    
    else:
        return catalogar(lista)

catalogar2(lista_vehiculos, 0)
catalogar2(lista_vehiculos, 2)
catalogar2(lista_vehiculos, 4)
