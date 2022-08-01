'''Leer una matriz 5x5 y determinar si el promedio de los elementos que se encuentran en
su diagonal está almacenado en ella. Mostrar en pantalla en qué posiciones exactas se
encuentra dicho dato.
'''
try:
	matriz1 = []
	suma1 = 0
	cont = 0
	cont1 = 0
	print('**MATRIZ**')
	for u in range(5):
		fila1 = []
		for i in range(5):
			num1 = int(input('Digite un numero: '))
			if u == i:
				suma1 += num1
				cont1 += 1
			fila1.append(num1)
		matriz1.append(fila1)
	promedio1 = suma1 // cont1

	posx = 0
	posy = 0

	for i in range(len(matriz1)):
		for j in range(len(matriz1)):
			if matriz1[i][j] == promedio1:
				cont += 1
				posx = i
				posy = j

	for m in range(len(matriz1)):
		print(matriz1[m])

	if cont == 1:
		print(f'El promedio de la diagonal esta en {posx}, {posy}')
	else:
		print('El promedio de la diaginal no esta en la matriz')

	
except ValueError:
	print("ERROR")