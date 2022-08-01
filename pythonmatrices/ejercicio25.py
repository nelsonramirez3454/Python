'''Leer dos matrices 4x5 enteras y determinar si el mayor número primo de una de las
matrices es también el mayor número primo de la otra matriz.'''
ma = []
mat = []
try:
	mayor1 = 0
	mayor2 = 0
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
			if (((2**(num1-1))%num1)== 1 or num1 == 2):
				if num1 > mayor2:
					mayor2 = num1
		mat.append(fila)

	print(f"matriz 1: {ma}")
	print(f"matriz 2: {mat}")
	if mayor1 == mayor2:
		print("Los numeros primos mayores de las matrices son iguales")
	else:
		print("Los numeros primos no son iguales")
except ValueError:
	print ('Valor invalido')