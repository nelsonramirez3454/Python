'''Leer dos números entero y mostrar todos los múltiplos de 5 comprendidos entre el
menor y el mayor.'''
try:
	num1=int(input("Digite un numero: "))
	num2=int(input("Digite otro numero: "))
	if num1 == num2:
		print ("el inicio y el limite son iguales")
	else:
		while num1 < num2:
			num1 += 1
			if num1 % 5 == 0:
				print(num1)
		while num2 < num1:
			num2 += 1
			if num2 % 5 == 0:
				print(num2)
except ValueError:
	print ("ERROR")
