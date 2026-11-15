"""Importa el módulo registro y lo utiliza (Tema 6)."""
import registro

lineas = registro.leer_registro("Tema06/datos/accesos.log")
print(len(lineas))
print(registro.leer_registro.__doc__)
