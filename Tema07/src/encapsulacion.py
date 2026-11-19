"""Encapsulación con uno y con dos guiones bajos (Tema 7)."""


class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self._estado = "activo"
        self.__clave = "abc123"

    def cambiar_estado(self, estado):
        if estado not in ("activo", "apagado"):
            raise ValueError(f"Estado no válido: {estado}")
        self._estado = estado

    def describir(self):
        return f"{self.nombre}: {self._estado}"

    def comprobar_clave(self, clave):
        return clave == self.__clave


router = Equipo("router01")
router.cambiar_estado("apagado")
print(router.describir())
try:
    router.cambiar_estado("roto")
except ValueError as error:
    print(error)
router._estado = "roto"
print(router.describir())
print(router.comprobar_clave("abc123"))
try:
    print(router.__clave)
except AttributeError as error:
    print(error)
print(router._Equipo__clave)
