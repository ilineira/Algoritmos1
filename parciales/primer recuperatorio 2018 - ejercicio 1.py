def analizar_texto(texto):
    lista = texto.split()
    status = True
    for palabra in lista:
        if (len(palabra) > 6):
            status = False
    return status
