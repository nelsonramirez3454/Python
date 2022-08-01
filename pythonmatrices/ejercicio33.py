'''Leer una matriz 4x6 entera y determinar en qué posiciones están los menores pares por
fila.'''
mat = []
try:
	for i in range(4):
		fila = []
		for j in range (6):
			num = int(input('Ingrese un numero: '))
			fila.append(num)
		mat.append(fila)
	print(mat)
	pos1 = 0
	pos2 = 0
	for k in range(len(mat)):
		menor = 2222222222222222
		for n in range(len(mat[i])):
			if mat[k][n] % 2 == 0:
				if mat[k][n] <= menor:
					menor = mat[k][n]
					pos1 = k
					pos2 = n
		print(f"El numero menor de la fila {pos1} se encuentra en la columna {pos2}")
except ValueError:
	print ('Valor invalido')