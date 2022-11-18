"""
nota = int(input("Dime que nota has sacado: "))

if 90<=nota<=100:
    print("Sobresaliente")
elif 70<=nota<=89:
    print("Notable")
elif 60<=nota<=69:
    print("Bien")
elif 50<=nota<=59:
    print("Suficiente")
elif 0<=nota<=49:
    print("Suspenso")
    
print("-------------------")

dia = int(input("Que dia es: "))
mes = input("En que mes estamos: ")
hemisferio = input("Hemisferio Norte o Hemisferio Sur: ").upper()

if hemisferio=="NORTE":
    if (mes == 9 and 23<=dia <= 30) or (mes==10 and 1<=dia<=31 or mes==11 and 1<=dia<=30) or (mes==12 and 1<=dia<=21):
        print("Es otoño")

elif hemisferio == "SUR":
    if (3<=mes<=5) and ((21 <=dia <=30) or (1<=dia<=20)):
        print("Es otoño")
        
print("--------------------")

fecha = "01-12-2022"
print(len("dd-mm-yyyy"))
print("dia %s, mes %s" % (fecha[0:2], fecha [3:5], fecha[6:11]))
"""

nombre= "Rigoberta Bandini"
inversa=""
tmp = ""
for i in range(len(nombre)):
    inversa = inversa + nombre 
    
for a in nombre:
    tmp = a + tmp
    
print(inversa, tmp)

