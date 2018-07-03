def listado(lista):
    laux = []
    for palabra in lista:
        if palabra not in laux:
            laux.append(palabra)
    laux.sort()
    return laux

texto = input("ingrese texto: ")
lista = texto.lower().split()
continuar = True
while continuar:
    longitud = len(lista)
    if longitud < 100:
        texto_agregado = input("debe ingresar por lo menos {0} palabras: ".format(100 - longitud))
        lista += texto_agregado.lower().split()
    else:
        continuar = False
print(listado(lista))