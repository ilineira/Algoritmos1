def contar_palabras(texto):
    l = texto.split()
    contador = len(l)
    return contador

def agregar_palabras(texto):
    continuar = True
    while continuar:
        long = contar_palabras(texto)
        if long < 100:
            texto_a = input("ingrese por lo menos {0} palabras: ".format(100 - long))
            texto += (" " + texto_a)
        else:
            continuar = False
    return texto.lower().split()

def lista_reducida(lista):
    lista2 = []
    for i in lista:
        lista2.append(" " + i)
    lista3 = []
    for i in lista2:
        if (" ab" not in i) and (" pseudo" not in i):
            lista3.append(i)
    lista3.sort()
    return lista3

#principal
texto = input("ingrese texto: ")
texto_separado = agregar_palabras(texto)
l = lista_reducida(texto_separado)
print(l)


