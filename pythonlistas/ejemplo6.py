"""elabore un programa que permita almacenar en una lista los 100 primeros numeros pares, la lista debe iniciar
en 2"""
try:
	lista = []

	for i in range(2,200+1,2):
		lista.append(i)
	print(f"los 100 primeros numeros pares son {lista}")
	
except ValueError:
	print("digite un numero entero ")