# Selección con [], loc e iloc (Tema 9)
import pandas as pd

activos = pd.read_csv("Tema09/datos/activos.csv")

# Columnas
print(activos["precio"].head(3))
print(activos[["codigo", "precio"]].head(3))

# loc usa etiquetas e incluye el final; iloc usa posiciones y no lo incluye
print(activos.loc[2, "equipo"])
print(activos.loc[0:2, ["codigo", "equipo"]])
print(activos.iloc[0:2, 0:2])

# Con set_index() el código pasa a ser la etiqueta de cada fila
indexado = activos.set_index("codigo")
print(indexado.loc["A005", "equipo"])
print(indexado.loc["A001":"A003", "precio"])
