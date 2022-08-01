'''Leer un número entero y mostrar en pantalla su tabla de multiplicar.'''
try:
	multiplicando = int(input("Digite un numero para mostrar su tabla: "))
	for i in range(1,10+1):
		producto = multiplicando * i
		print (f"{multiplicando} * {i} = {producto}")
except ValueError:
	print ("ERROR")