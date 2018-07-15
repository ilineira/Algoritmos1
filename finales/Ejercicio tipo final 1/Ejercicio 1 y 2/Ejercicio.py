#Leer de teclado (usando la función raw_input) los datos de un listado de alumnos terminados
# con padrón 0. Para cada alumno deben leer:
#*) Padrón
#*) Nombre
#*) Apellido
#*) Nota del primer parcial
#*) Nota del primer recuperatorio (en caso de no haber aprobado el parcial)
#*) Nota del segundo recuperatorio (en caso de no haber aprobado en el primero)
#*) Nombre del grupo
#*) Nota del TP 1
#*) Nota del TP 2
from leer_archivo import d


def verificar_nota(nota):
    continuar = True
    while continuar:
        if (nota < 0) and (nota > 10):
            nota = int(input("Ingrese nota valida(entre 0 y 10): "))
        else:
            continuar = False
    return nota


def verificar_padron(padron):
    continuar = True
    while continuar:
        if len(padron) < 2:
            padron = ""
            padron = input("Debe ingresar por lo menos 2 caracteres: ")
        else:
            continuar = False
    return padron


def leer_de_teclado(diccionario):
    continuar = True
    while continuar:
        padron = input("Ingrese numero de padron del alumno, ingrese 0 si no quiere ingresar mas alumnos: ")
        if padron != "0":
            padron = verificar_padron(padron)
            nombre = input("Ingrese nombre del alumno: ")
            apellido = input("Ingrese apellido del alumno: ")
            nota_del_primer_parcial = int(input("Ingrese nota del primer parcial: "))
            verificar_nota(nota_del_primer_parcial)
            nota_del_primer_recuperatorio = 0
            nota_del_segundo_recuperatorio = 0
            if nota_del_primer_parcial < 4:
                nota_del_primer_recuperatorio += int(input("Ingrese nota del primer recuperatorio: "))
                verificar_nota(nota_del_primer_recuperatorio)
                if nota_del_primer_recuperatorio < 4:
                    nota_del_segundo_recuperatorio += int(input("Ingrese nota del segundo recuperatorio: "))
                    verificar_nota(nota_del_segundo_recuperatorio)
            nombre_del_grupo = input("Ingrese nombre de grupo: ")
            nota_del_TP_1 = int(input("Ingrese nota del TP 1: "))
            nota_del_TP_1 = verificar_nota(nota_del_TP_1)
            nota_del_TP_2 = int(input("Ingrese nota del TP 2: "))
            nota_del_TP_2 = verificar_nota(nota_del_TP_2)
            diccionario[padron] = [nombre, apellido, nota_del_primer_parcial, nota_del_primer_recuperatorio,
                               nota_del_segundo_recuperatorio, nombre_del_grupo, nota_del_TP_1, nota_del_TP_2]
        else:
            continuar = False
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
#leer_de_teclado(d)
imprimir_a1(diccionario)
