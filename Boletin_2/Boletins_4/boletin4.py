import math
cateto1=float(input("Dime el cateto1:"))
cateto2=float(input("Dime el cateto2:"))
print("Hipotenusa=%.2f" % math.sqrt(cateto1**2+cateto2**2))


print("-------------------")

gradosf=float(input("Grados Fahrenheit:"))
gradosc=(gradosf*5/9)-32
print("Grados C:%.2f" % gradosc)

print("---------------")

numero1=float(input("Numero1:"))
numero2=float(input("Numero2:"))
numero3=float(input("Numero3:"))

print("Media:%.2f" % ((numero1+numero2+numero3)/3))

print("------------------")

total=float(input("Ingresa el dinero a pagar: "))
descuento=total* .15

print("El total a pagar es: ", total-descuento)
print("El descuento aplicacado es: ",descuento)

print("-------------------")

N1=float(input('''Ingrese el primer numero'''))
N2=float(input('''Ingrese el segundo numero'''))

R=abs(N1-N2)

print('La distancia entre ellos es: ',float(R))

print("-----------------")

import math

X1=(float(input("Ingrese X1")))
Y1=(float(input("Ingrese Y1")))
X2=(float(input("Ingrese X2")))
Y2=(float(input("Ingrese Y2")))

Distancia=float(math.sqrt(pow(X2-X1,2)+pow(Y2-Y1,2)))
print("La distancia es:, ", round(Distancia,3))

print("-----------")

import math
print("Raiz cuadrada y cubica de un numero")
N=(float(input("Ingrese el numero")))
R2=math.sqrt(N)
R3=N**(1/3)
print('La raiz cuadrada es: ',round(R2,3),'y la raiz cúbica es: ',round(R3,3))

print("------------------")

año=int(input("Dime un año"))

if año %4==0:
  if año %100==0:
    if año %400==0:
      print("El año",año,"es bisiesto")  
    else:
      print("El año",año,"no es bisiesto")
  else:
    print("El año",año,"es bisiesto")
else:
  print("El año",año,"no bisiesto")

print("-----------------------")

dias = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
 
numero = int(input("ingrese el numero del dia de semana: "))
 
print(dias[numero-1])

print("-------------------")

mes=int(input("Mes: "))        
if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
    print("31 días")
elif mes==4 or mes==6 or mes==9 or mes==11 :
    print("30 días")
elif mes==2:
    print("28 o 29 días")
else:
    print("Mes incorrecto")
    
print("-----------------")

tipo=input("nIndica el tipo de uva (A o B: ")
tamaño=int(input("Indica tamaño (1 o 2): "))

if (tipo=="A" or tipo =="B") and (tamaño==1 or tamaño==2):
    if tipo=="A" and tamaño==1:
        print("Se carga 20 cent")
    elif tipo=="A" and tamaño==2:
        print("Se carga 30 cent")
    elif tipo=="B" and tamaño==1:
        print("Se carga 30 cent")
    elif tipo=="B" and tamaño==2:
        print("Se carga 50 cent")
else:
    print("No es correcto")
    
    print("----------------------")
    
alumnos = int(input("Dime el numero de alumnos: "))
bus = 4000/alumnos

if alumnos>=100:
    print("Coste de cada alumno de %s euros"%(65+bus))
elif 50<=alumnos<=99:
    print("Coste de cada alumno de %s euros"%(70+bus))
elif 30<=alumnos<=49:
    print("Coste de cada alumno de %s euros"%(95+bus))
else:
    print("El coste de cada alumno en %s euros es"%(bus))
    

print("------------------")

tiempollamada=int(input("Dime el tiempo de llamada: "))
dia=input("Que dia la realizamos: ")
momentodia=input("En que momento la vamos a hacer: ")

if tiempollamada>=0:
    
    if 0<=tiempollamada<=5:
        coste=+1
    if 5<=tiempollamada<=8:
        coste=+1+0.80
    if 0<=tiempollamada<=5:
        coste=+1+0.80+0.70
    else:
        coste=1+0.80+0.70+0.50
        
    if dia=="Domingo":
        coste1=coste + (coste*0.03)
        print("El coste es", coste1)
    else:
        if momentodia=="mañana":
            coste1=coste + (coste*0.15)
            print("El coste es", coste1)
        elif momentodia=="tarde":
            coste1=coste + (coste*0.1)
            print("El coste es", coste1)
        else:
            print("Momento del dia incorrecto")
else:
    print("error")

print("-----------------------")  

angulo1=int(input("Dime el primer angulo: "))
angulo2=int(input("Dime el segundo angulo: "))
angulo3=int(input("Dime el tercer angulo: "))
A=int(input("Dime el valor del primer lado: "))
B=int(input("Dime el valor del segundo lado: "))
C=int(input("Dime el valor del tercer lado: "))
if A == B and A == C:
    print("Es equilatero")
elif (A == B and A != C) or (A !=B and A == C): 
        print("Es isósceles")
elif angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
        print("Es un triangulo rectángulo")
else:
    print("Es escaleno")
    
print("---------------------")

base=int(input("Dime la base"))
exponente=int(input("Dime el exponente"))

if exponente>0 :
    print("La potencia es ", base^exponente)

elif exponente==0:
    print("La potencia es 1")
else:
    print("La potencia es ",1/(base^abs(exponente)))
    


        
        
