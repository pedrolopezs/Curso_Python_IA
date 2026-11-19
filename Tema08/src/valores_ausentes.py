"""Valores ausentes en un fichero de datos (Tema 8)."""
import numpy as np

ruta = "Tema08/datos/latencias_ausentes.csv"

# loadtxt no admite celdas sin un número
try:
    np.loadtxt(ruta, delimiter=",", skiprows=1)
except ValueError as error:
    print("Error:", error)

# genfromtxt convierte la celda N/D en np.nan
datos = np.genfromtxt(ruta, delimiter=",", skip_header=1)
web02 = datos[:, 2]
print(web02[8:11])
print(web02.mean())
print(round(np.nanmean(web02), 1))

# Filtrar los valores ausentes con una máscara
validos = ~np.isnan(web02)
print(validos[8:11])
print(round(web02[validos].mean(), 1))
