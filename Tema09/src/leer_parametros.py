# Parámetros de read_csv() y to_csv() (Tema 9)
import pandas as pd

# El fichero lo ha guardado Excel: separador ;, coma decimal y cp1252
inventario = pd.read_csv(
    "Tema09/datos/inventario_excel.csv",
    sep=";",
    decimal=",",
    encoding="cp1252",
)
print(inventario)
print(inventario.dtypes)

# Guardamos sin y con el índice, y leemos los dos ficheros
inventario.to_csv("Tema09/inventario_utf8.csv", index=False)
inventario.to_csv("Tema09/inventario_indice.csv")
sin_indice = pd.read_csv("Tema09/inventario_utf8.csv")
con_indice = pd.read_csv("Tema09/inventario_indice.csv")
print(sin_indice.head(3))
print(con_indice.head(3))
