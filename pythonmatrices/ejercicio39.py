'''Leer dos matrices 4x6 enteras y determinar si el promedio de las “esquinas” de una
matriz es igual al promedio de las “esquinas” de la otra matriz.'''
mar = []
fib = []
try:
	print("Matriz 1")
	for i in range(4):
		fila = []
		for j in range (6):
			num = int(input('Ingrese un numero: '))
			fila.append(num)
		mar.append(fila)
	prom1 = (mar[0][0] + mar[0][5] + mar[3][0] + mar[3][5]) / 4 
	print("Matriz 2")
	for k in range(4):
		fila = []
		for n in range (6):
			num1 = int(input('Ingrese un numero: '))
			fila.append(num1)
		fib.append(fila)
	prom2 = (fib[0][0] + fib[0][5] + fib[3][0] + fib[3][5]) / 4

	if prom1 == prom2:
		print("Los promedios son iguales")
		print(f"Promedio matriz 1: {prom1}")
		print(f"Promedio matriz 2: {prom2}")
	else:
		print("Los promedios no son iguales")
except ValueError:
	print ('Valor invalido')