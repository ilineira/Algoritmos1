def definir_diccionario():
    d = {}
    d["100"] = ["ignacio", "l", 2, 3, 5, "a", 4, 5]
    d["200"] = ["leandro", "l", 9, 0, 0, "b", 6, 8]
    d["300"] = ["andres", "a", 0, 0, 0, "c", 5, 6]
    d["400"] = ["pablo", "p", 1, 4, 0, "d", 0, 5]
    d["500"] = ["justo", "v", 8, 0, 0, "e", 5, 0]
    d["600"] = ["julieta", "l", 7, 0, 0, "f", 0, 0]
    d["700"] = ["silvina", "b", 0, 0, 0, "g", 5, 5]
    d["800"] = ["mariano", "l", 0, 0, 0, "h", 0, 0]
    d["900"] = ["francisco", "l", 9, 0, 0, "i", 8, 8]
    return d


def condicion_de_rendir_coloquio(l):
        nota_ultimo_parcial_aprobado = max(l[0], l[1], l[2])
        parcial_aprobado = True if (nota_ultimo_parcial_aprobado >= 4) else False
        TPs_aprobados = True if (l[3] >= 4) and (l[4] >= 4) else False
        if parcial_aprobado and TPs_aprobados:
            return True
        return False


def promedio(lista):
    contador = len(lista)
    contador_notas = 0
    for i in lista:
        contador_notas += i
    promedio = contador_notas / contador
    return float(promedio)


def imprimir_a1(diccionario):
    print("\nEjercicio a.1\nEstan en condicion de rendir coloquio:")
    for key, value in diccionario.items():
        laux = [value[2], value[3], value[4], value[6], value[7],]
        if condicion_de_rendir_coloquio(laux):
            print(value[0], " ", value[1])
    return


def imprimir_a2(diccionario):
    print("\nEjercicio a.2")
    lista2 = []
    for key, value in diccionario.items():
        laux = [value[2], value[3], value[4], value[6], value[7],]
        if condicion_de_rendir_coloquio(laux):
            lista = [key, value[0], value[1]]
            lista2.append(lista)
            lista = []
    lista2.sort()
    longitud = len(lista2)
    if longitud == 0:
        print("No hay alumnos en condicion de rendir coloquio")
    else:
        print("Estan en condicion de rendir coloquio:")
        if longitud >= 5:
            for elemento in lista2[0:4]:
                print("Padron: {0} - Alumno: {1} {2}".format(elemento[0], elemento[1], elemento[2]))
        else:
            for elemento in lista2[0:(longitud)]:
                print("Padron: {0} - Alumno: {1} {2}".format(elemento[0], elemento[1], elemento[2]))
    return


def imprimir_a3(diccionario):
    print("\nEjercicio a.3")
    lista2 = []
    for key, value in diccionario.items():
        nota_parcial = max(value[2], value[3], value[4])
        laux = [value[2], value[3], value[4], value[6], value[7],]
        if condicion_de_rendir_coloquio(laux):
            lista = [nota_parcial, key, value[0], value[1]]
            lista2.append(lista)
            lista = []
    lista2.sort(key = lambda item: (item[0], item[1]))
    longitud = len(lista2)
    if longitud == 0:
        print("No hay alumnos en condicion de rendir coloquio")
    else:
        print("Estan en condicion de rendir coloquio:")
        if longitud >= 5:
            for elemento in lista2[0:4]:
                print("Padron: {0} - Alumno: {1} {2}".format(elemento[0], elemento[1], elemento[2]))
        else:
            for elemento in lista2[0:(longitud)]:
                print("Padron: {0} - Alumno: {1} {2}".format(elemento[0], elemento[1], elemento[2]))
    return


def ejercicio_b(diccionario):
    print("\nEjercicio b")
    for key, value in diccionario.items():
        l_parciales = [value[2], value[3], value[4]]
        promedio_parciales = promedio(l_parciales)
        l_TPs = [value[6], value[7]]
        promedio_TPs = promedio(l_TPs)
        l_promedio_gral = [promedio_parciales, promedio_TPs]
        promedio_gral = promedio(l_promedio_gral)
        print("El promedio del alumno con padron: {0} es {1}".format(key, promedio_gral))
    return


def ejercicio_c(diccionario):
    print("\nEjercicio c")
    lista = []
    for key,value in diccionario.items():
        lista.append(value[2])
        lista.append(value[3])
        lista.append(value[4])
    repeticiones = 0
    numero = 0
    for i in lista:
        apariciones = lista.count(i)
        if apariciones > repeticiones:
            repeticiones = apariciones
            numero = i
    print("La nota que mas aparecio fue {0} y aparecio {1} veces".format(numero, repeticiones))
    return


def ejercicio_d(diccionario):
    print("\nEjercicio d")
    lista = []
    lista2 = []
    lista3 = []
    lista4 = []
    for key, value in diccionario.items():
        lista = [value[2], key]
        lista2.append(lista)
        lista = []
    lista2.sort()
    for elemento in lista2:
        nota = elemento[0]
        for i in range((lista2.count(nota) - 1)):
            padron = elemento[1]
            if nota not in lista3:
                lista3 = [nota, padron]
            else:
                lista3.append(padron)
        if lista3[0] not in lista4:
            lista4.append(lista3)
            lista3 = []
    for i in lista4:
        print("Nota: {0}\n*{1}".format(i[0], i[1:len(i)]))
    return

def main():
    #value[0] = nombre
    #value[1] = apellido
    #value[2] = primer parcial
    #value[3] = primer recu
    #value[4] = segundo recu
    #value[5] = grupo
    #value[6] = TP1
    #value[7] = TP2
    d = definir_diccionario()
    #imprimir_a1(d)
    #imprimir_a2(d)
    #imprimir_a3(d)
    #ejercicio_b(d)
    #ejercicio_c(d)
    ejercicio_d(d)
    return


if __name__ == '__main__':
    main()

