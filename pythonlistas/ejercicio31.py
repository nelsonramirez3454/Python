""". Leer 10 números enteros, almacenarlos en una lista. Luego leer un entero y determinar cuántos divisores
exactos tiene este último número entre los valores almacenados en la lista. """
try:
	lista = []
	var = 10

	for i in range(var):
		num = int(input("digite un numero: "))
		lista.append(num)
	print("la lista es: ",lista)

	numero = int(input("digite un numero: "))
	contador = 0

	for j in range(len(lista)):
		if lista[j] % numero  == 0:
			contador += 1
	print("los divisores exactos de los numeros ingresados son: ",contador)


except ValueError:
	print("digite un numero entero ")