"""
    Programa10
    Nombre:Amayrani DB
    Fecha: 13/02/23
    Descripcion:Programa que utiliza clase persona e imprime el nombre y correo
"""
class Persona:
	__nombre = None  # denota falta de valor
	__email = None  # denota falta de valor
	def __init__(self):  # definicion creada porcualquier usuario 
		print("Persona")

	def setNombre (self,nombre): # definicion creada porcualquier usuario 
	    self.__nombre = nombre

	def getNombre (self):  # definicion creada porcualquier usuario 
	    return self.__nombre  #  final de la función y continúa la ejecución del programa tras la llamada a la función

	def setEmail (self,email):  # definicion creada porcualquier usuario 
	    self._email = email

	def getEmail (self):  # definicion creada porcualquier usuario 
	    return self.__email  #  final de la función y continúa la ejecución del programa tras la llamada a la función

dejah = Persona()  
dejah.setNombre("Dejah")
dejah.setEmail("amaydomibadi@gmail.com")
print(dejah.getNombre())
print(dejah.getEmail())