# Comprueba contar_niveles.py (Tema 5)
import os
import subprocess
import sys

script = os.path.join(os.path.dirname(__file__), "contar_niveles.py")
esperado = ["ERROR: 1", "INFO: 2", "WARNING: 1"]
resultado = subprocess.run(
    [sys.executable, script], capture_output=True, text=True
)
obtenido = resultado.stdout.strip().splitlines()
print("Líneas esperadas:", len(esperado), "obtenidas:", len(obtenido))
for linea_esperada, linea in zip(esperado, obtenido):
    estado = "OK" if linea == linea_esperada else "ERROR"
    print(estado, "esperado", linea_esperada, "obtenido", linea)
