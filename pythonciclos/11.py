'''Leer un número entero de dos dígitos y mostrar en pantalla todos los enteros
comprendidos entre un dígito y otro.'''
try:
	num = int(input("Digite un numero entero de dos digitos: "))
	if num < 100 and num > 9:
		di1 = num // 10
		di2 = num % 10
		for i in range(di1,di2+1):
			print(i)
			i += 1
	else:
		print("el numero no es de dos digitos")

except ValueError:
	print ("Digite un valor valido")