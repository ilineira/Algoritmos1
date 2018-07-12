def analizar_texto(texto):
    lista = sacar_vocales(texto)[::-1]
    imprimir(lista)
    return

def sacar_vocales(texto):
    lista = []
    for letra in texto.upper():
        if letra not in "AEIOU":
            lista.append(letra)
    return lista

def imprimir(lista):
    texto_definitivo = ""
    for letra in lista:
        texto_definitivo += letra
    print(texto_definitivo)
    return

#principal
texto = input("ingrese texto: ")
analizar_texto(texto)
