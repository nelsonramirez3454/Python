"""Leer una matriz 3x4 entera y determinar cuántos de los números almacenados son primos
y terminan en 3."""
try:
	matriz = []
	contador = 0
	for x in range(3):
		fila = []
		for j in range(4):
			num = int(input("ingrese un numero: "))
			fila.append(num)
		matriz.append(fila)
	for k in range(len(matriz)):
		for l in range(len(matriz[k])):
			if (((2 ** (matriz[k][l] -1))% matriz[k][l]) == 1 or matriz[k][l] == 2) and matriz[k][l] % 10 == 3:
				contador += 1
				
	print(f"hay {contador} numeros primos terminados en 3")
	print(matriz)
	

except ValueError:
	print("digite un numero valido:")