'''Generar todas las tablas de multiplicar del 1 al 10.'''
try:
	for i in range(1,10+1):
		print ("")
		for j in range(1,10+1):
			producto = i * j
			print (f"{i} * {j} = {producto}")
except ValueError:
	print ("ERROR")