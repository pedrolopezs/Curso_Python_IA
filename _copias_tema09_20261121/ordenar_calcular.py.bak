# Ordenar y crear columnas (Tema 9)
import numpy as np
import pandas as pd

activos = pd.read_csv("Tema09/datos/activos.csv")

# Ordenar por una columna y por varias
mas_caros = activos.sort_values("precio", ascending=False)
print(mas_caros[["codigo", "equipo", "precio"]].head(3))
orden = activos.sort_values(["ubicacion", "precio"], ascending=[True, False])
print(orden[["codigo", "ubicacion", "precio"]].head(5))

# Columna calculada, sin bucles
activos["precio_iva"] = (activos["precio"] * 1.21).round(2)
print(activos[["codigo", "precio", "precio_iva"]].head(3))

# Columna con una condición
activos["gama"] = np.where(activos["precio"] >= 2000, "Alta", "Estándar")
print(activos["gama"].value_counts())
