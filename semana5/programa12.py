"""
    Programa12
    Nombre:Amayrani DB
    Fecha: 14/02/23
    Descripcion:Herencia
"""
class Persona:
    
    def __init__(self):
        __nombre = None
        print("Persona")

class Alumno(Persona):
    def __init__(self):
        super().__init__()
        print("Alumno")

objeto_persona = Persona()
objeto_alumno = Alumno()

objeto_persona.nombre = "Dejah"
print(objeto_persona.nombre)

objeto_alumno.nombre="John Carter"
print(objeto_alumno.nombre)

objeto_alumno.email="john@utectulancingo.edu.mx"
print(objeto_alumno.email)

#print(dir(objeto_persona))  # dir nos permite ver los atibutos de los objetos, 
