"""
    Programa8
    Nombre:Amayrani DB
    Fecha: 07/02/23
    Descripcion:Programa 11 versiones de un encontrar el mayor de 2 numeros
"""
n1 = int(input("Dame tu n1: "))  #pide el valor del numero uno
n2 = int(input("Dame tu n2: "))  #pide el valor del numero dos

print("Primer version")  #imprime el texto de primera version
if n1 > n2:   #hace la operacion si el numero 1 es mayor que el numero 2
    print(n1)  #imrimira el numero mayor que es 1
if n2 > n1:  #hace la operacion si el numero 2 es mayor que el numero 1
    print(n2)  #imprimira el numero mayor que es el 2
if n1 == n2:  #hace la operacion si el numero1 y numero2 son iguales
    print(None)  #Va a imprimir None

mayor=(n1,n2)

print("Segunda version")   #imprime el texto de segunda version
if n2 > n1:   #hace la operacion si el numero 2 es mayor que el numero 1
    print(n2)  #imprimira el numero mayor que es el 2
if n1 > n2:  #hace la operacion si el numero 1 es mayor que el numero 2
    print(n1)   #imrimira el numero mayor que es 1
if n2 == n1:  #hace la operacion si el numero2 y numero1 son iguales
    print(None)   #Va a imprimir None

print("Tercera version")  #imprime el texto de tercera version
if n1 > n2:  #hace la operacion si el numero 1 es mayor que el numero 2
    print(n1)  #imrimira el numero mayor que es 1
elif n2 > n1:  #hace la operacion si el numero 2 es mayor que el numero 1
    print(n2)  #imprimira el numero mayor que es el 2
else:
    print(None)  #Va a imprimir None

print("Cuarta version")   #imprime el texto de cuarta version
if n1 < n2 :  #hace la operacion si el numero 1 es menor que el numero 2
    print(n2)  #imprimira el numero mayor que es el 2
elif n2 < n1:
    print(n1)
else:
    print(None)

print("Quinta version")   #imprime el texto de quinta version
if n2 < n1:
    print(n1)
if n1 < n2:
    print(n2)
if n1 == n2:
    print(None)

print("Sexta version")   #imprime el texto de sexta version
if n1 >= n2:
    if n1 > n2:
        print(n1)
    else:
        print(None)
else:
    print(n2)

print("Septima version")   #imprime el texto de septima version
if n1 <= n2:
    if n1 < n2:
        print(n2)
    else:
        print(None)
else:
    print(n1)

print("Octava version")   #imprime el texto de octava version
if n1 <= n2:
    if n1 == n2:
        print(None)
    else:
        print(n2)
else:
    print(n1)

print("Novena version")   #imprime el texto de novena version
if n1 == n2:
    print(None)
elif n1 > n2:
    print(n1)
else:
    print(n2)

print("Decima version")   #imprime el texto de decima version
if n1 == n2:
    print(None)
elif n1 < n2:
    print(n2)
else:
    print(n1)
    
print("onceava version")
if n1 == n2:
    print(None)

elif n1 >= n2:
    print(n1)
else:
    print(n2)