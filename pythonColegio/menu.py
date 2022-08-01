
from os import system
from estudiante import Estudiante
from colegio import Colegio
from laboratorio import Laboratorio
from fecha import Fecha
from asistencia import AsistenciaLaboratorio
from archivocolegio import ArchivoColegio
class Menu:
	def __init__(self, nombre_colegio, archivo_colegio_nombre):
		self.colegio = Colegio(nombre_colegio)
		self.archivo_colegio = ArchivoColegio(archivo_colegio_nombre)


	def crear_estudiante(self):
		system("cls")
		print("***crear estudiante***")
		nombre_estudiante = input("Digite el nombre del estudiante: ")
		apellido_estudiante = input("Digite el apellido del estudiante: ")
		codigo_estudiante = input("Digite el codigo del estudiante: ")
		estudiante = Estudiante(nombre_estudiante,apellido_estudiante, codigo_estudiante)

		self.colegio.adicionar_estudiante(estudiante)
		print("el estudiante fue adicionado correctamente")
		input()

	def crear_laboratorio(self):
		system("cls")
		print("Crear laboratorio")
		nombre_laboratorio = input("Digite el nombre del laboratorio: ")
		codigo_laboratorio = input("Digite el codigo  del laboratorio: ")
		capacidad_laboratorio = input("Digite la capacidad del laboratorio: ")

		laboratorio = Laboratorio(nombre_laboratorio, codigo_laboratorio, capacidad_laboratorio)

		self.colegio.adicionar_laboratorio(laboratorio)
		print("el laboratorio fue adicionado correctamente")
		input()

	def crear_asistencia_laboratorio(self):
		system("cls")
		print("***crear asistencia laboratorio***")
		codigo_laboratorio = input("digite el codigo del laboratorio: ")
		pos_laboratorio = self.colegio.buscar_laboratorio(codigo_laboratorio)

		if pos_laboratorio != -1:
			try:
				dia = int(input("Digite el dia: "))
				mes = int(input("Digite el mes: "))
				anio = int(input("Digite el anio: "))
				fecha = Fecha(anio,mes,dia)

				codigo_asistencia = int(input("digite el codigo de asistencia: "))
				asistencia_laboratorio = AsistenciaLaboratorio(fecha, self.colegio.get_laboratorio(pos_laboratorio), codigo_asistencia)

				while True:
					print("****asistencia estudiante****")
					print("1 = ingrese asistencia estudiante: ")
					print("2 = salir")

					op = int(input("digite la opcion: "))
					

					if op == 1:
						codigo_estudiante = input("digite el codigo del estudiante: ")
						pos_estudiante = self.colegio.buscar_estudiante(codigo_estudiante)


						if pos_estudiante != -1:
							asistencia_laboratorio.adicionar_estudiante(self.colegio.get_estudiante(pos_estudiante))

						else:
							print(" el estudiante no existe")
					elif op ==2:
						break
					else:
						print("opcion invalida")
				self.colegio.adicionar_asistencia(asistencia_laboratorio)
			except ValueError:
				print(" el valor ingresado debe ser un numero entero: ")
				input()
		else:
			print("el laboratorio no existe!")
			input()

	def listar_estudiantes(self):
		system("cls")
		print("****listar estudiantes****")

		for estudiante in self.colegio.get_estudiantes():
			print("Codigo: %s" %(estudiante.get_codigo()))
			print("Nombre: %s" %(estudiante.get_nombre()))
			print("Apellido: %s" %(estudiante.get_apellido()))
			print("**************************")
		input()


	def listar_laboratorios(self):
		system("cls")
		print("******Listar laboratorios******")

		for laboratorio in self.colegio.get_laboratorios():
			print("Nombre: %s" %(laboratorio.nombre))
			print("Codigo: %s" %(laboratorio.codigo))
			print("Capacidad: %s" %(laboratorio.capacidad))
			print("*********************************")
		input()

	def listar_asistencias(self):
		system("cls")

		print("****listar asistencias****")

		for asistencia in self.colegio.get_asistencias():
			asistencia.visualizar_asistencia()
			print("************************")
		input()


	def listar_asistencia_laboratorio(self):
		system("cls")
		print("*****Listar asistencia laboratorio*****")

		codigo_laboratorio = input("Digite el codigo del laboratorio: ")
		pos = self.colegio.buscar_laboratorio(codigo_laboratorio)

		if pos != -1:
			for asistencia in self.colegio.get_asistencia_laboratorio(codigo_laboratorio):
				asistencia.visualizar_asistencia()
				print("************************")
			input()

	def listar_asistencia_laboratorio_estudiante(self):
		system("cls")
		print("****Listar asistencia al laboratorio del estudiante")

		codigo_estudiante = input("Digite el codigo del estudiante: ")
		pos = self.colegio.buscar_estudiante(codigo_estudiante)

		if pos != -1:
			for asistencia in self.colegio.get_asistencia_laboratorio_estudiante(codigo_estudiante):
				asistencia.visualizar_asistencia()
				print("**************************")
			input()
		else:
			print("El estudiante NO existe")
			input()

	def mostrar_menu(self):
		while True:
			system("cls")
			print("***NUESTRA SENORA DEL ROSARIO***")
			print("1 = Crear estudiante")
			print("2 = Crear laboratorio")
			print("3 = Crear asistencia laboratorio")
			print("4 = Listar estudiantes")
			print("5 = Listar laboratorios")
			print("6 = Listar asistencias")
			print("7 = Listar asistencia por laboratorios")
			print("8 = Listar asistencia asistencia a los laboratorios del estudiante")
			print("9 = Salir")

			print("******************")

			try:
				opcion = int(input("Digite la opcion: "))
				self.archivo_colegio.guardar(self.colegio)

				if opcion == 1:
					self.crear_estudiante()

				if opcion == 2:
					self.crear_laboratorio()
				elif opcion == 3:
					self.crear_asistencia_laboratorio()
				elif opcion == 4:
					self.listar_estudiantes()

				elif opcion == 5:
					self.listar_laboratorios()

				elif opcion == 6:
					self.listar_asistencias()

				elif opcion == 7:
					self.listar_asistencia_laboratorio()

				elif opcion == 8:
					self.listar_asistencia_laboratorio_estudiante()

				elif opcion == 9:
					break

				else:
					print("Opcion invalida")
			except ValueError:
				print("El valor iungresado debe ser entero")
				input()
if __name__ == '__main__':
	menu = Menu("NSR", "colegio.data")
	data = menu.archivo_colegio.cargar()

	if data is not None:
		menu.colegio = menu.archivo_colegio.cargar()
	menu.mostrar_menu()