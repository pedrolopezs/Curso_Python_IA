"""Métodos, self y cambio de estado (Tema 7)."""


class Equipo:
    def __init__(self, nombre, direccion_ip, estado="activo"):
        self.nombre = nombre
        self.direccion_ip = direccion_ip
        self.estado = estado

    def describir(self):
        return (f"{self.nombre} ({self.direccion_ip}): "
                f"{self.estado}")

    def apagar(self):
        self.estado = "apagado"


router = Equipo("router01", "10.0.0.1")
print(router.describir())
router.apagar()
print(router.describir())
