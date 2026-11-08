# Comprueba registrar_eventos.py (Tema 5)
import os
import subprocess
import sys

script = os.path.join(os.path.dirname(__file__), "registrar_eventos.py")
esperado = ["Primero: ['arranque']", "Segundo: ['fallo']"]
resultado = subprocess.run(
    [sys.executable, script], capture_output=True, text=True
)
obtenido = resultado.stdout.strip().splitlines()
for linea_esperada, linea in zip(esperado, obtenido):
    estado = "OK" if linea == linea_esperada else "ERROR"
    print(estado, "esperado", linea_esperada, "obtenido", linea)
