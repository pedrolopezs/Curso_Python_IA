# Agregaciones y groupby (Tema 9)
import pandas as pd

activos = pd.read_csv("Tema09/datos/activos.csv")

# Resumen de una columna
precio = activos["precio"]
print(precio.sum(), precio.mean().round(2), precio.min(), precio.max())

# Una fila de resultados por cada grupo
print(activos.groupby("ubicacion")["precio"].mean().round(2))
print(activos.groupby("estado")["precio"].agg(["count", "sum"]))

# reset_index() devuelve el resultado como un DataFrame normal
por_fabricante = activos.groupby("fabricante")["precio"].sum().reset_index()
print(por_fabricante.sort_values("precio", ascending=False).head(3))
