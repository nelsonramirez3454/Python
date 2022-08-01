'''
Escribir en pantalla el resultado de sumar los primeros 20 múltiplos de 3.
'''
try:
    suma = 0
    for i in range(1,60+1):
    	if i % 3 == 0:
    		suma += i
    print(suma)
except ValueError:
    print ('ERROR')