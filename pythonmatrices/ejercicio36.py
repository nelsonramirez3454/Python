'''Leer dos matrices 4x6 enteras y determinar si el mayor número almacenado en una de
ellas que pertenezca a la Serie de Fibonacci es igual al mayor número almacenado en la otra
matriz que pertenezca a la Serie de Fibonacci.'''
mar = []
bon = []
try:
	mayor2 = 0
	mayor1 = 0
	print("Matriz 1")
	for i in range(4):
		fila = []
		for j in range (6):
			num = int(input('Ingrese un numero: '))
			fila.append(num)
		mar.append(fila)
	print("Matriz 2")
	for k in range(4):
		fila = []
		for n in range (6):
			num1 = int(input('Ingrese un numero: '))
			fila.append(num1)
		bon.append(fila)
	print(f"segunda matriz: {bon}")
	print(mar)
	for i in range(len(mar)):
		for j in range(len(mar[i])):
			for k in range(len(bon)):
				for n in range(len(bon[k])):		
					a = 0
					b = 1
					c = 0
					while b <= 218922995834555000000:
						c = a + b
						a = b
						b = c
						if mar[i][j] == b or mar[i][j] == 0:
							if mar[i][j] > mayor1:
								mayor1 = mar[i][j]
						if bon[k][n] == b or bon[k][n] == 0:
							if bon[k][n] > mayor2:
								mayor2 = bon[k][n]
	if mayor1 == mayor2:
		print(f"Los numeros mayores que pertenecen a la serie fibinacci son iguales: matriz 1 {mayor1} y matriz 2 {mayor2}")
	else:
		print(f"Los numeros mayores que pertenecen a la serie fibinacci no son iguales: matriz 1 {mayor1} y matriz 2 {mayor2}")	
except ValueError:
	print ('Valor invalido')