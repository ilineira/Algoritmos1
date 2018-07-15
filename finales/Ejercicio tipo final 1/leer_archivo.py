def leer_de_linea(linea):
    return linea.strip('\n').split(',')


def es_valida(linea):
    return linea != ''


def leer_archivo(diccionario):
    with open("datos.txt", 'r', encoding="utf-8") as archivo:
        linea = archivo.readline()
        while es_valida(linea):
            padron, nombre, apellido, nota_del_primer_parcial, nota_del_primer_recuperatorio, nota_del_segundo_recuperatorio, nombre_del_grupo, nota_del_TP_1, nota_del_TP_2 = leer_de_linea(linea)
            diccionario[padron] = [str(padron), str(nombre), str(apellido), int(nota_del_primer_parcial), int(nota_del_primer_recuperatorio), int(nota_del_segundo_recuperatorio), str(nombre_del_grupo), int(nota_del_TP_1), int(nota_del_TP_2)]
        return diccionario

def imprimir_a1(diccionario):
    print("Estan en condicion de rendir coloquio:\n")
    for key, value in diccionario.items():
        #if ((value[2] > 0) or (value[3] != 0) or (value[4] != 0)) and (value[6] >= 4) and (value[7] >= 4):
        if (max(value[2::4]) >= 4) and (value[6] >= 4) and (value[7] >= 4):
            print(value[0], " ", value[1], "\n")
    return


def imprimir_a2(diccionario):
    return


#principal
diccionario = {}
d = leer_archivo(diccionario)
imprimir_a1(d)
