"""Leer una matriz 5x3 entera y determinar en qué columna está el mayor número que
comienza con el dígito 4."""
try:
	matriz = []
	pos1 = 0
	mayor = 0
	for x in range(5):
		fila = []
		for j in range(3):
			num = int(input("ingrese un numero: "))
			fila.append(num)
		matriz.append(fila)
	for k in range(len(matriz)):
		for l in range(len(matriz[k])):
			if matriz [k] [l] > mayor:
				mayor = matriz[k][l]
				mayor1 = mayor
				while mayor1 != 0:
					resultado = mayor1 % 10
					mayor1 //= 10
				if resultado == 4:
					pos1 = [l]
	print(f"el numero mayor que comienz en 4 es {mayor} y esta en la columna {pos1}")
	print(matriz)
	

except ValueError:
	print("digite un numero valido:")