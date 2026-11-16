"""Inventario con búsqueda lineal (Tema 7)."""


class Equipo:
    def __init__(self, nombre, direccion_ip):
        self.nombre = nombre
        self.direccion_ip = direccion_ip


class Inventario:
    def __init__(self):
        self.equipos = []

    def agregar(self, equipo):
        self.equipos.append(equipo)

    def buscar(self, nombre):
        for equipo in self.equipos:
            if equipo.nombre == nombre:
                return equipo
        return None


inventario = Inventario()
inventario.agregar(Equipo("router01", "10.0.0.1"))
inventario.agregar(Equipo("switch01", "10.0.0.2"))
print(inventario.buscar("switch01").direccion_ip)
print(inventario.buscar("nas01"))
