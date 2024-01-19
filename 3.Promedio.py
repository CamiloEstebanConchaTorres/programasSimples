#Escriba un programa que calcule el promedio de 4 notas ingresadas por el usuario:

nota1 = float(input("ingrese el valor de la nota #1 \n"))
nota2 = float(input("ingrese el valor de la nota #2 \n"))
nota3 = float(input("ingrese el valor de la nota #3 \n"))
nota4 = float(input("ingrese el valor de la nota #4 \n"))
promedio = float(nota1 + nota2 + nota3 + nota4) / 4
print (f" la nota #1 es: {nota1} \n la nota #2 es: {nota2} \n la nota #3 es: {nota3} \n la nota #4 es: {nota4} \n")
print (f"el valor del promedio de las 4 notas es: {promedio}")