'''Defina la clase Cuenta Bancaria que permita las operaciones: Retirar, depositar, consultar saldo, entre otros. 
No olvide definir el constructor para crear objetos de dicha clase, además, recuerden que la cuenta siempre tiene un dueño."'''

from cuenta import Cuenta
from os import system

class Menu:
    def __init__(self):
        self.__cuentas=[]

    def buscar_cuenta(self,id_name):
        for j in range(len(self.__cuentas)):
            if self.__cuentas[j].get_id_name()==id_name:
                return j
        return -1

    def crear_cuenta(self):
        system("cls")
        print("Bienvedido para continar debes crear una cuenta!")
        print("****** CREAR CUENTA *********")
        nombre=input("Nombre: ")
        id_nombre=int(input("Cedula: "))
        cuenta=Cuenta(nombre,id_nombre)

        if self.buscar_cuenta(cuenta.get_id_name())==-1:
            self.__cuentas.append(cuenta)
            print("La cuenta fue agregada.")
        else:
            print("No se pudo agregar la cuenta.")
        input()


    def buscar_cuenta_op(self):
        system("cls")
        print("****** BUSCAR CUENTA PARA... ******")
        id_nombre=int(input("Digite la cedula de la cuenta: "))

        if self.buscar_cuenta(id_nombre)!=-1:
            while True:
                system("cls")
                print("********* DESEA HACER.. *********")
                print("1) Depositar")
                print("2) Retirar")
                print("3) Consultar")
                print("4) Salir")
                try:
                    op=int(input("Digite una opcion: "))
                    if op ==1:
                        system("cls")
                        for j in range(len(self.__cuentas)):
                            if self.__cuentas[j].get_id_name()==id_nombre:

                                print("*****DEPOSITAR*****")
                                deposito=int(input("Digite la cantidad a depositar: "))
                                self.__cuentas[j].set_depositar(deposito)
                        input()
                    elif op==2:
                        system("cls")
                        for j in range(len(self.__cuentas)):
                            if self.__cuentas[j].get_id_name()==id_nombre:
                                print("*******RETIRAR*******")
                                retiro=int(input("Digite la cantidad a depositar: "))
                                if self.__cuentas[j].get_consultar()>retiro:
                                    self.__cuentas[j].set_retirar(retiro)
                                else:
                                    print("El saldo de la cuenta no es menor al que decea retirar.")
                        input()
                    elif op==3:
                        system("cls")
                        for j in range(len(self.__cuentas)):
                            if self.__cuentas[j].get_id_name()==id_nombre:
                                print("*********DATOS DE LA CUENTA**********")
                                self.__cuentas[j].visualizar()
                        input()
                    elif op==4:
                        break
                    else:
                        print("Digite un valor valido")
                        input()
                except ValueError:
                    print("Error")
                    input()
        else:
            print("No se a encontrado la cuenta.")
            input()




    def menu_inicio(self):
        while True:
            system("cls")
            print("*********MENU*********")
            print("1) Crear cuenta")
            print("2) Buscar cuenta")
            print("3) Salir")
            try:
                op=int(input("Digite su respuesta: "))
                if op ==1:
                    self.crear_cuenta()
                elif op ==2:
                    self.buscar_cuenta_op()
                elif op == 3:
                    break
                else:
                    print("Digite un valor valido")
            except ValueError:
                print("Error")
                input()

if __name__ == "__main__":
    menu=Menu()
    menu.menu_inicio()