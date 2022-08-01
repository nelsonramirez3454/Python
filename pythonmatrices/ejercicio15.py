"""Leer una matriz 5x4 entera y determinar cuántos números almacenados en ella terminan
en 34."""
try:
	matriz = []
	contador = 0
	for x in range(5):
		fila = []
		for j in range(4):
			num = int(input("ingrese un numero: "))
			fila.append(num)
		matriz.append(fila)
	for k in range(len(matriz)):
		for l in range(len(matriz[k])):
			if matriz [k] [l] % 100 == 34:
				contador += 1
				
	print(f"hay {contador} numeros terminados en 34")
	print(matriz)
	

except ValueError:
	print("digite un numero valido:")