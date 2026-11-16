"""Representación y comparación de objetos (Tema 7)."""


class Equipo:
    def __init__(self, nombre, direccion_ip):
        self.nombre = nombre
        self.direccion_ip = direccion_ip


router = Equipo("router01", "10.0.0.1")
copia = Equipo("router01", "10.0.0.1")
otro = Equipo("switch01", "10.0.0.2")
print(router)
print(router == copia, router == otro)
