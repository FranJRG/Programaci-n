def suma(n1,n2):
    return n1+n2
print(suma(4,5))

def potencia(base, exp):
    return base**exp

print(potencia(4,3))

def multiplicar(n_1, n_2):
    return n_1*n_2

def operar(p1, p2):
    return potencia(p1, p2), suma(p1, p2), multiplicar(p1, p2)

print(operar(3,2))

from math import factorial

print(factorial(5))

def calcularRaizCuadrada(numero):
    return numero**(1/2)

print(calcularRaizCuadrada(64))

def obtenerElementoMayor(lista):
    mayor=lista[0]
    for i in range(len(lista)):
        if lista[i]>mayor:
            mayor=lista[i]
    return mayor
print(obtenerElementoMayor(lista))
'''
len(lista) =numero de elementos de una lista
lista.append(lista1[i]) = Cuando recorra el elemento lo almacene en otra lista
'''
