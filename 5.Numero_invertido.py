# Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el número con los dígitos en orden inverso:

entero = str(input("ingrese el  valor del numero entero de tres digitos"))
invertir = ""
for i in range (len(entero)):
    invertir += entero [-(i+1)]
    print(f" inversamente es: {invertir}")


            