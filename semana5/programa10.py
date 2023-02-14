"""
    Programa10
    Nombre:Amayrani DB
    Fecha: 13/02/23
    Descripcion:Programa que utiliza clase persona e imprime el nombre y matricula
"""
class Persona:
	__nombre = None
	__email = None
	def __init__(self):
		print("Persona")

	def setNombre (self,nombre):
	    self.__nombre = nombre

	def getNombre (self):
	    return self.__nombre

	def setEmail (self,email):
	    self._email = email

	def getEmail (self):
	    return self.__email

dejah = Persona()
dejah.setNombre("Dejah")
dejah.setEmail("amaydomibadi@gmail.com")
print(dejah.getNombre())
print(dejah.getEmail())