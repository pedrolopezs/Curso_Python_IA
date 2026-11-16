# Clase Equipo sin documentar (Tema 7).


class Equipo:
    def __init__(self, nombre, direccion_ip):
        self.nombre = nombre
        self.direccion_ip = direccion_ip

    def describir(self):
        return f"{self.nombre} ({self.direccion_ip})"


print(Equipo("router01", "10.0.0.1").describir())
