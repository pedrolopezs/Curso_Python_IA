"""Clasifica el stock de un equipo (Tema 3).

Con 10 unidades o más el stock es correcto, y con menos de 10 es bajo.
"""

unidades = int(input())

if unidades == 0:
    print("Sin existencias")
elif unidades <= 10:
    print("Stock bajo")
else:
    print("Stock correcto")
