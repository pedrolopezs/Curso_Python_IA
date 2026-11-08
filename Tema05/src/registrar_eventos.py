"""Registro de eventos de un servicio (Tema 5).
Cada llamada debe devolver solo los eventos de su propio historial.
"""


def registrar_evento(evento, historial=[]):
    historial.append(evento)
    return historial


primero = registrar_evento("arranque")
segundo = registrar_evento("fallo")
print("Primero:", primero)
print("Segundo:", segundo)
