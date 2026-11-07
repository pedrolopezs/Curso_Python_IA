"""Tuplas y desempaquetado (Tema 4)."""
lugar = ("Sala 2", "Armario B", 4)
print(lugar[0], lugar[-1], len(lugar))
print(lugar[:2])

# Desempaquetado
sala, armario, balda = lugar
print(f"{sala} / {armario} / balda {balda}")
primero, *resto = [12, 7, 25]
print(primero, resto)

# Intercambio de valores
a, b = 1, 2
a, b = b, a
print(a, b)

# Tupla de un solo ítem
un_item = ("SRV01",)
print(type(un_item), type(("SRV01")))

# enumerate() entrega tuplas
for par in enumerate(["PC", "AP"], start=1):
    print(par)
