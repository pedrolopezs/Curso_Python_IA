# Copias y asignaciones (Tema 9)
import pandas as pd

activos = pd.read_csv("Tema09/datos/activos.csv")

# Un subconjunto es una copia: modificarlo no cambia el original
caros = activos[activos["precio"] > 4000]
caros["estado"] = "Revisar"
print(caros[["codigo", "estado"]])
print(activos.loc[[1, 7, 15, 16], ["codigo", "estado"]])

# Para modificar el original se asigna con loc, en un solo paso
retirados = activos["estado"] == "Retirado"
activos.loc[retirados, "estado"] = "Baja"
print(activos["estado"].value_counts())
