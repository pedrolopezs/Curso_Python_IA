"""Módulos de la biblioteca estándar y functools (Tema 6)."""
import math
from datetime import datetime
import statistics as estadistica
from functools import reduce

print(math.ceil(2.1))

fecha = datetime(2026, 11, 10, 9, 30)
print(fecha.strftime("%d/%m/%Y %H:%M"))

print(estadistica.mean([120, 150, 90]))

# reduce() combina los ítems de un iterable en un único valor
print(reduce(lambda total, valor: total + valor, [3, 4, 5]))
print(sum([3, 4, 5]))


def sumar_contadores(acumulado, parcial):
    for direccion, peticiones in parcial.items():
        acumulado[direccion] = (acumulado.get(direccion, 0)
                                + peticiones)
    return acumulado


# El tercer argumento de reduce() es el valor inicial del acumulado
lunes = {"10.0.0.5": 3, "10.0.0.7": 2}
martes = {"10.0.0.5": 1, "10.0.0.9": 4}
miercoles = {"10.0.0.7": 5}
semana = reduce(sumar_contadores, [lunes, martes, miercoles], {})
print(semana)
