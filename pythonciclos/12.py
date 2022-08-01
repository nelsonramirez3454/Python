'''Leer un número entero de 3 dígitos y determinar si tiene el dígito 1.'''
try:
	num = int(input("Digite un numero entero de tres digitos: "))
	if num >= 100 and num <= 999:
		n1 = num // 100
		n2 = num // 10 % 10
		n3 = num % 10
		cont = 0
		while n1 == 1:
			n1 += 1
			cont += 1
		while n2 == 1:
			n2 += 1
			cont += 1
		while n3 == 1:
			n3 += 1
			cont += 1
		if cont >= 1:
			print (f"el numero tiene {cont} digito(s) 1")
		else:
			print ("no tiene el digito 1")
	else:
		print ("el numero no es de tres digitos")
except ValueError:
	print ("Digite un valor valido")