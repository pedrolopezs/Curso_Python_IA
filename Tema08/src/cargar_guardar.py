"""Cargar y guardar datos numéricos con NumPy (Tema 8)."""
import numpy as np

# Cargar el fichero, sin la fila de cabecera
datos = np.loadtxt("Tema08/datos/latencias.csv", delimiter=",",
                   skiprows=1)
print(datos.shape)
print(datos[0])

# Separar la hora de las latencias de los servidores
horas = datos[:, 0]
latencias = datos[:, 1:]
print(horas[:5])
print(latencias.shape)

# Media de cada servidor y guardado en un fichero
medias = latencias.mean(axis=0)
print(medias.round(1))
np.savetxt("Tema08/medias.csv", medias, fmt="%.1f")
