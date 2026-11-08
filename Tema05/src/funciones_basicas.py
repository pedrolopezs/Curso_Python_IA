"""Funciones, return y varios valores (Tema 5)."""


# Devuelve el resultado, por lo que se puede guardar y comparar
def convertir_a_gb(megabytes):
    return megabytes / 1024


# Solo muestra el resultado y no devuelve nada
def mostrar_en_gb(megabytes):
    print(megabytes / 1024)


# Devuelve dos valores, que Python agrupa en una tupla
def separar_direccion(direccion):
    ip, puerto = direccion.split(":")
    return ip, int(puerto)


# Varios return: se ejecuta el primero que se cumple
def clasificar_puerto(puerto):
    if puerto < 1024:
        return "sistema"
    if puerto < 49152:
        return "registrado"
    return "dinámico"


tamanio = convertir_a_gb(2048)
print(tamanio)
print(tamanio > 1)

resultado = mostrar_en_gb(2048)
print(resultado)

print(separar_direccion("10.0.0.5:443"))
ip, puerto = separar_direccion("10.0.0.5:443")
print(ip, puerto)

print(clasificar_puerto(22), clasificar_puerto(8080))
print(clasificar_puerto(50000))
