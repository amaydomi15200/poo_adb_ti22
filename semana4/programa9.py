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
    else:
        print(None)

mayor(3,2)
mayor(2,3)
mayor(3,3)

#version 2
def mayor(numero1:int,numero2:int)->int:
    mayor = None
    if numero1 > numero2:
        mayor = numero1
    elif numero2 > numero1:
        mayor = numero2
    else:
        mayor = None
    return mayor

print(mayor(3,2))
print(mayor(2,3))
print(mayor(3,3))
