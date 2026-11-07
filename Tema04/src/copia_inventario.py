"""Copia de seguridad de un inventario (Tema 4).
Debe modificar la copia sin alterar el inventario original.
"""
inventario = [
    {"codigo": "SRV01", "uds": 4},
    {"codigo": "SW01", "uds": 7},
]
respaldo = inventario.copy()
respaldo[0]["uds"] = 0
print("Original:", inventario[0]["uds"])
print("Copia:", respaldo[0]["uds"])
