'''Leer un número entero y determinar a cuánto es igual el primero de sus dígitos.'''
try:
	num=int(input("Digite un numero: "))

	if num < 0:
		num *= -1

	while num != 0:
		residuo = num % 10
		num //= 10
	print (f"El primer digito es igual a: {residuo}")


except ValueError:
	print ("ERROR")
