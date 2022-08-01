'''Determinar cuántos elementos de la serie de Fibonacci se encuentran entre 1000 y 2000.'''
try:
	num = 0
	aux = 0
	suma = 1
	cont = 0


	while suma < 2000:
		aux = num 
		num = suma 
		suma = num + aux
		if suma < 2000 and suma > 1000:
			cont += 1
	print (f"Hay {cont} elementos")
except ValueError:
	print ("ERROR")