""" Leer 10 números enteros, almacenarlos en una lista y determinar cuántos números de los
almacenados en dicha lista terminan en 15. """
try:
	lista = []
	var = 10
	contador = 0

	for i in range(var):
		num = int(input("digite un numero: "))
		lista.append(num)
		if num % 100 == 15:
			contador += 1
	print(f"hay {contador} que terminan por el numero 15")

	

except ValueError:
	print("digite un numero entero ")