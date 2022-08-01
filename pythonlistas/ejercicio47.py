"""Leer 10 números enteros, almacenarlos en una lista y determinar en qué posiciones
 se
encuentran los números múltiplos de 10. No utilizar el número 10 en ninguna operación. """
try:
	lista = []
	var = 10
	poss = []

	for i in range(var):
		num = int(input("digite un numero: "))
		lista.append(num)
		j = 1
	for j in range(len(lista)):
		variable = 11 - 1
		if lista[j] % variable == 0:
			poss.append(j)

	print(lista)
	print(poss)

	

except ValueError:
	print("digite un numero entero ")
