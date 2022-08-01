"""Leer una matriz 5x3 entera y determinar en qué fila está el mayor número primo."""
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
		for l in range(len(matriz[k])):
			if (((2 ** (matriz[k][l] -1))% matriz[k][l]) == 1 or matriz[k][l] == 2) and matriz[k][l] > mayor :
				mayor = matriz[k][l]
				pos1 = [k]	
	print(f"el numero primo mayor es {mayor} esta en la fila {pos1} ")
	print(matriz)
	

except ValueError:
	print("digite un numero valido:")