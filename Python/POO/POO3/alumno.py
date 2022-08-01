class Alumno:

    def __init__(self, nombre, dia, mes, año, cedula):
        self.__nombre=nombre
        self.__cedula=cedula
        self.__dia=dia
        self.__mes=mes
        self.__año=año

    def get_cedula(self):
        return self.__cedula


    def visualizar(self):
        print("Nombre:",self.__nombre)
        print("Cedula:",self.__cedula)
        print(self.__dia,"/",self.__mes,"/",self.__año)
        

    