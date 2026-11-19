"""Crear arrays, consultar sus atributos y cambiar su forma (Tema 8)."""
import numpy as np

# Funciones para crear arrays
print(np.array([12.4, 14.1, 18.7]))
print(np.zeros(3))
print(np.ones(3, dtype=int))
print(np.arange(8, 14))
print(np.arange(0, 10, 3))
print(np.linspace(0, 1, 5))

# Atributos de un array de dos dimensiones
latencias = np.array([[12.4, 8.1, 15.2],
                      [14.1, 9.0, 16.8]])
print(latencias.shape, latencias.ndim, latencias.size)
print(latencias.dtype)

# Conversión de tipo
print(latencias.astype(int))
print(np.round(latencias).astype(int))

# Cambio de forma y traspuesta
print(latencias.reshape(3, 2))
print(latencias.reshape(-1))
print(latencias.T)
