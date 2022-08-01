'''Leer dos matrices 4x6 enteras y determinar si el mayor número primo de una matriz está
repetido en la otra matriz.'''
mat = []
matr = []
try:
	mayor = 0
	for i in range(4):
		fila = []
		for j in range (6):
			num = int(input('Ingrese un numero: '))
			fila.append(num)
			cont = 0
			for i in range(1,num):
				if num % i  == 0:
					cont += 1

			if cont == 2:
				if num > mayor:
					mayor = num
		mat.append(fila)
	cont2 = 0
	for k in range(4):
		fila = []
		for n in range (6):
			num1 = int(input('Ingrese un numero: '))
			fila.append(num1)
			if mayor == num1:
				cont2+=1
		matr.append(fila)
	print("Matriz 2: ",matr)
	print("Matriz 1: ",mat)

	if cont2 != 0:
		print("El numero primo mayor de la matriz 1 esta repetido en la matriz 2")
	else:
		print("El numero primo mayor de la matriz 1 no esta repetido en la matriz 2")
except ValueError:
	print ('Valor invalido')