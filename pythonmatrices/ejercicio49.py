'''Leer una matriz 3x3 entera y determinar si el promedio de todos los datos almacenados
en ella se encuentra también almacenado.
'''
try:
	matriz1 = []
	suma1 = 0
	cont1 = 0
	print('**MATRIZ**')
	for u in range(3):
		fila1 = []
		for i in range(3):
			num1 = int(input('Digite un numero: '))
			suma1 += num1
			cont1 += 1
			fila1.append(num1)
		matriz1.append(fila1)
	promedio1 = suma1 // cont1

	for i in range(len(matriz1)):
		for j in range(len(matriz)):
			if matriz1[i][j] == promedio1:
				cont += 1

	if cont > 0:
		print('El promedio de todos los numeros esta en la matriz')
	else:
		print('El promedio de todos los numeros no esta en la matriz')

	
except ValueError:
	print("ERROR")