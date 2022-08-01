'''4. Leer una matriz 4x3 entera y determinar en que posiciones exactas se encuentran los
numeros primos.'''
try:
	matriz = []
	for x in range(4):
		fila = []
		for j in range(3):
			num = int(input("ingrese un numero: "))
			fila.append(num)
		matriz.append(fila)
	for k in range(len(matriz)):
		primos = 0
		for l in range(len(matriz[k])):
			if (((2 ** (matriz[k][l] -1))% matriz[k][l]) == 1 or matriz[k][l] == 2):
				primos = matriz [k] [l]
				pos1 = [k]
				pos2 = [l]
				print(f"el numero primo es {primos} esta en la fila {pos1} y columna {pos2}")
	print(matriz)
	

except ValueError:
	print("digite un numero valido:")