'''realize un programa que perimta visualizar la tabla del 5
donde el resultado sea multiplo de 3'''
try:
	num = int(input("Digite el limite de la tabla"))

	for i in range(1, num):
		resultado = 5 * i

		if resultado % 3 ==0:
			print (resultado)

except ValueError:
	print ("Digite un valor valido")