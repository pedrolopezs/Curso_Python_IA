"""Indexación y slicing en una y en dos dimensiones (Tema 8)."""
import numpy as np

# Una dimensión
latencias = np.array([12.4, 14.1, 18.7, 21.3, 35.8, 29.4])
print(latencias[0], latencias[-1])
print(latencias[1:4])
print(latencias[::2])
print(latencias[::-1])

# Dos dimensiones, con una fila por hora y una columna por servidor
m = np.array([[12.4, 8.1, 15.2],
              [14.1, 9.0, 16.8],
              [18.7, 11.5, 22.4],
              [21.3, 13.2, 25.1]])
print(m[1, 2])
print(m[0])
print(m[:, 1])
print(m[1:, :2])

# Dos corchetes encadenados dan otro resultado
print(m[:][1])
