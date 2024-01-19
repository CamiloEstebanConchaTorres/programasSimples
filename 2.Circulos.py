#Escriba un programa que reciba como entrada el radio de un círculo y entregue como salida su perímetro y su área:

import math

radio = float(input("ingrese el valor del radio del circulo \n"))
perimetro = 2 * math.pi * radio
area = math.pi * radio**2

print(F"el perimetro del circulo es: {perimetro} \n el area del circulo es {area} ")
