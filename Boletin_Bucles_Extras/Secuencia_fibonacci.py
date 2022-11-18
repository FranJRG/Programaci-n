valores=int(input("Cantidad de numeros a introducir: "))

contador = 0
valor_anterior = valores-1

while contador<valores:
    contador+=1
    valor_anterior = contador+valor_anterior
    print(contador)
    