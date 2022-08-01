'''Leer dos números y mostrar todos los enteros comprendidos entre ellos.'''
try:
	num1 = int(input("Digite un numero entero: "))
	num2 = int(input("Digite un numero entero: "))

	while num1 < num2:
		print(num1)
		num1 += 1
	while num2 <= num1:
		print(num2)
		num2 += 1


except ValueError:
	print ("Digite un valor valido")