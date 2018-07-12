def analizar_texto(texto):
    if (" ," in texto) or (" ." in texto):
        return False
    return True

texto = input("ingrese texto: ")
print(analizar_texto(texto))