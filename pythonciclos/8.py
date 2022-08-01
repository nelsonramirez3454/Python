'''Mostrar en pantalla todos los pares comprendidos entre 20 y 200.'''
try:
	for i in range(20,200,2):
		print (i)

except ValueError:
	print ("Digite un valor valido")