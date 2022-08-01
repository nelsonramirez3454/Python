"""Leer una matriz 4x4 entera y determinar en qué posiciones están los enteros terminados
en 0."""
try:
	matriz = []
	digito = 0
	pos1 = 0
	pos2 = 0
	for x in range(4):
		fila = []
		for j in range(4):
			num = int(input("ingrese un numero: "))
			fila.append(num)
		matriz.append(fila)
	for k in range(len(matriz)):
		for l in range(len(matriz[k])):
			if matriz [k] [j] % 10 == 0:
				digito = matriz [k] [j]
				pos1 = [k]
				pos2 = [l]
	print(f"los numeros terminados en 0 son: {digito} esta en la fila {pos1} y columna {pos2}")
	print(matriz)
	

except ValueError:
	print("digite un numero valido:")