""". Leer 10 números enteros, almacenarlos en una lista. Luego leer un entero y determinar si este último
 entero se encuentra entre los 10 valores almacenados en la lista. """
try:
	lista = []
	var = 10
	contador = 0

	for i in range(var):
		num = int(input("digite un numero: "))
		lista.append(num)
		
	numero = int(input("digite el numero a buscar: "))

	for j in range(len(lista)):
		if lista[j] == numero:
			contador += 1
	if contador > 0:
		print(f"el numero se encuentra en la lista {contador} veces" )
	else:
		print("el numero NO se encuentra en la lista")

except ValueError:
	print("digite un numero entero ")
