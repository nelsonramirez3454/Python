"""Leer una matriz 3x4 entera y determinar en qué posiciones exactas se encuentran los
números pares."""
try:
	matriz = []
	for x in range(3):
		fila = []
		for j in range(4):
			num = int(input("ingrese un numero: "))
			fila.append(num)
		matriz.append(fila)
	for k in range(len(matriz)):
		pares = 0
		for l in range(len(matriz)):
			if matriz[k] [l] % 2 == 0:
				pares = matriz [k] [l]
				pos1 = [k]
				pos2 = [l]
				print(f"el numero par es {pares} esta en la fila {pos1} y columna {pos2}")
	print(matriz)
except ValueError:
	print("digite un numero valido:")