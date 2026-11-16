"""Herencia, super() y polimorfismo (Tema 7)."""


class Equipo:
    def __init__(self, nombre, direccion_ip):
        self.nombre = nombre
        self.direccion_ip = direccion_ip

    def describir(self):
        return f"{self.nombre} ({self.direccion_ip})"


class Servidor(Equipo):
    def __init__(self, nombre, direccion_ip):
        super().__init__(nombre, direccion_ip)
        self.servicios = ["ssh"]

    def describir(self):
        return (f"{super().describir()}, "
                f"servicios: {len(self.servicios)}")


equipos = [Equipo("router01", "10.0.0.1"),
           Servidor("srv01", "10.0.0.10")]
for equipo in equipos:
    print(equipo.describir())
print(isinstance(equipos[1], Equipo), isinstance(equipos[0], Servidor))
