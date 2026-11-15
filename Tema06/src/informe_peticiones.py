"""Informe de peticiones por dirección IP de un registro."""
import sys

RUTA_PREDETERMINADA = "Tema06/datos/accesos.log"


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


if __name__ == "__main__":
    ruta = sys.argv[1] if len(sys.argv) > 1 else RUTA_PREDETERMINADA
    try:
        with open(ruta, encoding="utf-8") as fichero:
            lineas = [linea.strip() for linea in fichero if linea.strip()]
    except FileNotFoundError:
        print(f"No existe el fichero {ruta}", file=sys.stderr)
        sys.exit(1)
    # devuelve un diccionario de contadores y un entero
    totales, descartadas = contar_peticiones(lineas)
    for direccion in sorted(totales):
        print(direccion, totales[direccion])
    print("Líneas descartadas:", descartadas)
