"""
    Programa5
    Nombre:Amayrani DB
    Fecha: 30/01/23
    Descripcion:Area y perimetro de triangulo
"""
#area
print("Area del triangulo")  #imprime en la pantalla texto para identificar area
altura = int(input("Dame la altura de tu triangulo: "))  #pide la altura del triangulo
base = int(input("Dame la base de tu triangulo: "))  #pide la base del triangulo
area= (base * altura) / 2 #hace la operacion para sacar el area 
print(area)  #imprime el area a la pantalla

#perimetro
print("Perimetro del triangulo")#imprime en la pantalla texto para identificar perimetro
lado1 = int(input("Dame el valor del lado 1: "))  #pide el valor del primer lado
lado2 = int(input("Dame el valor del lado 2: "))  #pide el valor del segundo lado
lado3 = int(input("Dame el valor del lado 3: "))  #pide el valor del tercer lado
perimetro = (lado1 + lado2 + lado3)  #hace la operacion para resolver el perimetro del triangulo
print(perimetro)  #imprime el valor del perimetro 