"""Escribir y agregar contenido a un fichero de texto (Tema 6)."""

ruta = "Tema06/resumen.txt"

# El modo "w" crea el fichero o lo vacía si ya existe
with open(ruta, "w", encoding="utf-8") as fichero:
    fichero.write("Resumen de peticiones\n")
    caracteres = fichero.write("10.0.0.5 4\n")
    print(caracteres)
    print("10.0.0.7 3", file=fichero)

# El modo "a" agrega al final sin borrar
with open(ruta, "a", encoding="utf-8") as fichero:
    fichero.write("10.0.0.9 3\n")

with open(ruta, encoding="utf-8") as fichero:
    print(fichero.read())

# Abrir con "w" vacía el fichero aunque no se escriba nada
with open(ruta, "w", encoding="utf-8") as fichero:
    fichero.write("")
with open(ruta, encoding="utf-8") as fichero:
    print(len(fichero.read()))
