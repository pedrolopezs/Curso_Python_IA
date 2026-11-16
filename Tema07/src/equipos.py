"""Módulo propio con la clase Equipo (Tema 7)."""


class Equipo:
    def __init__(self, nombre, direccion_ip):
        self.nombre = nombre
        self.direccion_ip = direccion_ip

    def describir(self):
        return f"{self.nombre} ({self.direccion_ip})"


if __name__ == "__main__":
    print(Equipo("prueba", "10.0.0.99").describir())
