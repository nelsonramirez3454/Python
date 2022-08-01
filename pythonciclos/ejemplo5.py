'''realize un programa que perimta realizar la sumatoria de numeros enteros desde cero hasta 1000'''
try:
	num = 0

	while num <= 1000:
		print (f"{num}")
		num += 1

except ValueError:
	print ("Digite un valor valido")