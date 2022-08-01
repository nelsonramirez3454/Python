'''implemente un programa que solicite al usuario un valor inicial un valor final y un incremento que permita
llegar al valor final'''
try:
	num = int(input("Digite el valor inicial: ")) 
	limite = int(input("Digite el valor final: ")) 
	incremento = int(input("Digite el incremento: ")) 

	while num <= limite:
		print (f"{num}")
		num += incremento
except ValueError:
	print ("Digite un valor valido")