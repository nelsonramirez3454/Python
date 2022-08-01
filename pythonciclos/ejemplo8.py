'''leer un numero entero y mostrar todos los enteros comprendidos  entre 1 y el numero leido'''
try:
	num = int(input("Digite un numero: "))

	for i in range(1, num+1):
		print (i)

except ValueError:
	print ("Digite un valor valido")