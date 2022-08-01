class Pelicula:

	def __init__(self, codigo, titulo, genero):
		self.codigo = codigo
		self.titulo = titulo
		self.genero = genero
		self.alquilada = None

	def mostrar_pelicula(self):
		print("Codigo: %s"%(self.codigo))
		print("Titulo: %s"%(self.titulo))
		print("Genero: %s"%(self.genero))
		if self.alquilada == None:
			print("Estado: Disponible")
		else:
			print("Estado: Alquilada")
