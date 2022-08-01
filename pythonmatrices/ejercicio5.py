'''5. Leer una matriz 4x3 entera, calcular la suma de los elementos de cada fila y determinar
cual es la fila que tiene la mayor suma.'''
try:
	matriz = []
	mayor = 0
	pos1 = 0
	for x in range(4):
		fila = []
		for j in range(3):
			num = int(input("ingrese un numero: "))
			fila.append(num)
		matriz.append(fila)
	for k in range(len(matriz)):
		suma = 0
		for l in range(len(matriz[k])):
			suma += matriz [k] [l]
			if mayor < suma:
				mayor = suma
				pos1 = [k]
	print(f"la suma mayor es {mayor} y esta en la fila {pos1} ")
	print(matriz)
except ValueError:
	print("digite un numero valido:")