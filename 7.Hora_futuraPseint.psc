Algoritmo Hora_futura
	Definir Hora_actual Como Real
	Definir Hora_transcurrida Como Real
	Definir Nueva_hora Como Real
	Escribir "ingrese la hora actual"
	Leer Hora_actual
	Escribir "ingrese las horas transcurridas"
	leer Hora_transcurrida
	Nueva_hora <- (Hora_actual + Hora_transcurrida) MOD 24
	Imprimir "la hora " Hora_actual " despues de " Hora_transcurrida " sera " Nueva_hora
FinAlgoritmo
