"""Encapsulación por convención con un guion bajo (Tema 7)."""


class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self._estado = "activo"

    def cambiar_estado(self, estado):
        if estado not in ("activo", "apagado"):
            raise ValueError(f"Estado no válido: {estado}")
        self._estado = estado

    def describir(self):
        return f"{self.nombre}: {self._estado}"


router = Equipo("router01")
router.cambiar_estado("apagado")
print(router.describir())
try:
    router.cambiar_estado("roto")
except ValueError as error:
    print(error)
router._estado = "roto"
print(router.describir())
