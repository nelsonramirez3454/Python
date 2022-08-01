""" Leer 10 números enteros, almacenarlos 
en una lista y determinar cuántos dígitos primos hay en los números leídos. """
try:
	lista = []
	var = 10
	contador = 0
	for i in range(var):
		num = int(input("digite un numero: "))
		lista.append(num)
		while num != 0:
			dig = num % 10
			if (((2**(dig-1))% dig)== 1 or dig == 2):
				contador += 1
			num //= 10
	print(f"hay en total {contador} digitos primos ")	
except ValueError:
	print("digite un numero entero ")