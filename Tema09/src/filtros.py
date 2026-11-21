# Filtros con máscaras booleanas (Tema 9)
import pandas as pd

activos = pd.read_csv("Tema09/datos/activos.csv")

# Condición simple
mascara = activos["precio"] > 4000
print(mascara.sum())
print(activos[mascara][["codigo", "equipo", "precio"]])

# Condiciones compuestas: & (y), | (o), ~ (no), cada una entre paréntesis
en_madrid = (activos["ubicacion"] == "Madrid") & (activos["estado"] == "Activo")
print(activos[en_madrid]["codigo"].tolist())

# isin() y str.contains()
print(activos[activos["fabricante"].isin(["Dell", "HP"])][["codigo", "fabricante"]])
print(activos[activos["equipo"].str.contains("Portátil")][["codigo", "equipo"]])
