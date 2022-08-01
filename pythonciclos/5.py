'''Leer dos números y mostrar todos los números terminados en 4 comprendidos entre ellos.'''
try:
	num1 = int(input("Digite un numero: "))
	num2 = int(input("Digite un numero: "))

	while num1 < num2:
		if num1 == 4 or num1 % 10 == 4:
			print(num1)
		num1 += 1
	while num2 <= num1:
		if num2 == 4 or num2 % 10 == 4:
			print(num2)
		num2 += 1

 

except ValueError:
	print ("Digite un valor valido")