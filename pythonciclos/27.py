'''Leer 2 números enteros y determinar cuál de los dos tiene mayor cantidad de dígitos.'''
try:
	num1=int(input("Digite un numero: "))
	num2=int(input("Digite un numero: "))


	if num1 < 0:
		num1 *= -1
	if num2 < 0:
		num2 *= -1

	cont1 = 0
	cont2 = 0

	while num1 != 0:
		residuo1 = num1 % 10
		cont1 += 1
		num1 //= 10
	while num2 != 0:
		residuo2 = num2 % 10
		cont2 += 1
		num2 //= 10
	if cont1 > cont2:
		print ("El numero con mayor digitos es el primero")
	elif cont1 < cont2:
		print ("El numero con mayor digitos es el segundo")
	else:
		print ("Los dos numeros tienen la misma cantidad de digitos")


except ValueError:
	print ("ERROR")
