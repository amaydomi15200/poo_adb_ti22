"""
    Programa15
    Nombre:Amayrani DB
    Fecha: 15/02/23
    Descripcion:Clase alumno 
"""
from persona import Persona #Importa la calse Persona del archivo persona.py

class Alumno(Persona): #Crea la claase Alumno que hereda la clase Persona
    def __init__(self) -> None: #Constructor de la clase Alumno
        super().__init__() #Llama al constructor de la clase
        print("Alumno") #Imprime el texto Alumno

objeto_alumno = Alumno() #Crea un objeto de la clase Alumno

