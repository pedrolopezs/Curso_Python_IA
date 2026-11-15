"""Funciones para analizar un registro de accesos (Tema 6)."""


def leer_registro(ruta):
    """Devuelve las líneas no vacías del fichero."""
    with open(ruta, encoding="utf-8") as fichero:
        return [linea.strip() for linea in fichero
                if linea.strip()]


print("Módulo cargado:", __name__)

if __name__ == "__main__":
    lineas = leer_registro("Tema06/datos/accesos.log")
    print(len(lineas), "líneas")
