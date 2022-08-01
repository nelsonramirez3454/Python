'''Leer dos matrices 4x5 enteras y determinar si el número mayor almacenado en la
primera está en la segunda.'''
matriz1 = []
matriz2 = []
try:
	mayor = 0
	con = 'false'

	for i in range(4):
		fila1 = []
		for j in range(5):
			num1 = int(input('Digite un numero: '))
			if num1 > mayor:
				mayor = num1
			fila1.append(num1)
		matriz1.append(fila1)

	for k in range(4):
		fila2 = []
		for l in range(5):
			num2 = int(input('Digite un numero: '))
			fila2.append(num2)
		matriz2.append(fila2)

	print(f'primera matriz: {matriz1}')
	print(f'segunda matriz: {matriz2}')

	for d in range(4):
		for s in range(5):
			if mayor == matriz2[d][s]:
				con = 'true'

	if con == 'true':
		print(f'el numero mayor ({mayor}) de la matriz 1 esta en la matriz 2')
	else:
		print(f'el numero mayor de la matriz 1 no esta en la matriz 2')
except ValueError:
	print ('Valor invalido')