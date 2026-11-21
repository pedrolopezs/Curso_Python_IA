# Exploración de un DataFrame (Tema 9)
import pandas as pd

activos = pd.read_csv("Tema09/datos/activos.csv")
print(activos[["codigo", "equipo", "precio", "estado"]].head())
print(activos.shape)
activos.info()
print(activos["precio"].describe())
print(activos["estado"].value_counts())
print(activos["fabricante"].value_counts().head(3))
