'''Leer un número entero y determinar a cuánto es igual el promedio entero de sus dígitos.'''
try:
	num=int(input("Digite un numero: "))

	suma = 0
	cont = 0

	if num < 0:
		num *= -1
		while num != 0:
			residuo = num % 10
			cont += 1
			suma += residuo
			num //= 10
		promedio = suma // cont
		print (f"El promedio de sus digitos es: -{promedio}")
	else:
		while num != 0:
			residuo = num % 10
			cont += 1
			suma += residuo
			num //= 10
		promedio = suma // cont
		print (f"El promedio de sus digitos es: {promedio}")


except ValueError:
	print ("ERROR")
