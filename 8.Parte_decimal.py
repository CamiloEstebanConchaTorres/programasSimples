# Escriba un programa que entregue la parte decimal de un número real ingresado por el usuario.

numero_R = float(input("ingrese el valor del numero real que desea convertir a decimal \n"))
numero_D = numero_R % 1
print(f"el decimal del numero real {numero_R} es: {numero_D}")