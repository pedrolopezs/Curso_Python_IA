"""Agregaciones, parámetro axis, orden y unión de arrays (Tema 8)."""
import numpy as np

# Agregaciones sobre un array de una dimensión
latencias = np.array([12.4, 14.1, 18.7, 21.3, 35.8, 29.4])
horas = np.arange(8, 14)
print(round(latencias.sum(), 1), latencias.mean())
print(latencias.min(), latencias.max())
print(round(latencias.std(), 2))
print(latencias.argmax(), horas[latencias.argmax()])

# El parámetro axis, con las horas en las filas y los servidores en las
# columnas
matriz = np.array([[12.4, 8.1, 15.2],
                   [14.1, 9.0, 16.8],
                   [18.7, 11.5, 22.4],
                   [21.3, 13.2, 25.1]])
print(matriz.mean(axis=0).round(1))
print(matriz.mean(axis=1).round(1))
print(matriz.max(axis=0))
print(matriz.argmax(axis=0))

# Ordenar y combinar
servidores = np.array(["web01", "db01", "app01"])
medias = np.array([16.6, 10.4, 19.9])
print(np.sort(medias)[::-1])
orden = np.argsort(medias)
print(orden, servidores[orden])
web = np.array([12.4, 14.1, 18.7])
db = np.array([8.1, 9.0, 11.5])
print(np.concatenate([web, db]))
