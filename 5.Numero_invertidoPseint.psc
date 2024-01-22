Algoritmo Numero_invertido
	Definir _numero Como Real
	Definir _unidad Como Real
	Definir _decena Como Real
	Definir _centena Como Real
	Escribir "ingrese un numero de tres digitos"
	Leer _numero
	_centena <- _numero MOD 10 - 2
	_decena  <- (_numero MOD 100) MOD 10 - 1
	_unidad <- _numero MOD 10
	Imprimir "el numero " _numero " invertido seria: " _unidad _decena _centena
FinAlgoritmo
