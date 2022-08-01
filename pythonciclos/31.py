'''Leer números hasta que digiten 0 y determinar a cuánto es igual el promedio de los
números terminados en 5.'''
try:
	num = 1
	suma = 0
	cont = 0

	while num != 0:
		num=int(input("Digite un numero: "))

		if num < 0:
			num *= -1
		residuo = num % 10
		if residuo == 5:
			suma += num
			cont += 1
	promedio = suma / cont
	print(promedio)
except ValueError:
	print ("ERROR")
