# (Escriba un programa que reciba como entrada la temperatura original del huevo y muestre como salida el tiempo en 
#segundos que le toma alcanzar la temperatura máxima para prepararlo a la copa.)

import math

TH = float(input("Ingrese la temperatura original del huevo \n"))
TE = 100
M  = 47
P  = 1.038
C  = 3.7
K  = 0.0054


Dividiendo = math.pow(M, (2/3)) * (C * (math.pow(P,(1/3))))
Divisor    = (K * math.pow (math.pi, 2)) * math.pow ((4 * math.pi) / 3, (2/3))
Resultado  = Dividiendo / Divisor
Resultado2 = math.log(0.76 * ((TH - TE) / (70 - TE)))
Segundos   = Resultado * Resultado2
Minutos    = round(Segundos/60)

print (f"El tiempo maximo para prepararlo a la copa en segundos es: {round(Segundos)}")
print (f"El tiempo maximo para prepararlo a la copa en minutos es: {Minutos}")