'''Leer dos matrices 5x5 enteras y determinar si el promedio entero de los números
terminados en 4 de una matriz se encuentra al menos 3 veces en la otra matriz.'''
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
			if (num % 100)%10 == 4:
				cont+=1
				suma+=num
			fila.append(num)
		Mat1.append(fila)
	if cont != 0:
		promedio = suma // cont
	else:
		promedio = suma // 1

	cont1 = 0
	print("Matriz 2")
	for a in range(5):
		fila1 = []
		for b in range(5):
			num1 = int(input("Ingrese un numero: "))
			if num1 == promedio:
				cont1 += 1
			fila1.append(num1)
		Mat2.append(fila1)


	print("Matriz 1: ",Mat1)
	print("Matriz 2: ",Mat2)
	print("El promedio es: ",promedio)
	if cont1 > 2:
		print("El promedio de los numeros terminados en 4 se encuentra en la otra matriz mas de tres veces")
	else:
		print("El promedio no se encuentra en la matriz mas de tres veces")
except ValueError:
	print("Valor invalido")