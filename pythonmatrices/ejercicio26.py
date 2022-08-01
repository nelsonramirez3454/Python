'''Leer dos matrices 4x5 enteras y determinar si la cantidad de números pares almacenados
en una matriz es igual a la cantidad de números pares almacenados en la otra matriz.'''
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
			if num % 2 == 0:
				cont1 += 1
		ma.append(fila)
	print("Matriz 2")
	for k in range(4):
		fila = []
		for n in range (5):
			num1 = int(input('Ingrese un numero: '))
			fila.append(num1)
			if num1 % 2 == 0:
				cont2 += 1
		mat.append(fila)

	print(f"matriz 1 {ma}")
	print(f"matriz 2 {mat}")
	if cont1 == cont2:
		print("Las matrices 1 y 2 tienen la misma cantidad de numeros pares")
	else:
		print("Las matrices 1 y 2 no tienen la misma cantidad de numeros pares")

except ValueError:
	print ('Valor invalido')