'''Leer una matriz 4x6 entera y determinar en qué posiciones están los menores por fila.'''
m = []
try:

	for i in range(4):
		fila = []
		for j in range (6):
			num = int(input('Ingrese un numero: '))
			fila.append(num)
		m.append(fila)
	print(m)
	pos1 = 0
	pos2 = 0
	for k in range(len(m)):
		menor = m[i][j]
		for n in range(len(m[i])):
			if m[k][n] == 0:
				menor = m[k][n]
				pos1 = k
				pos2 = n
			else:
				if m[k][n] <= menor:
					menor = m[k][n]
					pos1 = k
					pos2 = n
		print(f"El numero menor de la fila {pos1} se encuentra en la columna {pos2}")
except ValueError:
	print ('Valor invalido')