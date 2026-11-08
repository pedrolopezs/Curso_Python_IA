"""Informe de peticiones por dirección IP de un registro (Tema 5)."""

UMBRAL_PETICIONES = 3

registro = [
    "10.0.0.5 GET /index",
    "10.0.0.7 GET /admin",
    "10.0.0.5 POST /login",
    "10.0.0.9 GET /index",
    "10.0.0.5 GET /admin",
    "10.0.0.7 GET /index",
]


def extraer_direccion(linea):
    """Devuelve la dirección IP de una línea del registro."""
    return linea.split()[0]


def contar_peticiones(lineas):
    """Devuelve un diccionario con las peticiones de cada dirección."""
    totales = {}
    for linea in lineas:
        direccion = extraer_direccion(linea)
        totales[direccion] = totales.get(direccion, 0) + 1
    return totales


def clasificar(peticiones, umbral=UMBRAL_PETICIONES):
    """Devuelve 'sospechosa' si se alcanza el umbral y 'normal' si no."""
    if peticiones >= umbral:
        return "sospechosa"
    return "normal"


totales = contar_peticiones(registro)
for direccion in sorted(totales):
    peticiones = totales[direccion]
    print(f"{direccion:<9} {peticiones} {clasificar(peticiones)}")

sospechosas = [direccion for direccion, peticiones in totales.items()
               if clasificar(peticiones) == "sospechosa"]
print("Sospechosas:", sospechosas)

paginas = {linea.split()[2] for linea in registro}
print("Páginas:", sorted(paginas))
