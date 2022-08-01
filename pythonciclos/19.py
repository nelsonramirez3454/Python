'''Leer un número entero y determinar si es primo.'''
try:
	num1=int(input("Digite un numero: "))

	if num1 < 2:
		print ("El numero no es primo")
	else:
		i = 1
		cont = 0
		while i <= num1:
			if num1 % i == 0:
				cont += 1
			i += 1
		if cont > 2:
			print ("El numero no es primo")
		else:
			print ("el numero es primo")

except ValueError:
	print ("ERROR")
