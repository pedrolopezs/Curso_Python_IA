"""Slice sobre una matriz de latencias, para explicar con la IA (Tema 8)."""
import numpy as np

# Una fila por hora, de la 8 a la 13, y una columna por servidor
latencias = np.array([[20.1, 9.7, 21.3],
                      [21.0, 12.1, 24.0],
                      [21.7, 11.9, 25.9],
                      [25.0, 15.5, 31.2],
                      [30.1, 17.4, 35.4],
                      [27.5, 15.1, 34.7]])
print(latencias[2:5, 1:])
