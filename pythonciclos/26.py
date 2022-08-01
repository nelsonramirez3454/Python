'''Leer un número entero y determinar cuál es el mayor de sus dígitos.'''
try:
	num=int(input("Digite un numero: "))

	mayor = 0

	if num < 0:
		num *= -1

	while num != 0:
		residuo = num % 10
		if residuo > mayor:
			mayor = residuo
		num //= 10
	print (f"El mayor de los digitos es: {mayor}")


except ValueError:
	print ("ERROR")
