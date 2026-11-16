"""Excepción propia IncidenciaError (Tema 7)."""


class IncidenciaError(Exception):
    """Error al crear una incidencia."""


def abrir_incidencia(prioridad):
    if prioridad not in ("alta", "media", "baja"):
        raise IncidenciaError(
            f"Prioridad no válida: {prioridad}")
    return prioridad


try:
    abrir_incidencia("urgente")
except IncidenciaError as error:
    print(error)

print(issubclass(IncidenciaError, Exception))

try:
    abrir_incidencia("urgente")
except Exception as error:
    print(type(error).__name__)
