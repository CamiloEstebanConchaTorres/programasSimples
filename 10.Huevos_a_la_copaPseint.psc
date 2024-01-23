Algoritmo Huevos_a_la_copa
	
	Definir TH Como Real
	Definir TE Como Real
	Definir M Como Real
	Definir P Como Real
	Definir C Como Real
	Definir K Como Real
	Definir Dividiendo Como Real
	Definir Divisor Como Real
	Definir Resultado Como Real
	Definir Resultado2 Como Real
	Definir _Segundos Como Real
	Definir Minutos Como Real
	Escribir "ingrese la temperatura original del huevo"
	Leer TH
	TE <- 100
	M  <- 47
	P  <- 1.038
	C  <- 3.7
	K  <- 0.0054
	Dividiendo <- (M ^ (2/3)) * (C * ((P ^ (1/3))))
	Divisor <- (K *  (3.14159265 ^ 2)) *  ((4 * 3.14159265) / (3 ^ (2/3)))
	Resultado <- Dividiendo / Divisor
	Resultado2 <- ln(0.76 * ((TH - TE) / (70 - TE)))
    _Segundos <- Resultado * Resultado2
	Minutos <-  _Segundos/60
	Imprimir "El tiempo maximo para prepararlo a la copa en segundos es: " _Segundos
	Imprimir "El tiempo maximo para prepararlo a la copa en minutos es: " Minutos
FinAlgoritmo
