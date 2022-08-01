"""Leer dos matrices 4x5 entera, luego leer un entero y determinar si cada uno de los
elementos de una de las matrices es igual a cada uno de los elementos de la otra matriz
multiplicado por el entero leído."""
try:
	matriz1 = []
	matriz2 = []
	matriz3 = []
	mult = 0
	for j in range(2):
		filas1 = []
		for k in range(2):
			numero1 = int(input("digite un numero: "))
			filas1.append(numero1)
		matriz1.append(filas1)

	for l in range(2):
		filas2 = []
		for m in range(2):
			numero2 = int(input("digite un numero: "))
			filas2.append(numero2)
		matriz2.append(filas2)

	numero = int(input("hola, ingerse un ultimo numero: "))
	for o in range(len(matriz1)):
		for p in range(len(matriz1[o])):
			while numero != 0:
				mult = matriz1[o] * numero
				mult = matriz1[p] * numero
				break
	
	for f in range(2):
		filas3 = []
		for g in range(2):
			filas3.append(mult)
		matriz3.append(filas3)

	print(matriz3)
except ValueError:
	print("digite un valor numerico")