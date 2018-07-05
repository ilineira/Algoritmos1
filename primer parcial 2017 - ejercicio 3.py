def print_a(diccionario):
    for key, value in diccionario.items():
        print("{0} tuvo {1} votos".format(key, value))
    return

def print_b(diccionario):
    lista = []
    laux = []
    for key, value in diccionario.items():
        laux.append(value)
        laux.append(key)
        lista.append(laux)
        laux = []
    lista.sort(reverse = True)
    print("orden por cantidad de votos decreciente: ")
    for elementos in lista:
        print(elementos[0], " - ", elementos[1])
    return

diccionario = {}
status = True
while status:
    partido_politico = input("ingrese partido politico: ")
    cantidad_de_votos = int(input("ingrese cantidad de votos: "))
    if partido_politico not in diccionario:
        diccionario[partido_politico] = cantidad_de_votos
    else:
        diccionario[partido_politico] += cantidad_de_votos
    continuar = input("desea continuar? (si/no)")
    if continuar == "no":
        status = False
print_a(diccionario)
print_b(diccionario)
