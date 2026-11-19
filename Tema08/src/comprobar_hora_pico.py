# Comprueba hora_pico.py (Tema 8)
import os
import subprocess
import sys

script = os.path.join(os.path.dirname(__file__), "hora_pico.py")
if not os.path.exists(script):
    print("ERROR no existe Tema08/src/hora_pico.py, hay que crearlo")
    sys.exit()
resultado = subprocess.run(
    [sys.executable, script], capture_output=True, text=True
)
for esperado in ["12", "24.2"]:
    estado = "OK" if esperado in resultado.stdout else "ERROR"
    print(estado, "debe aparecer", esperado)
with open(script, encoding="utf-8") as fichero:
    codigo = fichero.read()
estado = "OK" if "import numpy" in codigo else "ERROR"
print(estado, "debe importar numpy")
estado = "OK" if "Traceback" not in resultado.stderr else "ERROR"
print(estado, "no debe aparecer un traceback")
