"""Diccionarios: acceso, modificación y recorrido (Tema 4)."""
equipo = {"codigo": "SRV01", "tipo": "Servidor", "uds": 4}
print(equipo["tipo"], len(equipo))
print(equipo.get("precio"), equipo.get("precio", 0))
print("codigo" in equipo, "SRV01" in equipo)

# Agregar, modificar y eliminar
equipo["garantia"] = True
equipo["uds"] = 6
print(equipo)
equipo.update({"ubicacion": "Sala 2"})
print(equipo["ubicacion"])
eliminado = equipo.pop("garantia")
del equipo["ubicacion"]
print(eliminado, equipo)

# Recorrido
for clave, valor in equipo.items():
    print(f"{clave}: {valor}")
print(list(equipo.keys()))
print(list(equipo.values()))

# Contador con get()
tipos = ["Switch", "PC", "Switch", "Router", "Switch", "PC"]
cuenta = {}
for tipo in tipos:
    cuenta[tipo] = cuenta.get(tipo, 0) + 1
print(cuenta)
