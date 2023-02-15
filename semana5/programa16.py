"""
    Programa16
    Nombre:Amayrani DB
    Fecha: 15/02/23
    Descripcion:Clase profesor 
"""
from persona import Persona #Importa la calse Persona del archivo persona.py

class Profesor(Persona): #Crea la claase Profesor que hereda la clase Persona
    def __init__(self) -> None: #Constructor de la clase Prodesor
        super().__init__() #Llama al constructor de la clase
        print("Profesor") #Imprime el texto Profesor

objeto_profesor = Profesor() #Crea un objeto de la clase Profesor