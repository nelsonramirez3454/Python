'''Promediar los x primeros múltiplos de 2 y determinar si ese promedio es mayor que los y
primeros múltiplos de 5 para valores de x y y leídos.'''
try:
	multiplos2=int(input("Digite un numero de múltiplos de 2: "))
	multiplos5=int(input("Digite un numero de multiplos de 5: "))
	suma_multiplos2 = 0
	suma_multiplos5 = 0
	multiplo2 = 0
	multiplo5 = 0
# multiplos de dos
	for i in range(1,multiplos2+1):
		multiplo2 += 2
		suma_multiplos2 += multiplo2
	promedio2 = suma_multiplos2 / multiplos2
	print  (promedio2)
#multiplos de 5
	for i in range(1,multiplos5+1):
		multiplo5 += 5
		suma_multiplos5 += multiplo5
	promedio5 = suma_multiplos5 / multiplos5
	print  (promedio5)

	if promedio2 < promedio5:
		print ("El mayor es promedio de los multiplos de 5")
	elif promedio2 > promedio5:
		print ("El mayor es promedio de los multiplos de 2")
	else:
		print ("son iguales")
except ValueError:
	print ("Digite un valor valido")
