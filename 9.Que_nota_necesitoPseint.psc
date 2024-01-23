Algoritmo Que_nota_necesito
	Definir Certamen1 Como Real
	Definir Certamen2 Como Real
	Definir NL Como Real
	Definir NC Como Real
	Definir NF Como Real
	Escribir "ingrese el valor del primer certamen"
	Leer Certamen1
	Escribir "ingrese el valor del segundo certamen"
	Leer Certamen2
	Escribir "ingrese el valor del laboratorio"
	Leer NL
	NC <- (Certamen1 + Certamen2) / 3
	NF <- (NC * 0.7) + (NL * 0.3)
	Imprimir "el usuario necesita la nota " NF " en el certamen 3"
FinAlgoritmo
