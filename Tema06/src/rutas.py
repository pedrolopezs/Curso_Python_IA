"""Rutas, directorios y variables de entorno con os y pathlib (Tema 6)."""
import os
from pathlib import Path

print(os.getcwd())
ruta = os.path.join("Tema06", "datos", "accesos.log")
print(ruta)
print(os.path.exists(ruta), os.path.isdir(ruta))
print(os.path.basename(ruta), os.path.dirname(ruta))
print(sorted(os.listdir("Tema06/datos")))
os.makedirs("Tema06/informes", exist_ok=True)

# Variables de entorno
print(os.getenv("HOME"))
print(os.getenv("NO_EXISTE"))
print(os.getenv("NO_EXISTE", "valor"))

# pathlib: una alternativa a os para las rutas
ruta = Path("Tema06") / "datos" / "accesos.log"
texto = ruta.read_text(encoding="utf-8")
print(texto.splitlines()[0])
print(ruta.exists(), ruta.name)
print(ruta.parent)
