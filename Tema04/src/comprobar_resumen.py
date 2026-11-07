# Comprueba resumen_tipos.py (Tema 4)
import os
import subprocess
import sys

script = os.path.join(os.path.dirname(__file__), "resumen_tipos.py")
esperado = ["PC: 12", "Router: 0", "Switch: 10"]
resultado = subprocess.run(
    [sys.executable, script], capture_output=True, text=True
)
obtenido = resultado.stdout.strip().splitlines()
print("Líneas esperadas:", len(esperado), "obtenidas:", len(obtenido))
for linea_esperada, linea in zip(esperado, obtenido):
    estado = "OK" if linea == linea_esperada else "ERROR"
    print(estado, "esperado", linea_esperada, "obtenido", linea)
