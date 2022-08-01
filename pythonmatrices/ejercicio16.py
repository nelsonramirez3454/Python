"""Leer una matriz 5x4 entera y determinar cuántos números almacenados en ella tienen
un solo dígito."""
try:
	matriz = []
	contador = 0
	for x in range(5):
		filas = []
		for j in range(4):
			numero = int(input("digite un numero: "))
			filas.append(numero)
		matriz.append(filas)
	for k in range(len(matriz)):
		for l in range(len(matriz[k])):
			if matriz[k][l] < 10:
				contador += 1
	print(matriz)
	print(f"hay {contador} numeros de un solo digito")
except ValueError:
	print("digite un valor numerico")