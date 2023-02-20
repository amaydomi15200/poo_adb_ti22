"""
    Programa11
    Nombre:Amayrani DB
    Fecha: 13/02/23
    Descripcion:Programa que utiliza clase Alumno e imprime el nombre y matricula y carrera
"""
class Alumno:
    __nombre = None
    __matricula = None
    __carrera = None

    def __init__(self):
          print("Alumno")

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getNombre(self):
    return self.__nombre
    
    def setMatricula(self, matricula):
	self.__matricula = matricula

    def getMatricula(self):
	return self.__matricula

    def setCarrera(self, carrera):
	self.__carrera = carrera

    def getCarrera(self):
	return self.__carrera

amayrani = Alumno()
amayrani.setNombre("Amayrani")
amayrani.setMatricula("1722110485")
amayrani.setCarrera("Tecnologias de la informacion")
print(amayrani.getNombre())