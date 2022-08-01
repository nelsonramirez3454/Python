'''Leer un número y calcularle el factorial a todos los enteros comprendidos entre 1 y el
número leído.'''
try:
	num = int(input("Digite un numero: "))
	factorial = 1
	for i in range(1,num+1):
		
		for j in range(1,i+1):
			print (f"i: {i} j: {j}")
			factorial *= i
			print (f"{i}!= {factorial}")

except ValueError:
	print ("ERROR")