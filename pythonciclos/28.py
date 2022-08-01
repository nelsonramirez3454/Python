'''Leer 2 números enteros y determinar cuál de los dos tiene mayor cantidad de dígitos
primos.'''
try:
	num1=int(input("Digite un numero: "))
	num2=int(input("Digite un numero: "))

	if num1 < 0:
		num1 *= -1
	if num2 < 0:
		num2 *= -1

	cont1 = 0
	cont2 = 0
	j = 1
	k = 1

	while num1 != 0:
		residuo1 = num1 % 10
		if residuo1 == 2 or residuo1 == 3 or residuo1 == 5 or residuo1 == 7:
			cont1 += 1
		num1 //= 10

	while num2 != 0:
		residuo2 = num2 % 10
		if residuo2 == 2 or residuo2 == 3 or residuo2 == 5 or residuo2 == 7:
			cont2 += 1
		num2 //= 10


	if cont1 > cont2:
		print ("El numero con mayor digitos primos es el primero")
	elif cont1 < cont2:
		print ("El numero con mayor digitos primos es el segundo")
	else:
		print ("Los dos numeros tienen la misma cantidad de digitos primos")


except ValueError:
	print ("ERROR")