# Comprueba optimizar_inventario.py (Tema 7)
import os
import subprocess
import sys

script = os.path.join(os.path.dirname(__file__), "optimizar_inventario.py")
resultado = subprocess.run(
    [sys.executable, script], capture_output=True, text=True
)
salida = resultado.stdout
for esperado in ["10.0.0.2", "None"]:
    estado = "OK" if esperado in salida else "ERROR"
    print(estado, "debe aparecer", esperado)
estado = "OK" if "Traceback" not in resultado.stderr else "ERROR"
print(estado, "no debe aparecer un traceback")
