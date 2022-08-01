'''Leer dos matrices 4x6 enteras y determinar si el número mayor de una matriz se
encuentra en la misma posición exacta en la otra matriz.'''
mar = []
fib = []
try:
	mayor2 = 0
	mayor1 = 0
	pos1 = 0
	pos2 = 0
	pos3 = 0
	pos4 = 0
	print("Matriz 1")
	for i in range(4):
		fila = []
		for j in range (6):
			num = int(input('Ingrese un numero: '))
			fila.append(num)
			if num > mayor1:
				mayor1 = num
				pos1 = i
				pos2 = j
		mar.append(fila)
	print("Matriz 2")
	for k in range(4):
		fila = []
		for n in range (6):
			num1 = int(input('Ingrese un numero: '))
			fila.append(num1)
			if num1 > mayor2:
				mayor2 = num1
				pos3 = k
				pos4 = n
		fib.append(fila)
	print(f"matriz 1 {fib}")
	print(f"matriz 2 {mar}")
	if pos1 == pos3 and pos2 == pos4:
		print("El numero mayor de la matriz 1 se encuentra en la misma posicion del numero mayor de matriz 2")
		print(f"matriz 1 {pos1},{pos2} = matriz 2 {pos3},{pos4}")
	else:
		print("Los numeros mayores no estan en la misma posicion")
except ValueError:
	print ('Valor invalido')