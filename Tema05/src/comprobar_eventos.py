# Comprueba registrar_eventos.py (Tema 5)
import os
import subprocess
import sys

script = os.path.join(os.path.dirname(__file__), "registrar_eventos.py")
resultado = subprocess.run(
    [sys.executable, script], capture_output=True, text=True
)
salida = resultado.stdout
if "['arranque', 'fallo']" in salida:
    print("ERROR el segundo evento incluye el primero")
elif "['fallo']" in salida:
    print("OK cada llamada devuelve solo su evento")
else:
    print("ERROR no aparece ['fallo'] en la salida")
