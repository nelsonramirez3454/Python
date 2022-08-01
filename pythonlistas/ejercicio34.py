"""Leer 10 números enteros, almacenarlos en una lista y determinar cuántas veces en 
la lista
se encuentra el dígito 2. No se olvide que el dígito 2 puede estar varias veces
en un mismo
número. """
try:
	lista = []
	var = 10
	contador = 0

	for i in range(var):
		num = int(input("digite un numero: "))
		lista.append(num)
		while num != 0:
			dos = num % 10
			if dos == 2:
				contador += 1
			num //= 10
	print(f"el numero 2 esta {contador} veces en la lista")


	


except ValueError:
	print("digite un numero entero ")