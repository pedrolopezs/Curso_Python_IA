# Bucle for para vectorizar con la IA local (Tema 9)
import pandas as pd

inventario = pd.DataFrame({"precio": [2450.0, 1890.0, 1320.9]})
con_iva = []
for precio in inventario["precio"]:
    con_iva.append(round(precio * 1.21, 1))
print(con_iva)
