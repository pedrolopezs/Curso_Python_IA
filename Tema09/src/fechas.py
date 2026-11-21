# Fechas y rangos (Tema 9)
import pandas as pd

sucio = pd.read_csv("Tema09/datos/activos_sucio.csv")
sucio = sucio.drop_duplicates()
print(sucio["Fecha Compra"].dtype)

# errors="coerce" convierte las fechas imposibles en NaT
sucio["fecha"] = pd.to_datetime(sucio["Fecha Compra"], errors="coerce")
print(sucio["fecha"].dtype)
print(sucio[sucio["fecha"].isna()][["codigo", "Fecha Compra", "fecha"]])

# El accesor dt da el año, y las comparaciones filtran por rango
sucio["anio"] = sucio["fecha"].dt.year
print(sucio["anio"].value_counts().sort_index())
recientes = sucio[sucio["fecha"] >= "2023-01-01"]
print(recientes[["codigo", "fecha"]].head(5))
