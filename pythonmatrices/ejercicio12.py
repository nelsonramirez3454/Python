"""Leer una matriz 5x5 entera y determinar en qué fila está el mayor número terminado en
6."""
try:
	matriz = []
	pos1 = 0
	mayor = 0
	for x in range(5):
		fila = []
		for j in range(5):
			num = int(input("ingrese un numero: "))
			fila.append(num)
		matriz.append(fila)
	for k in range(len(matriz)):
		for l in range(len(matriz[k])):
			if matriz [k] [l] % 10 == 6 and matriz [k] [l] > mayor:
				mayor = matriz[k][l]
				pos1 = [k]
	print(f"el numero mayor terminado en 6 es {mayor} y esta en la fila {pos1}")
	print(matriz)
	

except ValueError:
	print("digite un numero valido:")