'''Leer un número entero y mostrar todos sus componentes numéricos o sea aquellos para
quienes él sea un múltiplo.'''
try:
	num=int(input("Digite un numero: "))

	if num < 0:
		num *= -1

	for i in range(1,num+1):
		if num % i == 0:
			print (f"los multiplos son: {i}")
			
except ValueError:
	print ("ERROR")
