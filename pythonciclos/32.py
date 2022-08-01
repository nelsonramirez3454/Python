'''Leer números hasta que digiten 0 y determinar a cuanto es igual el promedio entero de
los número primos leídos.'''
try:
	num = 1
	suma = 0
	cont_pri = 0

	while num != 0:
		num=int(input("Digite un numero: "))

		if num < 0:
			num *= -1

		if num < 2:
			cont_pri += 0
		else:
			i = 1
			cont = 0
			while i <= num:
				if num % i == 0:
					cont += 1
				i += 1
			if cont > 2:
				cont_pri += 0
			else:
				suma += num
				cont_pri += 1
	if cont_pri > 0:
		promedio = suma / cont_pri
		print (f"El promedio de los digitos primos es: {promedio}")

except ValueError:
	print ("ERROR")
