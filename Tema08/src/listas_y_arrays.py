"""Listas frente a arrays de NumPy (Tema 8)."""
import numpy as np

latencias_lista = [12.4, 14.1, 18.7, 21.3]

# Media con un bucle for y con NumPy
suma = 0
for latencia in latencias_lista:
    suma = suma + latencia
print(suma / len(latencias_lista))
latencias = np.array(latencias_lista)
print(latencias.mean())

# El operador * se comporta de forma distinta
print(latencias_lista * 2)
print(latencias * 2)

# Tipo del array y tipo común de sus elementos
print(type(latencias), latencias.dtype)
mezcla = np.array([1, 2.5, 3])
print(mezcla, mezcla.dtype)
