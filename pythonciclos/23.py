'''Leer un número entero y determinar si la suma de sus dígitos es también un número
primo.'''
try:
	num=int(input("Digite un numero: "))
#sumar sus digitos
	if num < 0:
		num *= -1

	suma = 0

	while num !=0:
		residuo = num % 10
		suma += residuo
		num //=10

#saber si es primo
	if suma < 2:
		print ("la suma de sus digitos no da como resultado un numero primo")
	else:
		i = 1
		cont = 0
		while i <= suma:
			if suma % i == 0:
				cont += 1
			i += 1
		if cont > 2:
			print ("la suma de sus digitos no da como resultado un numero primo")
		else:
			print ("la suma de sus digitos da como resultado un numero primo")
except ValueError:
	print ("ERROR")
