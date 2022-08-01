'''Determinar a cuánto es igual la suma de los elementos de la serie de Fibonacci entre 0 y
100.'''
try:
	num = 0
	aux = 0
	suma = 1
	resultado = 1
	'''resultado de la suma de los snumeros que estan en la serie de Fibonacci
	resultado empieza en 1 para contar...'''

	while suma < 89:
		aux = num 
		num = suma 
		suma = num + aux
		resultado += suma
	print (f"El resultado de la suma de los numeros de la serie de Fibonacci ente 0 y 100 es igual a: {resultado}")
except ValueError:
	print ("ERROR")