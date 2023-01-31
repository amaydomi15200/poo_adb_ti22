"""
    Programa5
    Nombre:Amayrani DB
    Fecha: 30/01/23
    Descripcion:Area y perimetro de triangulo
"""
#area
print("Area del triangulo")
altura = int(input("Dame la altura de tu triangulo: "))
base = int(input("Dame la base de tu triangulo: "))
area= (base * altura) / 2
print(area)

#perimetro
print("Perimetro del triangulo")
lado1 = int(input("Dame el valor del lado 1: "))
lado2 = int(input("Dame el valor del lado 2: "))
lado3 = int(input("Dame el valor del lado 3: "))
perimetro = (lado1 + lado2 + lado3)
print(perimetro)