"""Leer una matriz 4x4 entera y determinar cuántas veces se repita en ella el número mayor."""
try:
	mayor = 0
	matriz = []
	for x in range(4):
		fila = []
		for j in range(4):
			num = int(input("digite un numero:"))
			fila.append(num)
		matriz.append(fila)
	for k in range(len(matriz)):
		for l in range(len(matriz)):
			if matriz[k][l]> mayor:
				mayor = matriz [k][l]
				contador = 0
			if matriz[k][l] == mayor:
				contador += 1
	print(matriz)
	print(f"el numero mayor es: {mayor} y se repite {contador} veces")

except ValueError:
	print("digite un numero valido:")