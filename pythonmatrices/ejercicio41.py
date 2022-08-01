'''Leer dos matrices 5x5 enteras y determinar si el promedio entero de todos los elementos
que no están en la diagonal de una matriz es igual al promedio entero de todos los
elementos que no están en la diagonal de la otra matriz.'''
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
	sumaof = mar[4][1] + mar[4][2] + mar[4][3]
	suma = mar[2][0] + mar[2][1] + mar[2][3]+ mar[2][4] + mar[3][0] + mar[3][1] + mar[3][2] + mar[3][4] + mar[4][0]	
	prom1 = (mar[0][1] + mar[0][2] + mar[0][3] + mar[0][4] + mar[1][0]+ mar[1][2] + mar[1][3] + mar[1][4] + suma + sumaof) / 20
	print("Matriz 2")
	for k in range(5):
		fila = []
		for n in range (5):
			num1 = int(input('Ingrese un numero: '))
			fila.append(num1)
		fib.append(fila)
	sumaos = fib[4][0] + fib[4][1] + fib[4][2] + fib[4][3]
	suma2 = fib[2][0] + fib[2][1] + fib[2][3]+ fib[2][4] + fib[3][0] + fib[3][1] + fib[3][2] + fib[3][4]
	prom2 = (fib[0][1] + fib[0][2] + fib[0][3] + fib[0][4] + fib[1][0]+ fib[1][2] + fib[1][3] + fib[1][4] + suma2 + sumaos) / 20
	if prom1 == prom2:
		print("Los promedios son iguales")
		print(f"Promedio matriz 1: {prom1}")
		print(f"Promedio matriz 2: {prom2}")
	else:
		print("Los promedios no son iguales")
except ValueError:
	print ('Valor invalido')