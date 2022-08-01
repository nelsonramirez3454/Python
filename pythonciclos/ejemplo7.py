'''realize un programa que muestre en orden inverso los numeros pares comprendidos entre o y 200'''

try:

	for i in range(200, 0, -2):
		resultado = 5 * i

		if resultado % 3 ==0:
			print (resultado)

except ValueError:
	print ("Digite un valor valido") 