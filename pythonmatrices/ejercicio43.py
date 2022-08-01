'''Leer dos matrices 5x5 enteras y determinar si el promedio entero de los números pares
de una matriz es igual al promedio de los números pares de la otra matriz.'''
Mat1 = []
Mat2 = []
try:
	cont = 0
	suma = 0
	valor = False
	print("Matriz 1")
	for i in range(5):
		fila = []
		for j in range(5):
			num = int(input("Ingrese un numero: "))
			if num % 2 == 0:
				cont+=1
				suma+=num
			fila.append(num)
		Mat1.append(fila)
	if cont != 0:
		promedio = suma // cont
	else:
		promedio = suma // 1

	print("Matriz 2")
	for a in range(5):
		fila1 = []
		for b in range(5):
			num1 = int(input("Ingrese un numero: "))
			if num1 == promedio:
				valor = True
			fila1.append(num1)
		Mat2.append(fila1)


	print("Matriz 1: ",Mat1)
	print("Matriz 2: ",Mat2)
	print("El promedio es: ",promedio)
	if valor == True:
		print("El promedio de los numeros pares se encuentra en la otra matriz")
	else:
		print("El promedio no se encuentra en la matriz")
except ValueError:
	print("Valor invalido")