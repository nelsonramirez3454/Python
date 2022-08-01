"""Leer una matriz 5x4 entera y determinar cuántos múltiplos de 5 hay almacenados en ella."""
try:
	matriz = []
	contador = 0
	for j in range(5):
		filas = []
		for k in range(4):
			numero = int(input("digite un numero: "))
			filas.append(numero)
		matriz.append(filas)
	for l in range(len(matriz)):
		for m in range(len(matriz[l])):
			if matriz[l][m] % 5 == 0:
				contador += 1
	print(matriz)
	print(f"hay {contador} numeros multiplos de 5")
except ValueError:
	print("digite un valor numerico")