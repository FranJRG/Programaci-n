'''
numero1 = int(input("Dime un numero: "))
numero2 = int(input("Dime el segundo número: "))

while numero1 <= 0 and numero2 <= 0:
    numero1 = int(input("El numero introducido no es válido. Introduzca otro número: "))
    numero2 = int(input("El numero introducido no es válido. introduzca otro número: "))
    
if numero1>numero2:
    dividendo=numero1
    divisor=numero2
else:
    dividendo=numero2
    divisor=numero1

cociente=0

while dividendo>divisor:
    cociente+=1

numero = 9

for i in range(0, numero+1):
    print(str(numero)*i)
    


numero1, numero2 = 13, 7

contador= 0
inicio=numero1
total=" "
while contador<10:
    inicio+=1
    if inicio%numero2==0:
        contador+=1
        total=" "

print(f"{numero1} u {numero2} => " + total)

numero=int(input("Dime el tamaño de la frecuencia: "))
cadena =" "

for i in range (numero):
    
    cadena += str((-5)**i)
    if i < numero-1:
        cadena+=","
print(cadena)

numero=int(input("Dime el tamaño de la frecuencia: "))
cadena =" "

for i in range (numero):
    
    cadena += str(i(i%-3)+1)
    if i < numero-1:
        cadena+=","
print(cadena)

numero=int(input("Dime el tamaño de la frecuencia: "))
cadena =" "

for i in range (numero):
    
    cadena += str((3)**i)
    if i < numero-1:
        cadena+=","
print(cadena)


print("----------------")

numero = int(input("Dime un numero de comienzo: "))
cadena = int(input("Cual es la longitud de la secuencia: "))



print("----------------")

numero = int(input("Introduzca un numero: "))
lista=[numero]

while not (numero == 1):
    
    if numero % 2==0:
        numero = numero//2
        
    else:
        numero = numero*3+1
    
    
    lista.append(numero)
        
print(lista)
    
'''
edad = int(input("Que edad tiene Juan: "))
puzzle = 0
dinero = 0
acumulador_puzzle = 0
acumulador_dinero = 0

for i in range(1, edad+1):
    if edad == 1:
        puzzle = 1
        acumulador_puzzle+=1
    elif edad == 2:
        dinero = 20
        acumulador_dinero = dinero + 15
    elif edad % 2 == 0:
        dinero = acumulador_dinero
        acumulador_dinero = acumulador_dinero + 15
        acumulador_puzzle = acumulador_puzzle*2
    elif edad % 2 != 0:
        puzzle = acumulador_puzzle
        acumulador_puzzle = acumulador_puzzle*2
        acumulador_dinero = acumulador_dinero+15

print(f"Recibe {puzzle} y {acumulador_dinero}€")
     
    
    
    