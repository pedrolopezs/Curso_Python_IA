"""Módulo del paquete herramientas para leer un registro."""


def leer_registro(ruta):
    """Devuelve las líneas no vacías del fichero."""
    with open(ruta, encoding="utf-8") as fichero:
        return [linea.strip() for linea in fichero
                if linea.strip()]
