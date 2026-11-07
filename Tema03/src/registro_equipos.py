"""Registro de equipos del almacén (Tema 3).

Pide los datos de tres equipos y clasifica su stock.
"""

total = 0
for numero in range(1, 4):
    equipo = input(f"Equipo {numero}: ").strip().upper()
    unidades = int(input("Unidades: "))
    total += unidades
    # el umbral de stock bajo es 10 unidades
    if unidades == 0:
        estado = "sin existencias"
    elif unidades < 10:
        estado = "stock bajo"
    else:
        estado = "stock correcto"
    print(f"{equipo}: {unidades} unidades ({estado})")
print(f"Total de unidades: {total}")
