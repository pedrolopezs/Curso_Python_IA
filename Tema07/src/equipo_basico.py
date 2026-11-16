"""Primera clase: Equipo con __init__() y atributos (Tema 7)."""


class Equipo:
    def __init__(self, nombre, direccion_ip):
        self.nombre = nombre
        self.direccion_ip = direccion_ip


router = Equipo("router01", "10.0.0.1")
switch = Equipo("switch01", "10.0.0.2")
print(router.nombre, router.direccion_ip)
switch.direccion_ip = "10.0.0.20"
print(router.direccion_ip, switch.direccion_ip)
