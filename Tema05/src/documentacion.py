"""Docstrings, anotaciones de tipo y consulta de la documentación (Tema 5)."""


def calcular_media(valores):
    """Devuelve la media de una lista de números."""
    return sum(valores) / len(valores)


def calcular_ocupacion(usado: int, total: int, decimales: int = 1) -> float:
    """Calcula el porcentaje de disco ocupado.

    Parámetros:
        usado: gigabytes ocupados.
        total: capacidad del disco en gigabytes.
        decimales: decimales del resultado.

    Devuelve el porcentaje como número decimal.
    """
    return round(usado / total * 100, decimales)


print(calcular_media.__doc__)
print(calcular_media.__name__)
print(calcular_ocupacion.__doc__)
print(calcular_ocupacion(87, 250))
