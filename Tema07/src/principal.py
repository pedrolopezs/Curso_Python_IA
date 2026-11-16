"""Script que importa la clase Equipo del módulo equipos (Tema 7)."""
from equipos import Equipo

router = Equipo("router01", "10.0.0.1")
print(router.describir())
