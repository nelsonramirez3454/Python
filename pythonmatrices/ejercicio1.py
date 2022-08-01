
'''Leer  una matriz 4x4 entera y determinar en qué fila y en qué columna se encuentra el número mayor.'''
try:
	mayor = 0
	matriz = []
	for x in range(4):
		fila = []
		for j in range(4):
			num = int(input("digite un numero:"))
			fila.append(num)
		matriz.append(fila)
	for x in range(len(matriz)):
		for j in range(len(matriz)):
			if matriz[x][j]> mayor:
				mayor = matriz [x][j]
				pos1 = x
				pos2 = j
	print(matriz)
	print(f"el numero mayor es: {mayor} esta es la fila {pos1} en la coluna {pos2} ")

except ValueError:
	print("digite un numero valido:")