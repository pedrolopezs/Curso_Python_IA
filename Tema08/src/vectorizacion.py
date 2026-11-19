"""Operaciones vectorizadas y broadcasting (Tema 8)."""
import numpy as np

# Un bucle for frente a una operación vectorizada
lista_web = [12.4, 14.1, 18.7]
lista_db = [8.1, 9.0, 11.5]
diferencias = []
for posicion in range(len(lista_web)):
    diferencias.append(round(lista_web[posicion] - lista_db[posicion], 1))
print(diferencias)

web = np.array(lista_web)
db = np.array(lista_db)
print(np.round(web - db, 1))
print(np.round(web / db, 2))

# Broadcasting con un escalar, una fila y una columna
m = np.array([[12.4, 8.1, 15.2],
              [14.1, 9.0, 16.8]])
print(m[0] / 1000)
objetivo = np.array([10.0, 8.0, 12.0])
print(m - objetivo)
retardo = np.array([[0.5], [1.0]])
print(m + retardo)
