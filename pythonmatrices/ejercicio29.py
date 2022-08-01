'''Leer una matriz 4x6 entera y determinar si alguno de sus números está repetido al menos
3 veces.'''
matriz = []
try:
	v = False
	cont = 0
	for i in range(4):
		fila = []
		for j in range (6):
			num = int(input('Ingrese un numero: '))
			fila.append(num)
		matriz.append(fila)
	print(matriz)
	for i in range(4):
		for j in range(6):
			num1 = matriz[i][j]
			for k in range(4):
				for n in range(6):
					if num1 == matriz[k][n]:
						cont += 1
					if cont >= 3:
						v = True
	if v:
		print(f"Hay numeros repetidos {cont} veces")
	else:
		print("no hay numeros repetidos")
except ValueError:
	print ('Valor invalido')