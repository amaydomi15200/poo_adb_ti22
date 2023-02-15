"""
    Programa14
    Nombre:Amayrani DB
    Fecha: 15/02/23
    Descripcion:Clase persona 
"""
class Persona: #Class Persona
    __nombre = None # Variable privada __nombre
    __edad = None # Variable privada __edad
    def __init__(self) -> None: # Constructor de la clase Persona
        print("Persona") #Imprime el texto "Persona"

    def setNombre(self,nombre:str)->None: # Funcion para modificar el valor de la variable privada __nombre
        self.__nombre = nombre #Modifica el valor de la variable privada __nombre yle asigna valor del parametro

    def getNombre(self)->str: #Funion que regresa el valor de la variable privada __nombre
        return self.__nombre # Regresa el valor de la variable privada __nombre