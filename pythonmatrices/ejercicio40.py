'''Leer dos matrices 5x5 enteras y determinar si el promedio entero de los elementos de la
diagonal de una matriz es igual al promedio de los elementos de la diagonal de la otra matriz.'''

mar = []
fib = []
try:
	print("Matriz 1")
	for i in range(5):
		fila = []
		for j in range (5):
			num = int(input('Ingrese un numero: '))
			fila.append(num)
		mar.append(fila)
	prom1 = (mar[0][0] + mar[1][1] + mar[2][2] + mar[3][3] + mar[4][4]) / 5 
	print("Matriz 2")
	for k in range(5):
		fila = []
		for n in range (5):
			num1 = int(input('Ingrese un numero: '))
			fila.append(num1)
		fib.append(fila)
	prom2 = (fib[0][0] + fib[1][1] + fib[2][2] + fib[3][3] + fib[4][4]) / 5

	if prom1 == prom2:
		print("Los promedios son iguales")
		print(f"Promedio matriz 1: {prom1}")
		print(f"Promedio matriz 2: {prom2}")
	else:
		print("Los promedios no son iguales")
except ValueError:
	print ('Valor invalido')