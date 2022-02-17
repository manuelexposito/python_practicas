'''

Crea una clase llamada Punto con sus dos coordenadas X e Y.

Añade un método constructor para crear puntos fácilmente. Si no se reciben una coordenada, su valor será cero.

Sobreescribe el método string, para que al imprimir por pantalla un punto aparezca en formato (X,Y)

Añade un método llamado cuadrante que indique a qué cuadrante pertenece el punto,
teniendo en cuenta que si X == 0 e Y != 0 se sitúa sobre el eje Y, si X != 0 e Y == 0 se sitúa sobre el eje X y si X == 0 e Y == 0 está sobre el origen.

Añade un método llamado vector, que tome otro punto y calcule el vector resultante entre los dos puntos.

(Optativo) Añade un método llamado distancia, que tome otro punto y calcule la distancia entre los dos puntos y la muestre por pantalla. La fórmula es la siguiente:

Crea una clase llamada Rectangulo con dos puntos (inicial y final) que formarán la diagonal del rectángulo.

Añade un método constructor para crear ambos puntos fácilmente, si no se envían se crearán dos puntos en el origen por defecto.

Añade al rectángulo un método llamado base que muestre la base.

Añade al rectángulo un método llamado altura que muestre la altura.

Añade al rectángulo un método llamado area que muestre el area.
'''

import punto, rectangulo


a = punto.Punto(2, 3)

b = punto.Punto(5, 5)

c = punto.Punto(-3, -1)

d = punto.Punto(0, 0)

#Crea los puntos A(2, 3), B(5,5), C(-3, -1) y D(0,0) e imprimelos por pantalla.
print(a)
print(b)
print(c)
print(d)

 # Consulta a que cuadrante pertenecen el punto A, C y D.
print(a.cuadrante())
print(c.cuadrante())
print(d.cuadrante())

 # Consulta los vectores AB y BA.
print(a.vector(b))
print(b.vector(a))

 # (Optativo) Consulta la distancia entre los puntos 'A y B' y 'B y A'.
print(a.distancia(b))
print(b.distancia(a))


 # Crea un rectángulo utilizando los puntos A y B.
rect = rectangulo.Rectangulo(a, b)
 
 # Consulta la base, altura y área del rectángulo.
 
base = rect.base()
altura = rect.altura()

print(f"BASE -->{base}") 
print(f"ALTURA -->{altura}") 
print(f"AREA -->{rect.area(base, altura)}") 







