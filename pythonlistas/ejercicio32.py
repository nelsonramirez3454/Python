""" Leer 10 númertos enteros, almacenarlos en una lista. Luego leer un entero y
 determinar
cuántos números de los almacenados en la lista terminan en el mismo dígito que 
el último
valor leído. """
try:
	lista = []
	var = 10

	for i in range(var):
		num = int(input("digite un numero: "))
		lista.append(num)
	print("la lista es: ",lista)

	numero = int(input("digite un numero: "))
	contador = 0
	j = 1
	for j in range(len(lista)):
			if num // j == numero:
				contador += 1
			j *= 10
			contador += 1
	print(f"hay {contador} numeros terminados en {numero}")


except ValueError:
	print("digite un numero entero ")