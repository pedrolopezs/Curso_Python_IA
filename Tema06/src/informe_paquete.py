"""Importa los módulos del paquete herramientas (Tema 6)."""
ruta = "Tema06/datos/accesos.log"

# Carga el módulo. Se usa con el prefijo completo
import herramientas.registro
lineas = herramientas.registro.leer_registro(ruta)
print(len(lineas))

# Carga el módulo. Se usa sin el prefijo del paquete
from herramientas import registro
lineas = registro.leer_registro(ruta)
print(len(lineas))

# Carga solo la función
from herramientas.registro import leer_registro
lineas = leer_registro(ruta)
print(len(lineas))

from herramientas.informes import contar_peticiones
totales, descartadas = contar_peticiones(lineas)
print(totales, descartadas)
