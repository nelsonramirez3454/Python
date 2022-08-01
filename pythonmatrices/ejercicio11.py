"""Leer una matriz 5x3 entera y determinar en qué columna está el menor número par."""
try:
	matriz = []
	menor = 999999999999999999999999999999999999999999999999999999999999999
	pos2 = 0
	for x in range(4):
		fila = []
		for j in range(3):
			num = int(input("ingrese un numero: "))
			fila.append(num)
		matriz.append(fila)
	for k in range(len(matriz)):
		for l in range(len(matriz[k])):
			if matriz[k][l] % 2 == 0 and matriz[k][l] < menor :
				menor = matriz[k][l]
				pos2 = [l]	
	print(f"el numero par menor es {menor} esta en la columna {pos2} ")
	print(matriz)
	

except ValueError:
	print("digite un numero valido:")