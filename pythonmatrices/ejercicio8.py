"""Leer una matriz 4x4 entera y determinar cuántos enteros terminados en 0 hay
almacenados en ella."""
try:
	matriz = []
	contador = 0

	for x in range(4):
		fila = []
		for j in range(4):
			num = int(input("ingrese un numero: "))
			fila.append(num)
		matriz.append(fila)
	for k in range(len(matriz)):
		for l in range(len(matriz[k])):
			if matriz [k] [l] % 10 == 0:
				contador += 1
	print(f"hay {contador} terminados en cero")
	print(matriz)
	

except ValueError:
	print("digite un numero valido:")