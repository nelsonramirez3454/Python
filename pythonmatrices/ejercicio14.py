"""14. Leer una matriz 5x5 entera y determinar cuántos números almacenados en ella tienen
mas de 3 dígitos."""
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
			if matriz [k] [l] > 99:
				contador += 1
				
	print(f"hay {contador} numeros mayores a 3 digitos")
	print(matriz)
	

except ValueError:
	print("digite un numero valido:")