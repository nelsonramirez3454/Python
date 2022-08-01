'''Leer un número entero y determinar cuántas veces tiene el dígito 1.'''
try:
	num=int(input("Digite un numero: "))

	if num < 0:
		num *= -1

	cont = 0
	while num != 0:
		residuo = num % 10
		if residuo == 1:
			cont += 1
		num //=10

		
	print (f"El numero tiene {cont} uno(s)")
except ValueError:
	print ("ERROR")
