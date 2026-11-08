# Comprueba contar_niveles.py (Tema 5)
import os
import subprocess
import sys

script = os.path.join(os.path.dirname(__file__), "contar_niveles.py")
resultado = subprocess.run(
    [sys.executable, script], capture_output=True, text=True
)
salida = resultado.stdout
for esperado in ["ERROR: 1", "INFO: 2", "WARNING: 1"]:
    estado = "OK" if esperado in salida else "ERROR"
    print(estado, "debe aparecer", esperado)
