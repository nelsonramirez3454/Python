'''Determinar a cuánto es igual el promedio entero de los elementos de la serie de
Fibonacci entre 0 y 1000.'''
try:
	num = 0
	aux = 0
	suma = 1
	cont = 0
	resultado = 1
	

	while suma < 987:
		aux = num 
		num = suma 
		suma = num + aux
		cont += 1
		resultado += suma
	promedio = resultado / cont
	print (f"El promedio es: {promedio}")
except ValueError:
	print ("ERROR")