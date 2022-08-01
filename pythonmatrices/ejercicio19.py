"""Leer dos matrices 4x5 entera y determinar si sus contenidos son exactamente iguales."""
try:
	matriz1 = []
	matriz2 = []
	for j in range(2):
		filas1 = []
		for k in range(2):
			numero1 = int(input("digite un numero: "))
			filas1.append(numero1)
		matriz1.append(filas1)

	for l in range(2):
		filas2 = []
		for m in range(2):
			numero2 = int(input("digite un numero: "))
			filas2.append(numero2)
		matriz2.append(filas2)

	if matriz1== matriz2:
		print("ambas matrices tienen el contenido igual")
	else:
		print("NO tienen igual contenido")
	print(matriz1)
	print(matriz2)
				
	
except ValueError:
	print("digite un valor numerico")