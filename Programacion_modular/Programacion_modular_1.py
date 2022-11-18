lista=[15,4,5,6,45,6,32]
                     
def obtenerElementoMayor(lista):
    mayor=lista[0]
    for i in range(len(lista)):
        if lista[i]>mayor:
            mayor=lista[i]
    return mayor
print(obtenerElementoMayor(lista))

def obtenerElementoMenor(lista):
    menor=lista[0]
    for i in range(len(lista)):
        if lista[i]<menor:
            menor=lista[i]
    return menor
print(obtenerElementoMenor(lista))

def sumaElementos(lista):





