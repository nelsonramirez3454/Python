""" Leer 10 números enteros, almacenarlos en una lista y determinar cuántos números de los
almacenados en dicha lista comienzan con 3.  """
try:
	lista = []
	var = 10
	contador = 0

	for i in range(var):
		num = int(input("digite un numero: "))
		lista.append(num)
		j = 1
		while j < num:
			if num // j == 3:
				contador += 1
			j *= 10
	print(f"hay {contador} que empiezan por el digito 3 ")

	

except ValueError:
	print("digite un numero entero ")