"""Vistas y copias de un array (Tema 8)."""
import numpy as np

latencias = np.array([12.4, 14.1, 18.7, 21.3, 35.8, 29.4])

# Un slice es una vista que comparte la memoria con el original
vista = latencias[1:4]
vista[0] = 99.0
print(latencias)
print(vista.base is latencias)

# Con copy() los datos son independientes
copia = latencias[1:4].copy()
copia[0] = 0.0
print(latencias)
print(copia)
