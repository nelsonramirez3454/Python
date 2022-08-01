'''Se define la serie de Fibonacci como la serie que comienza con los dígitos 1 y 0 y va
sumando progresivamente los dos últimos elementos de la serie, así:
0 1 1 2 3 5 8 13 21 34.......

Utilizando el concepto de ciclo generar la serie de Fibonacci hasta llegar o sobrepasas el
número 10000.'''
try:
	num = 0
	aux = 0
	suma = 1
	print ("0")
	print ("1")
	while suma < 10000:
		aux = num 
		num = suma 
		suma = num + aux
		print (suma)
except ValueError:
	print ("ERROR")