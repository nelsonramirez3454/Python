'''Leer un número entero y mostrar todos los divisores exactos del número comprendidos
entre 1 y el número leído.'''
try:
	num = int(input("Digite un numero entero: "))
	if num >= 0:
		for i in range (1, num+1):
			if num % i == 0:
				print (i)
	else:
		print ("el numero no es un numero entero")

except ValueError:
	print ("Digite un valor valido")