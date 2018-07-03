def relacion(diccionario):
#calcula el valor de la relacion habitantes/CAS
    for key, value in diccionario.items():
        relacion = value[0] / value[1]
        diccionario[key][2] = relacion
    return

def print_a(diccionario):
#hace el print del ejercicio a
    for key, value in diccionario.items():
        print("hay {0} habitantes y {1} CAS en {2}".format(value[0], value[1], key))
    return

def print_b(diccionario):
# hace el print del ejercicio b
    lista = []
    lista2 = []
    for key, value in diccionario.items():
        lista.append(value[2])
        lista.append(key)
        lista2.append(lista)
        lista = []
    lista2.sort(reverse=True)
    for elementos in lista2[0:5]:
        print("localidad: ", elementos[1], " - relacion: ", elementos[0])
    return 

#principal
diccionario = {}
ciclo = True
while ciclo:
    localidades = input("ingrese localidad: ")
    cantidad_de_habitantes = int(input("ingrese cantidad de habitantes: "))
    cantidad_de_CAS = int(input("ingrese cantidad de CAS: "))
    if localidades in diccionario:
        diccionario[localidades][0] += cantidad_de_habitantes
        diccionario[localidades][1] += cantidad_de_CAS
    else:
        diccionario[localidades] = [cantidad_de_habitantes, cantidad_de_CAS, 0]
    continuar = input("desea continuar?(si/no)")
    if continuar == "no":
        relacion(diccionario)
        ciclo = False
imprimir_a = print_a(diccionario)
imprimir_b = print_b(diccionario)