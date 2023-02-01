"""
    Programa5
    Nombre:Amayrani DB
    Fecha: 30/01/23
    Descripcion:Area y perimetro de circulo y cuadrado
"""
#area circulo
print("Area del circulo")  #imprime en la pantalla texto para identificar area del circulo
PI = (3.1416)
radio = float(input("Dame el valor del radio: "))  #pide el radio del circulo
area_circulo= (PI) *(radio **2) #hace la operacion para sacar el area del circulo
print("El area del circulo con un radio de {} es {}: ",( area_circulo)) #imprime el area a la pantalla

#perimetro circulo
print("Perimetro del circulo")  #imprime en la pantalla texto para identificar perimetro del circulo
diametro = float(input("Dame el valor de tu diametro: "))  #pide el diametro del circulo
perimetro_circulo = (diametro*PI)  #hace la operacion para sacar el perimetro del circulo
print("El perimetro del circulo con un diametro de {} es {}: " ,perimetro_circulo)

#area del cuadrado
print("Area del cuadrado")  #imprime en la pantalla texto para identificar area del cuadrado
lado = float(input("Dame el valor de tu lado: "))  #pide el lado del cuadrado
area_cuadrado= (lado * lado) #hace la operacion para sacar el area del cuadrado
print("El area del cuadrado es de: ",area_cuadrado)  #imprime el area del cuadrado a la pantalla

#perimetro del cuadrado
print("Perimetro del cuadrado")#imprime en la pantalla texto para identificar el perimetro del cuadrado
perimetro_cuadrado = (lado * 4)  #hace la operacion para sacar el perimetro del cuadrado
print("El perimetro del cuadrado es de: ",perimetro_cuadrado)  #imprime el perimetrro del cuadrado
