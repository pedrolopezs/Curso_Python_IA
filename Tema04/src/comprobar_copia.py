# Comprueba copia_inventario.py (Tema 4)
import os
import subprocess
import sys

script = os.path.join(os.path.dirname(__file__), "copia_inventario.py")
esperado = ["Original: 4", "Copia: 0"]
resultado = subprocess.run(
    [sys.executable, script], capture_output=True, text=True
)
obtenido = resultado.stdout.strip().splitlines()
for linea_esperada, linea in zip(esperado, obtenido):
    estado = "OK" if linea == linea_esperada else "ERROR"
    print(estado, "esperado", linea_esperada, "obtenido", linea)
