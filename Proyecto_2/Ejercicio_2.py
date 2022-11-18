
precio=int(input("Cual es el precio "))
if precio >=60 and precio <=420:
    precio= True
else:
    precio=False
print(precio)

print("--------------")

numero=int(input("Cual es el numero "))
if numero%2 != 0:
    numero= True
else:
    numero=False
print(numero)

print("-------------")

saldo=int(input("Cual es el saldo "))
dineroSacar=int(input("Cuanto quieres sacar "))
if saldo >=dineroSacar and saldo>=0 and dineroSacar>=0:
    total=True
else:
    total=False
print(total)

print("---------------")

hora=int(input("Cual es la hora"))
minutos=int(input("Cuantos minutos"))
if 0<=hora<=23 and 0<=minutos<=59:
    tiempo=True
else:
    tiempo=False
print(tiempo)

print("---------------")

estadoCivil=str(input("Como te encuentras"))
if estadoCivil=="C" or estadoCivil=="S" or estadoCivil=="V" or estadoCivil=="D":
        estado=False
else:
        estado=True
print(estado)





