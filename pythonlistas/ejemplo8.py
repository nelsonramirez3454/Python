"""elabore un progroma que almacene en una lista de 10 numeros enteros,
imprima el promedio de los numeros, la cantidad de numeros mayores al promedio y una lista con los numeros mayores
al promedio"""
try:
	lista = []
	lista2 = []
	var = 10
	suma = 0
	cantidad = 0

	for i in range(var):
		num = int(input("digite un numero: "))
		suma += num
		lista.append(num)
	promedio = suma // var

	print(f"el promedio es: {promedio}")

	for j in range(len(lista)):
		suma += lista[j]
		promedio = suma / var
		if num < promedio:
			lista2.append(num)
			contador += 1
	print(f"la lista de los numeros enteros es:{lista}")
	print(f"el promedio es:{promedio} ")
	print(f"la lista con los numeros mayores es:{contador} ")
except ValueError:
	print("digite un numero entero ")

