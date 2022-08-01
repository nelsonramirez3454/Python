class Cine:
    def __init__(self, codigo, nombre, pelicula):
        self.codigo = codigo
        self.nombre = nombre
        self.pelicula = pelicula
        

    def mostrar_sala(self):
        print("codigo: %s"%(self.codigo))
        print("nombre: %s"%(self.nombre))
        print("pelicula: %s"%(self.pelicula))
        