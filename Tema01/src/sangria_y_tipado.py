# Sangría y tipado en Python (Tema 1)

# Los bloques se delimitan con sangría de 4 espacios
equipos = 3
if equipos > 0:
    print("Hay equipos")
else:
    print("Sin equipos")

# Tipado dinámico: una variable puede cambiar de tipo
inventario = 12
print(type(inventario))
inventario = "doce"
print(type(inventario))

# Tipado fuerte: los tipos se convierten de forma explícita
print("Equipos: " + str(12))

# Para provocar el error, quita el # de la línea siguiente
# print("Equipos: " + 12)
