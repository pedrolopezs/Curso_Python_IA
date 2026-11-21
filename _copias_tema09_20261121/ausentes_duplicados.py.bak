# Valores ausentes y duplicados (Tema 9)
import pandas as pd

sucio = pd.read_csv("Tema09/datos/activos_sucio.csv")
print(sucio.shape)

# Ausentes: cuántos hay por columna y en qué filas
print(sucio.isna().sum())
print(sucio[sucio["ubicacion"].isna()][["codigo", "equipo", "ubicacion"]])

# fillna() y dropna() devuelven un resultado nuevo
sucio["ubicacion"] = sucio["ubicacion"].fillna("Sin asignar")
print(sucio["ubicacion"].value_counts())

# Duplicados: filas repetidas por completo
print(sucio.duplicated().sum())
print(sucio[sucio.duplicated()]["codigo"].tolist())
sucio = sucio.drop_duplicates()
print(sucio.shape)
