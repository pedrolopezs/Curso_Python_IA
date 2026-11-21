# Cadena de métodos para explicar con la IA local (Tema 9)
import pandas as pd

inventario = pd.read_csv("Tema09/datos/activos.csv")
resultado = (
    inventario.groupby("fabricante")["precio"]
    .mean()
    .round(0)
    .sort_values(ascending=False)
    .head(3)
)
print(resultado)
