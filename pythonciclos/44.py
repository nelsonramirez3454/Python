'''Leer un número y calcularle su factorial.'''
try:
	num = int(input("Digite un numero para calcular su factorial: "))
	factorial = 1
	for i in range(2,num+1):
		factorial *= i

	print (f"{num}!= {factorial}")
except ValueError:
	print ("ERROR")