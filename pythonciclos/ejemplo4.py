'''implemente un programa que muestre todos los numeros potencia
de 2 entre 0 y 30, ambos inclusive'''
try:
	num = 0

	while num <= 30:
		resultado = 2 ** num
		print (f"{resultado}")
		num += 1
except ValueError:
	print ("Digite un valor valido")