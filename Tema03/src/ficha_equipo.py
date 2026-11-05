"""Ficha de un equipo del inventario (Tema 3).

Pide el nombre, las unidades y el precio de un equipo y muestra una ficha
con el valor total del stock.
"""

equipo = input("Equipo: ").strip().upper()
unidades = int(input("Unidades: "))
precio = float(input("Precio en euros: "))

total = unidades * precio

print("-" * 24)
print(f"Equipo:   {equipo}")
print(f"Unidades: {unidades:>8d}")
print(f"Precio:   {precio:>8,.2f} €")
print(f"Total:    {total:>8,.2f} €")
print("-" * 24)
