'''Leer dos matrices 5x5 enteras y determinar si el promedio entero de los números
mayores de cada fila de una matriz es igual al promedio de los números mayores de cada fila
de la otra matriz.
'''
try:
	matriz1 = []
	matriz2 = []
	suma1 = 0
	suma2 = 0
	cont1 = 0
	cont2 = 0
	print('**PRIMERA MATRIZ**')
	for u in range(5):
		fila1 = []
		mayor1 = 0
		for i in range(5):
			num1 = int(input('Digite un numero: '))
			if num1 > mayor1:
				mayor1 = num1
			fila1.append(num1)
		suma1 += mayor1
		cont1 += 1
		matriz1.append(fila1)
	promedio1 = suma1 // cont1

	print('**SEGUNDA MATRIZ**')
	for o in range(5):
		fila2 = []
		mayor2 = 0
		for p in range(5):
			num2 = int(input('Digite un numero: '))
			if num2 > mayor2:
				mayor2 = num2
			fila2.append(num2)
		suma2 += mayor2
		cont2 += 1
		matriz2.append(fila2)
	promedio2 = suma2 // cont2
	

	if promedio1 == promedio2:
		print('El promedio de los mayores de cada fila es igual en ambas matrices')
	else:
		print('El promedio de los mayores de cada fila NO es igual en ambas matrices')

	
except ValueError:
	print("ERROR")