'''Leer dos matrices 4x6 enteras y determinar cuál es el mayor dato almacenado en ella que
pertenezca a la Serie de Fibonacci.'''
mar = []
fib = []
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
		fib.append(fila)
	print(fib)
	print(mar)
	for i in range(len(mar)):
		for j in range(len(mar[i])):
			for k in range(len(fib)):
				for n in range(len(fib[k])):		
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
						if fib[k][n] == b or fib[k][n] == 0:
							if fib[k][n] > mayor2:
								mayor2 = fib[k][n]
	print(f"El numero mayor de la matriz 1 que pertenece a la serie fibinacci es: {mayor1}")
	print(f"El numero mayor de la matriz 2 que pertenece a la serie fibinacci es: {mayor2}")	
except ValueError:
	print ('Valor invalido')