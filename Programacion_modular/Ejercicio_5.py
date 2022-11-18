lista = ["Di", "buen", "día", "a", "papa"]
lista_invertida = []
def reverse (lista):
    for i in range (len(lista), 0,-1):
        lista_invertida.append(lista[i-1])
    return lista_invertida
print(reverse(lista))