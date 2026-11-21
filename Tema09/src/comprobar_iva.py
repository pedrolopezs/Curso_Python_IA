# Comprueba iva_bucle.py (Tema 9)
import os
import subprocess
import sys

script = os.path.join(os.path.dirname(__file__), "iva_bucle.py")
resultado = subprocess.run(
    [sys.executable, script], capture_output=True, text=True
)
for esperado in ["2964.5", "2286.9", "1598.3"]:
    estado = "OK" if esperado in resultado.stdout else "ERROR"
    print(estado, "debe aparecer", esperado)
with open(script, encoding="utf-8") as fichero:
    lineas = fichero.read().splitlines()
codigo = "\n".join(lineas)
estado = "OK" if "import pandas" in codigo else "ERROR"
print(estado, "debe importar pandas")
hay_bucle = any(linea.strip().startswith("for ") for linea in lineas)
estado = "ERROR" if hay_bucle else "OK"
print(estado, "no debe haber un bucle for")
estado = "OK" if "Traceback" not in resultado.stderr else "ERROR"
print(estado, "no debe aparecer un traceback")
