'''Leer dos números enteros y determinar a cuánto es igual el producto mutuo del primer
dígito de cada uno.'''
try:
	num1 = int(input("Digite un numero 1: "))
	num2 = int(input("Digite un numero 2: "))
	
	while num1 != 0:
		residuo1 = num1 % 10
		num1 //= 10
		
	while num2 != 0:
		residuo2 = num2 % 10
		num2 //= 10

	producto = residuo1 * residuo2
	print (producto)
except ValueError:
	print ("ERROR")