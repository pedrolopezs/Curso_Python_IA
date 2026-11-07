"""Igualdad, identidad, alias y copias (Tema 4)."""
import copy

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b, a is b)

# Alias: dos nombres para la misma lista
c = a
c.append(4)
print(a, c, a is c)

# Copia superficial
d = a.copy()
d.append(5)
print(a, d, a is d)

# La copia superficial comparte los objetos internos
inventario = [["PC", 12], ["Switch", 7]]
copia = inventario.copy()
copia[0][1] = 0
print(inventario)

# Copia profunda
profunda = copy.deepcopy(inventario)
profunda[0][1] = 99
print(inventario, profunda)
