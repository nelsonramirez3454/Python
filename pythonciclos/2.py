'''Leer un número entero y mostrar todos los pares comprendidos entre 1 y el número leído.'''
try:
	num = int(input("Digite un numero entero: "))
	if num >= 0:
		for i in range(2,num+1,2):
			print (i)
	else:
		print ("El numero no es un numero entero")
except ValueError:
	print ("Digite un valor valido")