"""Listas como argumentos y valor por defecto mutable (Tema 5)."""


# La función modifica la lista recibida
def agregar_regla(reglas, nueva):
    reglas.append(nueva)


# La función trabaja con una copia y devuelve la lista nueva
def ampliar_reglas(reglas, nueva):
    copia = reglas.copy()
    copia.append(nueva)
    return copia


firewall = ["permitir 22", "permitir 80"]
agregar_regla(firewall, "permitir 443")
print(firewall)
ampliadas = ampliar_reglas(firewall, "denegar 23")
print(ampliadas)
print(firewall)


# Error clásico: la lista por defecto se crea una sola vez
def anotar_alerta(mensaje, historial=[]):
    historial.append(mensaje)
    return historial


print(anotar_alerta("disco lleno"))
print(anotar_alerta("cpu alta"))


# Solución habitual: None como valor por defecto
def anotar_alerta_segura(mensaje, historial=None):
    if historial is None:
        historial = []
    historial.append(mensaje)
    return historial


print(anotar_alerta_segura("disco lleno"))
print(anotar_alerta_segura("cpu alta"))
