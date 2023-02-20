"""
    Programa11
    Nombre:Amayrani DB
    Fecha: 13/02/23
    Descripcion:Programa que utiliza clase Alumno e imprime el nombre y matricula y carrera
"""
class Alumno:
    __nombre = None  # denota falta de valor __nombre
    __matricula = None  # denota falta de valor __matricula
    __carrera = None  # denota falta de valor __carrera

    def __init__(self):  # definicion creada porcualquier usuario
          print("Alumno")  #Imprimira Alumno

    def setNombre(self, nombre):  # definicion creada porcualquier usuario
        self.__nombre = nombre

    def getNombre(self):  # definicion creada porcualquier usuario
        return self.__nombre  #  final de la función y continúa la ejecución del programa tras la llamada a la función
    
    def setMatricula(self, matricula):  # definicion creada porcualquier usuario
	    self.__matricula = matricula

    def getMatricula(self):  # definicion creada porcualquier usuario
	    return self.__matricula  #  final de la función y continúa la ejecución del programa tras la llamada a la función

    def setCarrera(self, carrera):  # definicion creada porcualquier usuario
	    self.__carrera = carrera

    def getCarrera(self):  # definicion creada porcualquier usuario
	    return self.__carrera  #  final de la función y continúa la ejecución del programa tras la llamada a la función

amayrani = Alumno()
amayrani.setNombre("Amayrani")
amayrani.setMatricula("1722110485")
amayrani.setCarrera("Tecnologias de la informacion")
print(amayrani.getNombre())