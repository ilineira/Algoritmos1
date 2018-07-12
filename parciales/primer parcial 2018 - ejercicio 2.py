def analizar_texto(texto):
    lista = texto.split()
    laux = []
    for palabra in lista:
        if (len(palabra) > 3) and (len(palabra) <10) and (palabra not in laux):
            laux.append(palabra)
        laux.sort(key = lambda item: (len(item), item))
    return laux

#principal
texto = input("ingrese texto: ")
lista = analizar_texto(texto)
print(lista)
