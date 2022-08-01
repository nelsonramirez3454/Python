'''Leer dos matrices 4x5 enteras y determinar si el número mayor de una de las matrices es
igual al número mayor de la otra matriz.'''
ma = []
triz = []
try:
	mayor1 = 0
	mayor2 = 0
	for i in range(4):
		fila = []
		for j in range (5):
			num = int(input('Ingrese un numero: '))
			fila.append(num)
			if num > mayor1:
				mayor1 = num
		ma.append(fila)
	for i in range(4):
		fila = []
		for j in range (5):
			num1 = int(input('Ingrese un numero: '))
			fila.append(num1)
			if num1 > mayor2:
				mayor2 = num1
		triz.append(fila)
	if mayor1 == mayor2:
		print(f"El numero mayor ({mayor1}) de la matriz 1 es igual al numero mayor ({mayor2}) de la matriz 2")
	else:
		print(f"El numero mayor ({mayor1}) de la matriz 1 no es igual al numero mayor ({mayor2}) de la matriz 2")
except ValueError:
	print ('Valor invalido')