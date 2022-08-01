class Cuenta:
	TIPO_CUENTA = ("Ahorro", "Corriente")
	def __init__(self, titular, id_titular, numero_cuenta, saldo, fecha, tipo_cuenta, cupo):
		self.__titular = titular
		self.__id_titular = id_titular
		self.__numero_cuenta = numero_cuenta
		self.__saldo = saldo
		self.__fecha = fecha
		self.__tipo_cuenta = self.validar_tipo_cuenta(tipo_cuenta)
		self.__cupo = cupo

		