"""Índices y slicing de cadenas (Tema 4)."""
codigo = "SRV-01-A"

# Índices positivos y negativos
print(codigo[0])
print(codigo[-1])
print(len(codigo))

# Slicing [inicio:fin:salto]
print(codigo[0:3])
print(codigo[4:6])
print(codigo[:3])
print(codigo[4:])
print(codigo[-1:])

# Salto e inversión
print(codigo[::2])
print(codigo[::-1])

# Una cadena nueva a partir de fragmentos de la original
nuevo = "XRV" + codigo[3:]
print(nuevo)
