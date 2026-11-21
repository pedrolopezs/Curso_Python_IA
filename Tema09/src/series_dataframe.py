# Series y DataFrame (Tema 9)
import pandas as pd

# Una Series es una columna con etiquetas
precios = pd.Series([2450.0, 1890.0, 1320.9], name="precio")
print(precios)
print(precios.dtype)
print(precios.mean())

# Un DataFrame reúne varias columnas con nombre y tipos distintos
equipos = pd.DataFrame({
    "codigo": ["A001", "A003", "A005"],
    "equipo": ["Servidor web", "Switch planta 1", "Portátil dirección"],
    "precio": [2450.0, 1890.0, 1320.9],
})
print(equipos)
print(equipos.shape)
print(list(equipos.columns))
print(equipos.dtypes)
