'''Mostrar en pantalla la tabla de multiplicar del número 5.'''
try:
	j = 1
	for i in range(5,50+1,5):
		print (f"5 * {j} = {i}")
		j += 1
except ValueError:
	print ("ERROR")