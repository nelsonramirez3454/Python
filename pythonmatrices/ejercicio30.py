'''Leer una matriz 4x6 entera y determinar cuántas veces está en ella el número menor.'''
mat = []
try:
	menor = 9999999999999999
	for i in range(4):
		fila = []
		for j in range (6):
			num = int(input('Ingrese un numero: '))
			fila.append(num)
			if num < menor:
				menor = num
		mat.append(fila)
	cont = 0
	for i in range(len(mat)):
		for j in range(len(mat[i])):
			if mat[i][j] == menor:
				cont += 1
	print(mat)
	if cont != 0:
		print(f"El numero menor se repite {cont} veces")
	else:
		print("El numero menor no se repite")
except ValueError:
	print ('Valor invalido')