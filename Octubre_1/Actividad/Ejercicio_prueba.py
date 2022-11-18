print("Bienvenido al gimnasio Jacafitness")

hora = int(input("A que hora quieres entrar: "))
dia=input("Que dia vamos a asistir ")

if (dia == "Lunes" or dia == "Viernes" or dia =="Miércoles" or dia == "Martes" or dia =="Jueves") and 12<=hora<22:
    
    if 12<=hora<14:
        print("Pase a la clase de Spinning")
    elif 16<=hora<20:
        print("Pase a la sala de yoga")
    elif 20<=hora<22:
        print("Pase a la clase de body Combat")
    
    else:
        print("No hay clases")
    if dia== "Martes" or dia == "Jueves":
    
        if 12<=hora<14:
            print("Pase a la sala de yoga")
        elif 16<=hora<20:
            print("Pase a la clase de Sipinning")
        elif 20<=hora<22:
            print("Pase a la clase de body Combat")
        
    else:
        print("No hay clases")

else:
    print("No hay clases disponibles")



 














