def print_a(diccionario):
#hace el print del ejercico a
    for key, value in diccionario.items():
        print("en {0} hay {1} personas en edad laboral y {2} empleados".format(key, value[0], value[1]))
    return

def porcentaje_de_desocupacion(diccionario):
    for key, value in diccionario.items():
        PEA = value[0]
        empleados = value[1]
        desempleados = PEA - empleados
        porcentaje = (desempleados / PEA) * 100
        diccionario[key][2] = porcentaje
    return

def print_b(diccionario):
#hace el print del ejercicio b
    porcentaje_de_desocupacion(diccionario)
    for key, value in diccionario.items():
        print("localidad: ", key, " - % de desocupacion: %", value[2])
    return

#principal
diccionario = {}
status = True
while status:
    localidades = input("ingrese localidad: ")
    cantidad_de_personas_en_edad_laboral = int(input("ingrese cantidad de personas en edad laboral: "))
    cantidad_de_empleados = int(input("ingrese cantidad de empleados: "))
    if localidades not in diccionario:
        diccionario[localidades] = [cantidad_de_personas_en_edad_laboral, cantidad_de_empleados, 0]
    else:
        diccionario[localidades][0] += cantidad_de_personas_en_edad_laboral
        diccionario[localidades][1] += cantidad_de_empleados
    continuar = input("desea continuar? (si/no)")
    if continuar == "no":
        status = False
print_a(diccionario)
print_b(diccionario)




