"""Argumentos de las funciones y expresiones lambda (Tema 5)."""


def crear_url(servidor, puerto=80, protocolo="http"):
    return f"{protocolo}://{servidor}:{puerto}"


# Posicionales, valores por defecto y argumentos por nombre
print(crear_url("web01"))
print(crear_url("web01", 8080))
print(crear_url("web01", protocolo="https", puerto=443))


# *usuarios recoge los argumentos posicionales sobrantes en una tupla
def contar_conectados(*usuarios):
    return len(usuarios)


print(contar_conectados("ana", "luis", "marta"))
print(contar_conectados())


# **datos recoge los argumentos con nombre sobrantes en un diccionario
def mostrar_ficha(equipo, **datos):
    print(equipo)
    for clave, valor in datos.items():
        print(f"  {clave}: {valor}")


mostrar_ficha("SW01", ubicacion="Sala 2", puertos=24)

# Una lambda como clave de ordenación
conexiones = [("web01", 120), ("db01", 45), ("web02", 300)]
print(sorted(conexiones, key=lambda conexion: conexion[1]))
print(max(conexiones, key=lambda conexion: conexion[1]))
