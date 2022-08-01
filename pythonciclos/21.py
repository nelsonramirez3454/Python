'''Leer un número entero y determinar a cuánto es igual la suma de sus dígitos.'''
try:
	num=int(input("Digite un numero: "))

	suma = 0

	if num < 0:
		num *= -1
		while num != 0:
			residuo = num % 10
			suma += residuo
			num //= 10
		print (f"La suma de sus digitos es igual a -{suma}")
	else:
		while num != 0:
			residuo = num % 10
			suma += residuo
			num //= 10
		print (f"La suma de sus digitos es igual a {suma}")


except ValueError:
	print ("ERROR")
