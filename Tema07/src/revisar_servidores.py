"""Servidores con servicios (Tema 7). Contiene un error a corregir."""


class Servidor:
    servicios = []

    def __init__(self, nombre):
        self.nombre = nombre

    def agregar_servicio(self, servicio):
        self.servicios.append(servicio)


web = Servidor("web01")
db = Servidor("db01")
web.agregar_servicio("ssh")
print(web.servicios)
db.agregar_servicio("http")
print(db.servicios)
