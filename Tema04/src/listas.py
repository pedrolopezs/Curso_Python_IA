"""Listas: acceso, métodos y orden (Tema 4)."""
equipos = ["Portátil", "Switch", "Router"]

# Acceso y slicing
print(equipos[0], equipos[-1])
print(equipos[1:])

# Agregar ítems
equipos.append("NAS")
equipos.insert(1, "Servidor")
equipos.extend(["SAI", "Firewall"])
print(equipos)

# Eliminar y buscar
equipos.remove("Switch")
ultimo = equipos.pop()
print(ultimo, equipos)
print(equipos.index("Router"), "NAS" in equipos)

# sorted() devuelve una lista nueva y sort() modifica la original
print(sorted(equipos))
print(equipos)
equipos.sort()
print(equipos)

# Los métodos que modifican la lista devuelven None
resultado = equipos.append("Hub")
print(resultado)

# Recorrido con enumerate
for pos, equipo in enumerate(equipos, start=1):
    print(pos, equipo)
