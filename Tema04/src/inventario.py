"""Inventario como lista de diccionarios (Tema 4)."""
inventario = [
    {"codigo": "SRV01", "tipo": "Servidor", "unidades": 4},
    {"codigo": "SW01", "tipo": "Switch", "unidades": 7},
    {"codigo": "SW02", "tipo": "Switch", "unidades": 0},
    {"codigo": "PC01", "tipo": "Portátil", "unidades": 12},
    {"codigo": "RT01", "tipo": "Router", "unidades": 3},
]

# Recorrido con acceso a las claves
for equipo in inventario:
    print(f"{equipo['codigo']:<6} {equipo['tipo']:<10} {equipo['unidades']:>3}")

# Total de unidades
total = 0
for equipo in inventario:
    total += equipo["unidades"]
print("Total de unidades:", total)

# Códigos con menos de 5 unidades
bajos = []
for equipo in inventario:
    if equipo["unidades"] < 5:
        bajos.append(equipo["codigo"])
print("Stock bajo:", bajos)

# Tipos distintos
tipos = set()
for equipo in inventario:
    tipos.add(equipo["tipo"])
print(sorted(tipos))

# Códigos agrupados por tipo
grupos = {}
for equipo in inventario:
    tipo = equipo["tipo"]
    if tipo not in grupos:
        grupos[tipo] = []
    grupos[tipo].append(equipo["codigo"])
for tipo, codigos in grupos.items():
    print(tipo, codigos)
