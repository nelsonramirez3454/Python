'''Mostrar en pantalla los primeros 20 múltiplos de 3.'''
try:
	for i in range(1,60+1):
		if i % 3 == 0:
			print (i)
except ValueError:
	print ("Digite un valor valido")
