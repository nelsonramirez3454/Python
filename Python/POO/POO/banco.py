import random
from os import system
from datetime import datetime
from cuenta import Cuenta



class Banco:
	def __init__(self):
		self.__cuentas = []
		self.__numeros_cuentas = []


	def generar_numero_cuenta(self):
		while True:
			numero = random.randint(1, 10)
			if numero not in self.__numeros_cuentas:
				self.__numeros_cuentas.append(numero)
				break
		return numero


	def pedir_datos_cuenta(self):
		try:
			system("cls")
			print("***************************")
			print("******  CREAR CUENTA ******")
			print("***************************")
			titular = input("Digite el nombre del titular: ")
			id_titular = input("Digite el numero de identificacion del titular: ")
			num_cuenta = self.generar_numero_cuenta()
			saldo = int(input("Digite el saldo: "))
			fecha_actual = datetime.now()

			while True:
				print("***************************")
				print("**    TIPOS DE CUENTAS   **")
				print("")
				print("1 = Ahorro")
				print("2 = Corriente")

				try:
					op_tipo_cuenta = int(input("Digite la opcion: "))

					if op_tipo_cuenta == 1:
						tipo_cuenta = "Ahorro!"
						cupo = 0
						break
					elif op_tipo_cuenta == 2:
						tipo_cuenta = "Corriente!"
						
						try:
							cupo = float(input("Digite el cupo asignado ala cuenta: "))
							break
						except ValueError:
							print("Digite un valor numerico")
							input()
					else:
						print("** Ups, opcion incorrecta, debe ser 1 o 2**")
						input()
				except ValueError:
					print("Digite un valor numerico!")
					input()
				cuenta = Cuenta(titular, id_titular, num_cuenta, saldo, fecha_actual, tipo_cuenta, cupo)
				self.adicionar_cuenta(cuenta)
				print("***************************")
				print("**La cuenta se creo Correctamente!  **")
				print("Su numero de cuenta es: %d"% num_cuenta)
				print("********       * * * *      *********")
				input()
		except ValueError:
			print("Digite un valor numerico!")
			input()
	def buscar_cuenta(self, num_cuenta):
		for i in range(len(self.__cuentas)):
			if numero_cuenta == self.__cuentas[i].get_numero_cuenta():
				return i
		return -1

	def adicionar_cuenta(self, cuenta):
		pos = self.buscar_cuenta(cuenta.get_numero_cuenta())
		if pos == -1:
			self.__cuentas.append(cuenta)
			return True
		return False

	def mostrar_menu_principal(self):
		while True:
			system("cls")
			print("***************************")
			print("***************************")
			print("********** BANCO **********")
			print("***************************")
			print("**     MENU PRINCIPAL    **")
			print("")
			print("1 = Crear Cuenta")
			print("2 = Salir")

			try:
				op = int(input("Digite una opcion: "))
				print("**************")

				if op == 1:
					self.pedir_datos_cuenta()

				elif op == 2:
					break

			except ValueError:
				print("Digite un valor numerico")
				input()

if __name__ == '__main__':
	banco = Banco()
	banco.mostrar_menu_principal()

