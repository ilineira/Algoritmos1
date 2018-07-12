#!/usr/bin/python


def leer_de_linea(linea):
    return linea.strip('\n').split(',')


def es_valida(linea):
    return linea != ''


def procesar_mudanza():
    with open("faltantes.txt", "w") as faltantes, open("salida.csv", "r") as salida, \
            open("llegada.csv", "r") as llegada:

        s_peso_total = 0
        s_vol_total = 0
        l_peso_total = 0
        l_vol_total = 0

        linea = salida.readline()
        linea2 = llegada.readline()

        while es_valida(linea) and es_valida(linea2):
            s_id, s_hora, s_peso, s_vol, s_desc = leer_de_linea(linea)
            l_id, l_hora, l_peso, l_vol, l_desc = leer_de_linea(linea2)
            if s_id < l_id:
                faltantes.write("El articulo {0} con hora de salida {1} no llego a destino​\n​"
                            .format(s_desc, s_hora))

                s_peso_total += int(s_peso)
                s_vol_total += int(s_vol)

                linea = salida.readline()
                # puede resolverse sin el continue, reemplazando el cuerpo del while por un if..elif..else
                continue
            # se supone que s_id == l_id para el resto de los casos por no poder venir elementos en la llegada
            # que no esten en la salida
            if float(s_peso) > float(l_peso) + 0.25:
                faltantes.write("El cajon {0} salio con {1} kg de origen y llego con {2} kg a destino​\n​"
                            .format(s_desc, s_peso, l_peso))

            s_peso_total += int(s_peso)
            s_vol_total += int(s_vol)
            l_peso_total += int(l_peso)
            l_vol_total += int(l_vol)

            linea = salida.readline()
            linea2 = llegada.readline()

            while es_valida(linea):
                s_id, s_hora, s_peso, s_vol, s_desc = leer_de_linea(linea)
                faltantes.write("El articulo {0} con hora de salida {1} no llego a destino​\n​".format(s_desc, s_hora))

                linea = salida.readline()
                print("Peso total: {0}/{1}​\n​Vol. total: {2}/{3}"
                      .format(s_peso_total, l_peso_total, s_vol_total, l_vol_total))
    return


#principal
procesar_mudanza()