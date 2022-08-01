'''Leer dos matrices 4x5 enteras y determinar si el mayor número primo de una de las
matrices también se encuentra en la otra matriz.'''
ma = []
mat = []
try:
	mayor1 = 0
	mayor2 = 0
	con = 'false'
	con2 = 'false'
	print("Matriz 1")
	for i in range(4):
		fila = []
		for j in range (5):
			num = int(input('Ingrese un numero: '))
			fila.append(num)
			if (((2**(num-1))%num)== 1 or num == 2):
				if num > mayor1:
					mayor1 = num
		ma.append(fila)
	print("Matriz 2")
	for k in range(4):
		fila = []
		for n in range (5):
			num1 = int(input('Ingrese un numero: '))
			fila.append(num1)
			if (((2**(num1-1))% num1)== 1 or num1 == 2):
				if num1 > mayor2:
					mayor2 = num1
		mat.append(fila)

	print(f"Matriz 1 {ma}")
	print(f"Matriz 2 {mat}")

	for i in range(len(ma)):
		for j in range(len(ma[i])):
			if mayor2 == ma[i][j]:
				con = 'true'
	if con == 'true':
		print("El numero primo mayor de la matriz 2 se encuentra en la matriz 1")
	else:
		print("No se encuentra en la matriz 1")

	for k in range(len(mat)):
		for n in range(len(mat[k])):
			if mayor1 == mat[k][n]:
				con2 = 'true'
	if con2 == 'true':
		print("El numero primo mayor de la matriz 1 se encuentra en la matriz 2")
	else:
		print("El numero primo mayor de la matriz 1 no se encuentra en la matriz 2")
except ValueError:
	print ('Valor invalido')