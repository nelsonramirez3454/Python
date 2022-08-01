"""Leer 10 números enteros, almacenarlos en una lista y determinar a cuánto es igual la
suma de los dígitos pares de cada uno de los números leídos. """
try:
	lista = []
	var = 10
	contador = 0
	for i in range(var):
		num = int(input("digite un numero: "))
		lista.append(num)
		suma = 0
		while num != 0:
			dig = num % 10
			if dig % 2 ==  0:
				suma += dig
			num //= 10
		print(f"la suma de los digitos pares es: {suma} ")


	


except ValueError:
	print("digite un numero entero ")