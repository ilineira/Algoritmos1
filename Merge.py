def leer(archivo):
    linea = archivo.readline()
    if linea:
        return linea.strip('\n')
    else:
        return

def agregar_a(nuevo, palabra):
    print(palabra)
    nuevo.write(palabra + '\n')

def merge(txt1, txt2, txt3, nuevo, m):
    palabra1 = leer(txt1)
    palabra2 = leer(txt2)
    palabra3 = leer(txt3)
    l = [palabra1, palabra2, palabra3]
    lista = []
    while (palabra1 != m) or (palabra2 != m) or (palabra3 != m):
        l.sort()
        print(l)

        if l[0] == m:
            break

        elif l[0] == l[1] == l[2]:
            agregar_a(nuevo, palabra1)
            aux = palabra1
            aux2 = palabra2
            aux3 = palabra3
            while aux == palabra1:
                palabra1 = leer(txt1)
            while aux2 == palabra2:
                palabra2 = leer(txt2)
            while aux3 == palabra3:
                palabra3 = leer(txt3)
            l = [palabra1, palabra2, palabra3]

        elif l[0] == l[1]:
            agregar_a(nuevo, palabra1)
            aux = palabra1
            aux2 = palabra2
            while aux == palabra1:
                palabra1 = leer(txt1)
            while aux2 == palabra2:
                palabra2 = leer(txt2)
            l = [palabra1, palabra2, palabra3]

        elif l[0] == palabra1:
            agregar_a(nuevo, palabra2)
            aux = palabra1
            while aux == palabra1:
                palabra1 = leer(txt1)
            l = [palabra1, palabra2, palabra3]

        elif l[0] == palabra2:
            agregar_a(nuevo, palabra2)
            aux = palabra2
            while aux == palabra2:
                palabra2 = leer(txt2)
            l = [palabra1, palabra2, palabra3]

        else:
            agregar_a(nuevo, palabra3)
            aux = palabra3
            while aux == palabra3:
                palabra3 = leer(txt3)
            l = [palabra1, palabra2, palabra3]

m = 'zzz'
t1 = open('archivo1.txt', 'r')
t2 = open('archivo2.txt', 'r')
t3 = open('archivo3.txt', 'r')
n = open('palabras.txt', 'w')
merge(t1, t2, t3, n, m)
t1.close()
t2.close()
t3.close()