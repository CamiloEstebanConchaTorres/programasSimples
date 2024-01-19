# Escriba un programa que pregunte al usuario las notas de los dos primeros certamen y la nota de laboratorio,
#y muestre la nota que necesita el alumno para aprobar el ramo con nota final 60.

Certamen1 = float(input("Ingrese el valor del primer certamen \n"))
Certamen2 = float(input("Ingrese el valor del segundo certamen \n"))
NL        = float(input("Ingrese el valor del laboratorio \n"))
NC        = (Certamen1 + Certamen2) / 3
NF        = (NC * 0.7) + (NL * 0.3)
print(f"el usuario necesita la nota {NF} en el certamen 3")

