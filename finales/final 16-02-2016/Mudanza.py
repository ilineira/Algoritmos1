def leer_de_linea(linea):
    return linea.strip('\n').split(',')


def es_valida(linea):
    return linea != ''

def procesar_mudanza():
    s_peso_total = 0
    s_vol_total = 0
    l_peso_total = 0
    l_vol_total = 0
    with open('faltantes.txt', 'w', encoding="utf-8") as faltantes:
        with open('salida.csv', 'r', encoding="utf-8") as archsalida:
            with open('llegada.csv', 'r', encoding="utf-8") as archllegada:
                linea = archsalida.readline()
                linea2 = archllegada.readline()
                while es_valida(linea) and es_valida(linea2):
                    s_id, s_hora, s_peso, s_vol, s_desc = leer_de_linea(linea)
                    l_id, l_hora, l_peso, l_vol, l_desc = leer_de_linea(linea2)
                    if s_id < l_id:
                        faltantes.write("El articulo " + s_desc + " con hora de salida " + s_hora + " no llego a destino​\n​")

                        s_peso_total += int(s_peso)
                        s_vol_total += int(s_vol)

                        linea = archsalida.readline()

                        #puede resolverse sin el continue, reemplazando el cuerpo del while por un if..elif..else
                        continue

                    #se supone que s_id == l_id para el resto de los casos por no poder venir elementos en la llegada que no esten en la salida
                    if (float(s_peso) > (float(l_peso) + 0.25)):
                        faltantes.write("El cajon " + s_desc + " salio con " + s_peso + "kg de origen y llego con " + l_peso + "kg a detino\n")

                    s_peso_total += int(s_peso)
                    s_vol_total += int(s_vol)
                    l_peso_total += int(l_peso)
                    l_vol_total += int(l_vol)

                    linea = archsalida.readline()
                    linea2 = archllegada.readline()

                while es_valida(linea):
                    s_id, s_hora, s_peso, s_vol, s_desc = leer_de_linea(linea)
                    faltantes.write("El articulo " + s_desc + " con hora de salida " + s_hora + " no llego a destino​\n​")

                    linea = archsalida.readline()

                print("Peso total: {}/{}\nVol. total: {}/{}".format(s_peso_total, l_peso_total, s_vol_total, l_vol_total))

def main():
    procesar_mudanza()

if __name__ == '__main__':
    main()
