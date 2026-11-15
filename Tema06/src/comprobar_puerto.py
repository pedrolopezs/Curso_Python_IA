# Comprueba leer_puerto.py (Tema 6)
import os
import subprocess
import sys

script = os.path.join(os.path.dirname(__file__), "leer_puerto.py")
resultado = subprocess.run(
    [sys.executable, script], capture_output=True, text=True
)
salida = resultado.stdout
for esperado in ["Puerto no válido", "Fin del script"]:
    estado = "OK" if esperado in salida else "ERROR"
    print(estado, "debe aparecer", esperado)
estado = "OK" if "Traceback" not in resultado.stderr else "ERROR"
print(estado, "no debe aparecer un traceback")
