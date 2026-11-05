"""Estado del stock de un equipo (Tema 3).

Clasifica las unidades en sin existencias, stock bajo o stock correcto y
decide si el equipo se puede prestar.
"""

unidades = int(input("Unidades: "))
garantia = input("¿En garantía? (s/n): ").strip().lower() == "s"

if unidades == 0:
    estado = "Sin existencias"
elif unidades < 10:
    estado = "Stock bajo"
else:
    estado = "Stock correcto"
print("Estado:", estado)

# condición compuesta con and
if unidades > 0 and garantia:
    print("Se puede prestar")
else:
    print("No se puede prestar")
