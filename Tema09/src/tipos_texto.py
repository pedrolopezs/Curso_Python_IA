# Tipos y texto (Tema 9)
import pandas as pd

sucio = pd.read_csv("Tema09/datos/activos_sucio.csv")

# Texto: quitar espacios y unificar mayúsculas
print(sucio["fabricante"].value_counts().head(4))
sucio["fabricante"] = sucio["fabricante"].str.strip().str.lower()
sucio["estado"] = sucio["estado"].str.strip().str.lower()
print(sucio["fabricante"].value_counts().head(4))
print(sucio["estado"].value_counts())

# Tipos: precio es texto porque contiene 1.6k y N/D
print(sucio["precio"].dtype)
sucio["precio_num"] = pd.to_numeric(sucio["precio"], errors="coerce")
print(sucio["precio_num"].dtype)
print(sucio[sucio["precio_num"].isna()][["codigo", "precio", "precio_num"]])
