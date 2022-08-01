"""Leer dos matrices 4x5 enteras y determinar cuántos datos tienen en común."""
try:
	print("Matriz 1")
	for i in range(4):
		fila = []
		for j in range (5):
			num = int(input('Ingrese un numero: '))
			fila.append(num)
		m.append(fila)
	print("Matriz 2")
	for k in range(4):
		fila = []
		for n in range(5):
			num1 = int(input("Ingrese un numero: "))
			fila.append(num1)
		mat.append(fila)
	cont = 0
	for i in range(len(m)):
		for j in range(len(m[i])):
			for k in range(len(mat)):
				for n in range(len(mat[k])):
					if m[i][j] == mat[k][n]:
						cont += 1
	print(m)
	print(mat)
	print(f"La cantidad de datos en comun de las matrices son: {cont}")
except ValueError:
	print ('Valor invalido')