"""Lectura de un fichero de texto con open() y with (Tema 6)."""

ruta = "Tema06/datos/accesos.log"

# open() devuelve un objeto fichero que hay que cerrar con close()
fichero = open(ruta, "r", encoding="utf-8")
print(type(fichero))
print(fichero.name, fichero.mode)
contenido = fichero.read()
print(contenido[:19])
fichero.close()
print(fichero.closed)

# with cierra el fichero al salir del bloque
with open(ruta, encoding="utf-8") as fichero:
    primera = fichero.readline()
    print(fichero.closed)
print(primera.strip())
print(fichero.closed)

# read() devuelve todo el contenido en una cadena
with open(ruta, encoding="utf-8") as fichero:
    contenido = fichero.read()
print(type(contenido))
print(len(contenido.splitlines()))

# readline() lee una línea y readlines() las que quedan
with open(ruta, encoding="utf-8") as fichero:
    primera = fichero.readline()
    restantes = fichero.readlines()
print(repr(primera))
print(len(restantes))

# Cada línea conserva su salto de línea, por lo que print() deja un hueco
print("--- Sin strip()")
with open(ruta, encoding="utf-8") as fichero:
    for linea in fichero:
        print(linea)

# strip() elimina el salto de línea
print("--- Con strip()")
with open(ruta, encoding="utf-8") as fichero:
    for linea in fichero:
        print(linea.strip())

# enumerate() numera las líneas y la condición omite las vacías
print("--- Con enumerate()")
with open(ruta, encoding="utf-8") as fichero:
    for numero, linea in enumerate(fichero, start=1):
        if linea.strip():
            print(numero, linea.strip())
