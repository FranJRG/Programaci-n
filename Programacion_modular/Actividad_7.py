pieza1= "[3,4]"
pieza2= "[2,5]"

def encajan(cadena1, cadena2):
    
    if (cadena1[1] or cadena1[3]) == (cadena2[1] or cadena2[3]):
        resultado = True
    else:
        resultado = False
    
    return resultado

print(encajan(pieza1, pieza2))
        