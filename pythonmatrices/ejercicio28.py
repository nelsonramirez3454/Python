'''Leer una matriz 4x6 entera y determinar en qué posiciones se encuentran los números
cuyo penúltimo dígito sea el 5.'''
m = []
try:
	pos1 = 0
	posicion = []
	for i in range(4):
		fila = []
		for j in range (6):
			num = int(input('Ingrese un numero: '))
			fila.append(num)
			res = num % 100
			if res // 10 == 5:
				pos1 = (i,j)
				posicion.append(pos1)
		m.append(fila)
	print(m)
	print(f"Las pociones de los numeros con penultimo digito igual a 5 son: {posicion}")
except ValueError:
	print ('Valor invalido')