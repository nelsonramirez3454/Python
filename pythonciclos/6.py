'''Leer un número entero de tres dígitos y mostrar todos los enteros comprendidos entre 1 y
cada uno de los dígitos.'''
try:
	num = int(input("Digite un numero entero de tres dígitos: "))
	if num < 1000 and num > 100:
		di1 = num // 100
		di2 = num // 10 % 10
		di3 = num % 10

		for i in range(1,di1+1):
			print(i)
			i += 1
			print()

		for j in range(1,di2+1):
			print(j)
			j += 1
			print()
			
		for k in range(1,di3+1):
			print(k)
			k += 1

	else:
		print ("El numero no es de tres dígitos")
except ValueError:
	print ("Digite un valor valido")