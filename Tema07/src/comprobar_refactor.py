# Comprueba refactorizar_incidencia.py (Tema 7)
import os
import subprocess
import sys

script = os.path.join(os.path.dirname(__file__), "refactorizar_incidencia.py")
resultado = subprocess.run(
    [sys.executable, script], capture_output=True, text=True
)
estado = "OK" if "INC-001 srv-web01 (alta)" in resultado.stdout else "ERROR"
print(estado, "debe aparecer INC-001 srv-web01 (alta)")
with open(script, encoding="utf-8") as fichero:
    codigo = fichero.read()
estado = "OK" if "class Incidencia" in codigo else "ERROR"
print(estado, "debe definir la clase Incidencia")
estado = "OK" if "Traceback" not in resultado.stderr else "ERROR"
print(estado, "no debe aparecer un traceback")
