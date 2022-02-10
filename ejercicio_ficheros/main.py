
from io import open
import csv
#Lee el fichero y procésalo de tal manera que sea capaz de mostrar la temperatura máxima para una ciudad dada.
# Esa ciudad la debe poder recibir como un argumento de entrada. Si la ciudad no existe,
# se deberá manejar a través de una excepción.

def mostrar_temp_max(nombre_ciudad):
    
    list_temp_max = []
    
    with open("climatologia.csv", newline="\n", encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
       
        for tuplas in reader:
            if  nombre_ciudad in tuplas["provincia"]:
                    list_temp_max.append(float(tuplas["temperatura_maxima"]))
                    
        try:
            list_temp_max.sort()
            list_temp_max.reverse()
            print(list_temp_max[0])
        except:
            print("No se encontró esa ciudad.")
        
            

mostrar_temp_max("Alicante")