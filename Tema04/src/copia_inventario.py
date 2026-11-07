"""Copia de seguridad de un inventario (Tema 4).
Debe modificar la copia sin alterar el inventario original.
"""
inventario = [
    {"codigo": "SRV01", "unidades": 4},
    {"codigo": "SW01", "unidades": 7},
]
respaldo = inventario.copy()
respaldo[0]["unidades"] = 0
print("Original:", inventario[0]["unidades"])
print("Copia:", respaldo[0]["unidades"])
