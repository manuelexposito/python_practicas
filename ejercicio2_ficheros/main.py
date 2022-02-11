'''
1. Realizar una aplicación que sea capaz de transformar un fichero CSV en un fichero
 .sql con sentencias insert into.


- El nombre de la tabla sql será el nombre del fichero sin extensión.
- Las columnas de la tabla vendrán determinadas por la fila de encabezado.
- Como entrada, el programa recibirá un fichero csv con varias líneas, y como salida,
sea obtendrá un fichero con extensión .sql con tantos INSERT INTO.... como línea tuviera el CSV.




2. Realiza la herramienta inversa a la anterior, que reciba un fichero con una serie
 de sentencias INSERT INTO y lo transforme en un fichero .csv
'''
from io import open
import csv, sqlite3


#Ejercicio 1


archivo = "climatologia.csv"

'''
def convert_csv_to_sql(archivo):

    bd_fields =[]
    with open(archivo, "r", newline="\n", encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        for contacto in reader:
            contacto(0)

    bg_fields = reader.fieldnames

    nuevo_nombre_sql = {archivo[:-4]} + ".sql"

    create_table_text = f""" CREATE TABLE {archivo[:-4].upper()} (
    
    )"""
'''

with open("climatologia.csv", "r", newline="\n", encoding="utf8") as csvfile:
    tabla = []
    tupla = ()
    reader = csv.DictReader(csvfile)
    bg_fields = reader.fieldnames
    increment = 0
    for contacto in reader:

        tupla = contacto[bg_fields[2]]
        tabla.append(tupla)
        '''if increment < len(bg_fields):
            increment += 1
        else:
            increment = 0
'''
    print(tabla)

#Ejercicio 2