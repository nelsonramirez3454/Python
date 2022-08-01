'''Leer un número entero y determinar a cuánto es igual la suma de sus dígitos pares.'''
try:
	num=int(input("Digite un numero: "))
#sumar sus digitos
	if num < 0:
		print ("El numero no tiene digitos pares porque es negativo")
	else:
		suma = 0

		while num != 0:
			residuo = num % 10
			if residuo % 2 == 0:
				suma += residuo
			num //= 10
		print (suma)
except ValueError:
	print ("ERROR")
