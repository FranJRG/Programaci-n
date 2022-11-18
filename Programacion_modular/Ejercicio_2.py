lista = [1, 3, 5, 7]
lista_nueva = []
escribir = 0
guardar = 0

for i in range(len(lista)):
    if i == 0:
        escribir+=lista[i]
        guardar+=lista[i+1]
        lista_nueva.append(guardar)
    elif i == 1:
        escribir+=lista[i]
        guardar+=lista[i+1]
        lista_nueva.append(guardar)
    elif i == 2:
        escribir+=lista[i]
        guardar+=lista[i+1]
        lista_nueva.append(guardar)
    elif i == 3:
        escribir+=lista[i]
        lista_nueva.append(escribir)
        
print(lista_nueva)
    
    
    