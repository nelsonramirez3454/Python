""""La escuela de computación desea llevar a cabo un registro de ingreso de sus alumnos
al laboratorio de programación haciendo uso de la fecha en la cual cada estudiante
ingresa al lugar. Se requiere crear la clase Fecha con las siguientes especificaciones:
 Variables: Día, mes, año.
 Constructores: Uno que se inicialice con un fecha fija y otro que reciba como
parámetros los valores para crear el objeto.
 Métodos: Modificar la fecha, mostrar fecha usando el formato:
Día/Mes/Año, y mostrar la fecha en pantalla poniendo el mes en palabras."""
from os import system
from alumno import Alumno
class Menu:
    def __init__(self):
        self.__alumnos=[]


    def crear_alumno(self):
        system("cls")
        print("Bienvedido para continar debes crear una cuenta!")
        print("****** Alumno *********")
        nombre=input("Nombre: ")
        dia=input("Ingrese el dia: ")
        mes=input("ingrese el mes: ")
        año=input("ingrese el año: ")
        cedula=int(input("Cedula: "))
        alumno=Alumno(nombre, dia, mes, año, cedula)


        if self.buscar_alumno(alumno.get_cedula())==-1:
            self.__alumnos.append(alumno)
            print("el alumno fue agregada.")
        else:
            print("No se pudo agregar el alumno.")
        input()
    def mes(self, mes):
    	if mes == 1:
    		print("Enero")


    def buscar_alumno(self,cedula):
        for j in range(len(self.__alumnos)):
            if self.__alumnos[j].get_cedula()==cedula:
                return j
        return -1

    def visualizar_datos(self):
        system("cls")
        print("****** Datos alumno ******")
        cedula=int(input("Para ver la fecha usando el mes en palabras debes ingresar tu cedula: "))
        if self.buscar_alumno(cedula)!=-1:
            while True: 
                try:
                    system("cls")
                    for j in range(len(self.__alumnos)):
                        if self.__alumnos[j].get_cedula()==cedula:
                            print("*********DATOS DEL ALUMNO**********")
                            self.__alumnos[j].visualizar()
                        input()
                except ValueError:
                    print("Error")
                    input()
        else:
            print("No se a encontrado el alumno.")
            input()





    def menu_inicio(self):
        while True:
            system("cls")
            print("*********DATOS*********")
            print("1) Crear Alumno")
            print("2) visualizar")
            print("3) Salir")
            try:
                op=int(input("Digite su respuesta: "))
                if op ==1:
                    self.crear_alumno()
                elif op == 2:
                	self.visualizar_datos()
          
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