'''Leer un entero y mostrar todos los múltiplos de 5 comprendidos entre 1 y el número
leído.'''
try:
	num = int(input("Digite un numero entero: "))
	for i in range(1,num+1):
		if i % 5 == 0:
			print(i)
			i += 1
except ValueError:
	print ("Digite un valor valido")