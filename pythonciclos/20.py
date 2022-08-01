'''Leer un número entero y determinar cuántos dígitos tiene.'''
try:
	num=int(input("Digite un numero: "))
	contador = 1
	control = 10
	while control < num:
		contador += 1
		control = control * 10

		
		
	print (f"El numero tiene {contador} digitos")
except ValueError:
	print ("ERROR")
