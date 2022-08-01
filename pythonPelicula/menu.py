from os import system
from socio import Socio
from pelicula import Pelicula
from videoclub import Videoclub
from cine import Cine

class Menu:
	def __init__(self, videoclub):
		self.videoclub = videoclub

	"""socios"""
	def adicionar_socio(self):
		system("cls")
		print("** adicionar socio **")
		codigo = input("Digite el codigo del socio: ")
		nombre = input("Digite el nombre del socio: ")
		telefono = input("Digite el telefono del socio: ")
		domicilio = input("Digite el domicilio del socio: ")
		socio = Socio(codigo,nombre,telefono,domicilio)

		if self.videoclub.adicionar_socio(socio):
			print("El socio fue ingresado correctamente")
			input()
		else:
			print("El socio no se pudo ingresar")
			input()

	def listar_socio(self):
		system("cls")
		print("*** LISTAR SOCIOS ***")
		self.videoclub.listar_socio()
		input()

	def eliminar_socio(self):
		system("cls")
		print("*** ELIMINAR SOCIO ***")
		codigo = input("Digite el codigo del socio que desea eliminar: ")

		if self.videoclub.eliminar_socio(codigo):
			print("el socio fue eliminado correctamente")
			input()
		else:
			print("el socio no se pudo eliminar")
			input()


	"""Salas de cine"""
	def adicionar_sala(self):
		system("cls")
		print("Adicionar sala de cine")
		codigo = input("Digite el codigo de la sala: ")
		nombre = input("Digite el nombre de la sala: ")
		pelicula = input("Digite el nombre de la pelicula: ")
		cine = Cine(codigo, nombre, pelicula)

		if self.videoclub.adicionar_sala(cine):
			print("Sala ingresada correctamente!")
			input()
		
		else:
			print("La sala no se adiciono, intente de nuevo")
			input()

	def listar_sala(self):
		system("cls")
		print("***Salas creadas***")
		self.videoclub.listar_sala()
		input()


	"""peliculas"""
	def adicionar_pelicula(self):
		system("cls")
		print("** adicionar pelicula **")
		codigo = input("Digite el codigo de la pelicula: ")
		titulo = input("Digite el titulo de la pelicula: ")
		genero = input("Digite el genero de la pelicula: ")
		pelicula = Pelicula(codigo,titulo,genero)

		if self.videoclub.adicionar_pelicula(pelicula):
			print("La pelicula fue ingresada correctamente")
			input()
		else:
			print("La pelicula no se pudo ingresar")
			input()

	def listar_pelicula(self):
		system("cls")
		print("*** LISTAR PELICULAS ***")
		self.videoclub.listar_pelicula()
		input()

	def eliminar_pelicula(self):
		system("cls")
		print("*** ELIMINAR PELICULA ***")
		codigo = input("Digite el codigo de la pelicula que desea eliminar: ")

		if self.videoclub.eliminar_pelicula(codigo):
			print("La pelicula fue eliminado correctamente")
			input()
		else:
			print("La pelicula no se pudo eliminar")
			input()

	def alquilar_pelicula(self):
		system("cls")
		print("*** ALQUILAR PANTALLA ***")
		codigo_pelicula = input("Digite el codigo de la pelicula: ")
		codigo_socio = input("Digite el codigo del socio: ")

		if self.videoclub.alquilar_pelicula(codigo_pelicula,codigo_socio):
			print("la pelicula fue alquilada")
			input()
		else:
			print("La pelicula no se pudo alquilar")
			input()

	def devolver_pelicula(self):
		system("cls")
		print("*** DEVOLVER PELICULA ***")
		codigo_pelicula = input("Digite el codigo de la pelicula: ")
		codigo_socio = input("Digite eel codigo del socio: ")

		if self.videoclub.devolver_pelicula(codigo_pelicula,codigo_socio):
			print("Se devolvio la pelicula exitosamente")
			input()
		else:
			print("no se pudo devolver la pelicula")
			input()


	def mostrar_menu_principal(self):
		while True:
			system("cls")
			print("*************************************")
			print("***** VIDEOCLUB 2020 *****")
			print("1 = Crear socio")
			print("2 = Mostrar socios")
			print("3 = Eliminar socio")
			print("***")
			print("4 = Agregar pelicula")
			print("5 = Mostrar peliculas")
			print("6 = Eliminar pelicula")
			print("7 = Alquilar pelicula")
			print("8 = Devolver pelicula")
			print("11 = Adicionar Sala")
			print("12 = Listar Salas")
			print("9 = Salir")

			try:
				opcion = int(input("digite la opcion a ejecutar: "))
				if opcion == 1:
					self.adicionar_socio()
				elif opcion == 2:
					self.listar_socio()
				elif opcion == 3:
					self.eliminar_socio()
				if opcion == 4:
					self.adicionar_pelicula()
				elif opcion == 5:
					self.listar_pelicula()
				elif opcion == 6:
					self.eliminar_pelicula()
				elif opcion == 7:
					self.alquilar_pelicula()
				elif opcion == 8:
					self.devolver_pelicula()
				elif opcion == 11:
					self.adicionar_sala()
				elif opcion == 12:
					self.listar_sala()
				elif opcion == 0:
					break
				else:
					print("Opcion invalida")

			except ValueError:
				print("Digite un numero entero")
				

if __name__ == '__main__':
	videoclub = Videoclub("TGOADSI")
	menu = Menu(videoclub)
	menu.mostrar_menu_principal()