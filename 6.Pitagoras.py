# Escriba un programa que reciba como entrada las longitudes de los dos catetos a
#  y b de un triángulo rectángulo, y que entregue como salida el largo de la hipotenusa c
#  del triangulo, dado por el teorema de Pitágoras: c2=a2+b2

import math

Cateto_A   = float(input("Ingrese el valor del cateto A \n"))
Cateto_B   = float(input("Ingrese el valor del cateto B \n"))
Pitagoras  = ((Cateto_A ** 2) + (Cateto_B ** 2))
Pitagoras2 = math.sqrt(Pitagoras)
print(f"la hipotenusa del triangulo es: {Pitagoras2}")