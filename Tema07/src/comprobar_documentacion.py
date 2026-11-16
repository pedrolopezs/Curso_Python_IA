# Comprueba documentar_equipo.py (Tema 7)
import os
import subprocess
import sys

script = os.path.join(os.path.dirname(__file__), "documentar_equipo.py")
resultado = subprocess.run(
    [sys.executable, script], capture_output=True, text=True
)
estado = "OK" if "router01 (10.0.0.1)" in resultado.stdout else "ERROR"
print(estado, "debe aparecer router01 (10.0.0.1)")
with open(script, encoding="utf-8") as fichero:
    codigo = fichero.read()
marcas = codigo.count('"""') + codigo.count("'''")
estado = "OK" if marcas >= 6 else "ERROR"
print(estado, "debe haber docstrings en la clase y en sus dos métodos")
estado = "OK" if "Traceback" not in resultado.stderr else "ERROR"
print(estado, "no debe aparecer un traceback")
