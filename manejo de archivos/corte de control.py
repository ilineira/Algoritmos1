def leer_info(ejs, default):
    linea = ejs.readline()
    return linea if linea else default

with open('movimientos.txt', 'rt') as movs:
    linea = leer_info(movs, '999999,0')
    nro_cta, importe = linea.rstrip().split(',')
    max = '999999'
    print (nro_cta, importe)
    total = 0
    while nro_cta != max:
        cta_ant = nro_cta
        tot_cta = 0
        print ('cta',cta_ant)
        print ('importe',importe)
        while nro_cta == cta_ant and nro_cta != max:
            print (importe)
            tot_cta+=int(importe)
            print (nro_cta, importe)
            linea = leer_info(movs, '999999,0')
            nro_cta, importe = linea.rstrip().split(',')
        print ('cierre')
        print ('El total de la cuenta {} es {}:'.format(cta_ant, tot_cta))
        total += tot_cta
print ('Total Gral:', total)