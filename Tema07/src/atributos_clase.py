"""Atributos de clase, atributos de instancia y lista compartida."""


class Equipo:
    total = 0

    def __init__(self, nombre):
        self.nombre = nombre
        Equipo.total += 1


router = Equipo("router01")
switch = Equipo("switch01")
print(Equipo.total, router.total)
switch.total = 10
print(Equipo.total, switch.total)


class Servidor:
    servicios = []

    def __init__(self, nombre):
        self.nombre = nombre

    def agregar_servicio(self, servicio):
        self.servicios.append(servicio)


web = Servidor("web01")
db = Servidor("db01")
web.agregar_servicio("ssh")
print(db.servicios)
