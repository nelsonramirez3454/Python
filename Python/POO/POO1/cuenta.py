class Cuenta:

    def __init__(self, nombre, id_name):
        self.__nombre=nombre
        self.__id_name=id_name
        self.__saldo=0

    def set_depositar(self, deposito):
        self.__saldo+= deposito


    def get_consultar(self):
        return self.__saldo


    def set_retirar(self, retirar):
        self.__saldo-=retirar

    def get_id_name(self):
        return self.__id_name

    def visualizar(self):
        print("Nombre:",self.__nombre)
        print("Cedula:",self.__id_name)
        print("Saldo:",self.__saldo)

    