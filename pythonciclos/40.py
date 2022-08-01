'''Leer un número de dos dígitos y determinar si pertenece a la serie de Fibonacci.'''
try:
	numero1 = int(input("Digite un numero de dos digitos: "))
	if numero1 < 100 and numero1 > 9:
		num = 0
		aux = 0
		suma = 1

		cont = 0 

		while suma < 100:
			aux = num 
			num = suma 
			suma = num + aux

			if suma == numero1:
				cont += 1
				print ("El numero pertenece a la serie de Fibonacci")
		if cont == 0:
			print ("El numero no pertenece a la serie de Fibonacci")
	else:
		print ("El numero no es de dos digitos")
except ValueError:
	print ("ERROR")