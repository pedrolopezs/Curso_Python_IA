"""Tipos, conversiones e identidad de objetos (Tema 3).

Muestra el tipo de los valores básicos, convierte entre tipos y compara
valores e identidades.
"""

# Variables de los cinco tipos básicos
equipo = "Portátil"
unidades = 12
precio = 549.90
en_garantia = True
asignado_a = None

print(equipo, type(equipo))
print(unidades, type(unidades))
print(precio, type(precio))
print(en_garantia, type(en_garantia))
print(asignado_a, type(asignado_a))

# Conversiones entre tipos
print(int("12") + 1)
print(int(3.9))
print(str(12) + " equipos")
print(bool(""), bool("TI"))
print(0.1 + 0.2, round(0.1 + 0.2, 2))

# Igualdad frente a identidad
marca = "hp".upper()
fabricante = "HP"
print(marca == fabricante)
print(marca is fabricante)
print(asignado_a is None)
