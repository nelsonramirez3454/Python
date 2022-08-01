'''Leer dos matrices 5x5 enteras y determinar si el promedio entero de los números
menores cada fila de una matriz corresponde a alguno de los datos almacenados en las
“esquinas” de la otra matriz.
'''
try:
	matriz1 = []
	matriz2 = []
	suma1 = 0
	cont1 = 0
	print('**PRIMERA MATRIZ**')
	for u in range(5):
		fila1 = []
		menor1 = 999999999999999999999999999999999
		for i in range(5):
			num1 = int(input('Digite un numero: '))
			if num1 < menor1:
				menor1 = num1
			fila1.append(num1)
		suma1 += menor1
		cont1 += 1
		matriz1.append(fila1)
	promedio1 = suma1 // cont1

	print('**SEGUNDA MATRIZ**')
	for o in range(5):
		fila2 = []
		menor2 = 999999999999999999999999999999999
		for p in range(5):
			num2 = int(input('Digite un numero: '))
			fila2.append(num2)
		matriz2.append(fila2)
	

	if promedio1 == matriz2[0][0] or promedio1 == matriz2[0][5] or promedio1 == matriz2[5][0] or promedio1 == matriz2[5][5]:
		print('El promedio de los menores de cada fila se encuentra en una de las esquinas')
	else:
		print('El promedio de los menores de cada fila NO esta en las esquinas')

	
except ValueError:
	print("ERROR")