"""
    Programa9
    Nombre:Amayrani DB
    Fecha: 08/02/23
    Descripcion:Programa que por medio de un def nos de el numero mayor de dos numeros
"""
def mayor(numero1,numero2):  #definimos el mayor de los numeros
    if numero1 > numero2:  #
        print(numero1)  #Imprime el numero mayor que es el numero1
    elif numero2 > numero1:
        print(numero2)  #imprime el umero mayor que es el numero2
    else: # combinar la ejecución de la condición y la iteración
        print(None)  #Imprime None

mayor(3,2)  #3
mayor(2,3)  #3
mayor(3,3)  #None

#version 2
def mayor(numero1:int,numero2:int)->int:  #  definición de función usa dapara crear objetos, las cuales son definidas por cada usuario
    mayor = None  #dice que mayor es igual a None
    if numero1 > numero2:  # ejecutar un bloque de código si, y solo si, se cumple una determinada condición
        mayor = numero1  #Dice que mayor es igual a numero1
    elif numero2 > numero1: # Enlaza condiciones
        mayor = numero2
    else:   # combinar la ejecución de la condición y la iteración
        mayor = None #dice que mayor es igual a None
    return mayor

print(mayor(3,2))  #Imprimira 3
print(mayor(2,3))  #Imprimira 3
print(mayor(3,3))  #Imprimira None
