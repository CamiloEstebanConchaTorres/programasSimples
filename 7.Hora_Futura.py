# Escriba un programa que pregunte al usuario la hora actual t del reloj y un número entero de horas h, que indique qué hora marcará el reloj dentro de h horas:

Hora_actual = float(input("ingrese la hora actual \n"))
hora_transcurrida = int(input("ingrese las horas transcurridas \n"))
Nueva_hora = (Hora_actual + hora_transcurrida) % 24
print (f"la hora {Hora_actual} despues de {hora_transcurrida} horas sera: {Nueva_hora}")
