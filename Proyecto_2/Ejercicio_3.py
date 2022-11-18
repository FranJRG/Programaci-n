cantidad=int(input("Cuanto tienes"))
if cantidad>=300 or cantidad<0:
    total=False
else:
    total=True
print(total)

print("-----------")

edad=int(input("Cual es la edad"))
if 16<=edad<=22:
    edadAdolescente=False
else:
    edadAdolescente=True
print(edadAdolescente)

print("------------")

respuesta=str(input("Cual es la respuesta"))
if respuesta=="Si" or respuesta=="No":
    contestacion=False
else:
    contestacion=True
print(contestacion)

print("----------------")

numero=int(input("Cual es el numero"))
if numero%7==0 or numero%3==0:
    valor=False
else:
    valor=True
print(valor)
