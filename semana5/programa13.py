"""
    Programa13
    Nombre:Amayrani DB
    Fecha: 14/02/23
    Descripcion:Herencia
"""
class Persona:  #Class Persona

    __nombre=None  #Variable privada __nombre
    __edad=None  #Variable privada __edad

    def __init__(self):  #constructor de la clase Persona
      print("Persona")  #Imprime el texto persona

    def getNombre(self): #Funion que regresa el valor de la variable privada __nombre
      return self.__nombre  # Regresa el valor de la variable privada __nombre

    def setNombre(self,nombre):  # Funcion para modificar el valor de la variable privada __nombre
      self.__nombre = nombre  #Modifica el valor de la variable privada __nombre yle asigna valor del parametro

    def getEdad(self):  #Funion que regresa el valor de la variable privada __edad
      return self.__edad   # Regresa el valor de la variable privada __edad

    def setEdad(self,edad): # Funcion para modificar el valor de la variable privada __edad
      self.__edad = edad  #Modifica el valor de la variable privada __edad yle asigna valor del parametro


class Alumno(Persona): #Class Alumno y herencia de Persona

    __nombre=None  #Variable privada __nombre
    __matricula=None  #Variable privada __matricula

    def __init__(self):  #Constructor de la clase Alumno
      print("Alumno")  #Imprime el texto alumno

    def getNombre(self): #Funion que regresa el valor de la variable privada __nombre
      return self.__nombre   # Regresa el valor de la variable privada __nombre

    def setNombre(self,nombre):  # Funcion para modificar el valor de la variable privada __nombre
      self.__nombre = nombre  #Modifica el valor de la variable privada __nombre yle asigna valor del parametro

    def getMatricula(self): #Funion que regresa el valor de la variable privada __matricula
      return self.__matricula  # Regresa el valor de la variable privada __matricula

    def setMatricula(self,matricula): # Funcion para modificar el valor de la variable privada __matricula
      self.__maricula = matricula  #Modifica el valor de la variable privada __matricula yle asigna valor del parametro

objeto_persona = Persona()
#print(objeto_persona.nombre)
objeto_persona.nombre ="Hola"
print(objeto_persona.nombre)  #imprime texto en pantalla
objeto_persona.setNombre("Dejah")
print(objeto_persona.getNombre())  #Imprime objeto persona

print(dir(objeto_persona))

#assert dir(objeto_persona)==op

