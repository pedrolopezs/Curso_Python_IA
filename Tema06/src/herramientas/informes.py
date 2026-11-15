"""Módulo del paquete herramientas para resumir un registro."""


def contar_peticiones(lineas):
    """Devuelve las peticiones de cada dirección y las descartadas."""
    totales = {}
    descartadas = 0
    for linea in lineas:
        try:
            direccion, metodo, pagina = linea.split()
        except ValueError:
            descartadas += 1
        else:
            totales[direccion] = totales.get(direccion, 0) + 1
    return totales, descartadas
