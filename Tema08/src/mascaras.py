"""Máscaras booleanas, condiciones compuestas y np.where (Tema 8)."""
import numpy as np

latencias = np.array([12.4, 14.1, 18.7, 21.3, 35.8, 29.4])

# Una máscara filtra sin bucles
mascara = latencias > 20
print(mascara)
print(latencias[mascara])
print(mascara.sum())

# Condiciones compuestas, con cada condición entre paréntesis
print(latencias[(latencias > 15) & (latencias < 30)])
print(latencias[(latencias < 13) | (latencias > 30)])
print(latencias[~(latencias > 20)])

# np.where elige entre dos valores según la condición
print(np.where(latencias > 20, "alta", "normal"))
print(np.where(latencias > 20, 20.0, latencias))

# Una máscara también modifica los valores que la cumplen
latencias[latencias > 30] = 30.0
print(latencias)
