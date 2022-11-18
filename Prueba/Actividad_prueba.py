peso = float(input("Introduzca su peso: "))
edad = int(input("Introduzca su edad: "))
tipoVida = input("¿Que tipo de vida lleva?, Sedentaria,Activa o Muy Activa: ")

while peso>0 and peso<210:
    
    while 0<edad or edad>120:
        edad=int(input("La edad no es correcta. Introduzca de nuevo su edad: "))
    
    while tipoVida!="Sedentaria" and tipoVida!="Activa" and tipoVida!="Muy Activa":
        tipoVida=input("El tipoVida no es correcto. Introduzca de nuevo: ")

    if (edad>70 or tipoVida=="Sedentaria") and (peso>100) and (peso>74.4 or edad>50):
        print("Es recomendable acudir al médico")
    else:
        print("No es urgente acudir al médico")
    
    peso = float(input("Introduzca su peso: "))
    edad = int(input("Introduzca su edad: "))
    tipoVida = input("¿Que tipo de vida lleva?, Sedentaria,Activa o Muy Activa: ")