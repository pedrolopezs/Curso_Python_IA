# Comprueba limpiar_activos.py (Tema 9)
import os
import re
import subprocess
import sys

script = os.path.join(os.path.dirname(__file__), "limpiar_activos.py")
if not os.path.exists(script):
    print("ERROR no existe Tema09/src/limpiar_activos.py, hay que crearlo")
    sys.exit()
resultado = subprocess.run(
    [sys.executable, script], capture_output=True, text=True
)
for esperado in ["24", "1567.3"]:
    estado = "OK" if esperado in resultado.stdout else "ERROR"
    print(estado, "debe aparecer", esperado)
with open(script, encoding="utf-8") as fichero:
    codigo = fichero.read()
estado = "OK" if "import pandas" in codigo else "ERROR"
print(estado, "debe importar pandas")
limpia = re.search(r"\[.fabricante.\]\s*\.str\.strip", codigo)
estado = "OK" if limpia else "ERROR"
print(estado, "debe quitar espacios a los valores de fabricante")
estado = "OK" if ".str.lower()" in codigo else "ERROR"
print(estado, "debe pasar fabricante a minusculas")
estado = "OK" if "Traceback" not in resultado.stderr else "ERROR"
print(estado, "no debe aparecer un traceback")
