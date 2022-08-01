'''Leer una matriz 4x6 entera y determinar cuántos de los números almacenados en ella
pertenecen a los 100 primeros elementos de la serie de Fibonacci.'''
mar = []
try:
	cont = 0
	for i in range(4):
		fila = []
		for j in range (6):
			num = int(input('Ingrese un numero: '))
			fila.append(num)
		mar.append(fila)
	print(mar)

	for i in range(len(mar)):
		for j in range(len(mar[i])):		
			a = 0
			b = 1
			c = 0
			while b <= 218922995834555000000:
				c = a + b
				a = b
				b = c
				if mar[i][j] == b or mar[i][j] == 0:
					cont += 1
	print(f"La cantidad de numeros que epertenecen a la serie fibonacci son: {cont}")
except ValueError:
	print ('Valor invalido')