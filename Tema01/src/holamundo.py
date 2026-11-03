# Comprobación del entorno Python (Tema 1)
import os
import platform
import sys

print("Entorno Python operativo")
print("Usuario:", os.getenv("USER"))
print("Directorio actual:", os.getcwd())
print("Ejecutable:", sys.executable)
print("Version:", sys.version.split()[0])
print("Sistema:", platform.platform())
