'''Leer dos matrices 4x5 enteras y determinar si la cantidad de números primos
almacenados en una matriz es igual a la cantidad de números primos almacenados en la otra
matriz.'''
ma = []
mat = []
try:
	cont1 = 0
	cont2 = 0
	print("Matriz 1")
	for i in range(4):
		fila = []
		for j in range (5):
			num = int(input('Ingrese un numero: '))
			fila.append(num)
			if (((2**(num-1))%num)== 1 or num == 2):
				cont1 += 1
		ma.append(fila)
	print("Matriz 2")
	for k in range(4):
		fila = []
		for n in range (5):
			num1 = int(input('Ingrese un numero: '))
			fila.append(num1)
			if (((2**(num1-1))%num1)== 1 or num1 == 2):
				cont2 += 1
		mat.append(fila)

	print(f"Matriz 1: {ma}")
	print(f"Matriz 2: {mat}")

	if cont1 == cont2:
		print("tienen la misma cantidad de numeros primos")
	else:
		print("No tienen la misma cantidad de numeros primos")

except ValueError:
	print ('Valor invalido')