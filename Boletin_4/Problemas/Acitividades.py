numero = int(input("Dime un numero"))

if numero%2==0:
    print("Par")
else:
    print("Impar")
    
print("-------------")

numero1 = int(input("Dime el primer numero "))
numero2 = int(input("Dime el segundo numero "))

if numero1 == numero2:
    print("Son iguales")
elif numero1<numero2:
    print("El segundo es mayor")
else:
    print("El primero es mayor")
    
print("--------------")

numero = int(input("Cual es el numero"))

if numero%2==0 and numero%3==0:
    print("Es múltiplo de 2 y de 3")
elif numero%2==0:
    print("Es múltiplo de 2")
elif numero%3==0:
    print("Es multilpo de 3")
    
print("----------------")

numero=int(input("Cual es la edad de la persona: "))

if 0<=numero<=12:
    print("Es un niño")
elif 13<=numero<=17:
    print("Es un adolescente")
elif 18<=numero<=29:
    print("Es un joven")
elif 30<=numero<100:
    print("Es un adulto")
    
print("--------------")

numero1 = int(input("Cual es el numero"))
numero2 = int(input("Cual es el numero"))
numero3 = int(input("Cual es el numero"))
numero4 = int(input("Cual es el numero"))
media = (numero1 + numero2 + numero3 + numero4)/4

if media < numero1:
    print("Media %s la media es %s"%(media,numero1))
    
if media < numero2:
    print("Media %s la media es %s"%(media,numero2))

if media < numero3:
    print("Media %s la media es %s"%(media,numero3))

if media < numero4:
    print("Media %s la media es %s"%(media,numero4))
    
print("-----------------")

letra = input("Dime una letra")

if letra=="A" or letra=="E" or letra=="I" or letra=="O" or letra=="U":
    print("Es una vocal")

    if letra == "A":
        print("Es la primera vocal (A)")

    elif letra == "E":
        print("Es la segunda vocal (E)")
    
    elif letra == "I":
        print("Es la tercera vocal (I)")
    
    elif letra == "O":
        print("Es la cuarta vocal (O)")
    
    elif letra == "U":
        print("Es la quinta vocal (U)")

else:
    print("No es una vocal")
    
print("----------------------")

Estado = input("Como se encuentra")
Edad = int(input("Dime su edad: "))

if Estado == "S" or Estado == "D" and Edad<35:
    print("La retención es del 12%")
    
elif Edad>35:
    print("La retención es del 8,5%")
    
elif Estado == "V" or Estado == "C" and Edad<35:
    print("La retención es del 11,3%")

else:
    print("Se le aplica un 10,5%")

print("-----------------------")

hora1=int(input("Dime la primera hora"))
minutos1=int(input("Dime los minutos"))
segundos1=int(input("Dime los segundos"))
hora2=int(input("Dime la segunda hora"))
minutos2=int(input("Dime los minutos"))
segundos2=int(input("Dime los segundos"))

if 0<=hora1<=23 and 0<=hora2<=23 and hora1>hora2:
    print("Hora 1 es mayor")

elif 0<=hora1<=23 and 0<=hora2<=23 and hora1<hora2:
    print("Hora 2 es mayor")

elif 0<=hora1<=23 and 0<=hora2<=23 and hora1==hora2:
    
    if 0<=minutos1<=23 and 0<=minutos2<=23 and minutos1>minutos2:
        print("Hora 1 es mayor")
    
    elif 0<=minutos1<=23 and 0<=minutos2<=23 and minutos1<minutos2:
        print("Hora 2 es mayor")
    
    elif 0<=minutos1<=23 and 0<=minutos2<=23 and minutos1==minutos2:
        
        if 0<=segundos1<=23 and 0<=segundos2<=23 and segundos1>segundos2:
            print("Hora 1 es mayor")
            
        elif 0<=segundos1<=23 and 0<=segundos2<=23 and segundos1<segundos2:
            print("Hora 2 es mayor")
        
        elif 0<=segundos1<=23 and 0<=segundos2<=23 and segundos1==segundos2:
            print("Son iguales")
            
            
print("-------------------")

Producto = (input("Cual es el producto"))
Precio = int(input("Cual es el precio"))

if Producto=="A":
    print(Precio-(Precio*7/100))
    
elif Producto=="C" or Precio<500:
    print(Precio-(Precio*12/100))
     
else:
    print(Precio-(Precio*7/100))
    
print("------------------")

caracter=input("Dime un caracter")
numero1=int(input("Dime el primer numero"))
numero2=int(input("Dime el segundo numero"))

if caracter=="*":
    print(numero1 * numero2)
elif caracter=="+":
    print(numero1 + numero2)
elif caracter=="-":
    print(numero1 - numero2)
elif caracter=="/":
    print(numero1 / numero2)








    