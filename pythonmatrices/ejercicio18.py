"""Leer una matriz 5x5 entera y determinar en qué posición exacta se encuentra el mayor
múltiplo de 8."""
try:
	matriz = []
	mayor = 0
	posMyor = 0
	for j in range(3):
		filas = []
		for k in range(3):
			numero = int(input("digite un numero: "))
			filas.append(numero)
		matriz.append(filas)
	for l in range(len(matriz)):
		for m in range(len(matriz[l])):
			if matriz[l][m] % 8 == 0:
				matriz[l][m] = matriz[l][m]
			if matriz[l][m] >  mayor:
				mayor = matriz[l][m]
			while mayor != 0:
		 		posMyor = [l]
		 		posMyor = [m]
		 		break
				
	print(matriz)
	print(f"el mayor multiplo de 8 es: {mayor} y esta en la posicion: {posMyor}")
except ValueError:
	print("digite un valor numerico")