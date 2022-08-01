'''Leer dos matrices 5x5 entera y determinar si el promedio de los mayores elementos que
pertenecen a la serie de Fibonacci de cada fila de una matriz es igual al promedio de los
mayores elementos que pertenecen a la serie de Fibonacci de cada fila de la otra matriz.'''
try:
	matriz1 = []
	matriz2 = []
	suma = 0
	for i in range(5):
		fila = []
		mayor = 0
		for j in range(5):
			num = int(input('Digite un numero: '))
			a = 1
			b = 0
			c = 0
			while c <= num:
				if c== num and num == mayor:
					mayor = num
				c = a + b
				a = b
				b = c
			fila.append(num)
		suma += mayor
		matriz1.append(fila)
	promedio1 = suma / 5

	for i in range(5):
		fila = []
		mayor = 0
		for j in range(5):
			num = int(input('Digite un numero: '))
			a = 1
			b = 0
			c = 0
			while c <= num:
				if c== num and num == mayor:
					mayor = num
				c = a + b
				a = b
				b = c
			fila.append(num)
		suma += mayor
		matriz2.append(fila)
	promedio2 = suma / 5

	print('matriz 1 ',matriz1)
	print('matriz 2 ',matriz2)

	if promedio1 == promedio2:
		print('el promedio de la primera matriz es igual al de la segunda')
	else:
		print('el promedio de la primera matriz no es igual al de la segunda')

except ValueError:
	print('ERROR')