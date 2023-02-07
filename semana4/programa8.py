"""
    Programa8
    Nombre:Amayrani DB
    Fecha: 07/02/23
    Descripcion:Programa 11 versiones de un encontrar el mayor de 2 numeros
"""
n1 = int(input("Dame tu n1: "))
n2 = int(input("Dame tu n2: "))

print("Primer version")
if n1 > n2:
    print(n1)
if n2 > n1:
    print(n2)
if n1 == n2:
    print(None)

mayor=(n1,n2)

print("Segunda version")
if n2 > n1:
    print(n2)
if n1 > n2:
    print(n1)
if n2 == n1:
    print(None)

print("Tercera version")
if n1 > n2:
    print(n1)
elif n2 > n1:
    print(n2)
else:
    print(None)

print("Cuarta version")
