def leer(archivo, defalut):
    linea = archivo.readline()
    return linea if linea else defalut

max = '999999999999'
archivo1 = open('archivo1.txt', 'rt')
archivo2 = open('archivo2.txt', 'rt')
linea1 = leer(archivo1, "max, '0'")
linea2 = leer(archivo2, "max, '0'")
cta1, importe1 = linea1.strip().split(',')
cta2, importe2 = linea2.strip().split(',')
total_gral = 0
while (cta1 != max) or (cta2 != max):
    menor = min(cta1, cta2)
    total = 0
    while cta1 == menor:
        total += int(importe1)
        linea1 = leer(archivo1, "max, '0'")
        cta1, importe1 = linea1.strip().split(',')
    while cta2 == menor:
        total += int(importe2)
        linea2 = leer(archivo1, "max, '0'")
        cta2, importe2 = linea2.strip().split(',')
    print(total)
    total_gral += total
print(total_gral)
archivo1.close()
archivo2.close()