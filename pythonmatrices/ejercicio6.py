'''6. Leer una matriz 4x4 entera y calcular el promedio de los numeros mayores de cada fila.'''
try:
	matriz = []
	mayor = 0
	for i in range(4):
		fila = []
		for j in range(4):
			num = int(input("ingrese un numero: "))
			fila.append(num)
		matriz.append(fila)
	for k in range(len(matriz)):
		suma = 0
		for l in range(len(matriz[k])):
			if mayor < matriz[k][l]:
				mayor = matriz[k][l]
		suma += mayor
	total = suma / 4
	print(f"el promedio de los numeros mayores de cada fila es: {total} ")
	print(matriz)
except ValueError:
	print("digite un numero valido:")






