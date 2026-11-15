"""Excepciones al abrir ficheros (Tema 6)."""

# La ruta es relativa al directorio desde el que se ejecuta python
try:
    with open("datos/accesos.log", encoding="utf-8") as fichero:
        lineas = fichero.readlines()
except FileNotFoundError as error:
    print(error)
except PermissionError:
    print("Sin permisos para leer el fichero")
else:
    print("Líneas leídas:", len(lineas))

# Un solo except para los dos casos
try:
    with open("/etc/shadow", encoding="utf-8") as fichero:
        fichero.read()
except OSError as error:
    print(type(error).__name__)
