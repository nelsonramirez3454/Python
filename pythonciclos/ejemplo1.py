''' multiplicar un numero por 2 mientras sea menor que 10. Inicie el numero en 1.'''
try:

	num = 1
	while num < 10:
		print (f"{num}")
		num *= 2
	
except ValueError:
	print ("Digite un valor valido")