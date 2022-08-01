'''Si 32768 es el tope superior para los números entero cortos, determinar cuál es el
número primo más cercano por debajo de él.'''
try:

	for i in range(32767,1,-2):
		multiplos = 0
		for j in range(2, (i//2)):
			if i % j == 0:
				multiplos += 1

		if multiplos == 0:
			print (f"El numero primo mas cercano a 32768 es {i}")
			break;

except ValueError:
	print ("ERROR")
