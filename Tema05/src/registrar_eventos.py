"""Registro de eventos de un servicio (Tema 5).
Cada llamada debe devolver solo los eventos que ha recibido.
"""


def registrar_evento(evento, historial=[]):
    historial.append(evento)
    return historial


print(registrar_evento("arranque"))
print(registrar_evento("fallo"))
