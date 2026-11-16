# Comprueba revisar_servidores.py (Tema 7)
import os
import subprocess
import sys

script = os.path.join(os.path.dirname(__file__), "revisar_servidores.py")
resultado = subprocess.run(
    [sys.executable, script], capture_output=True, text=True
)
salida = resultado.stdout
for esperado in ["['ssh']", "['http']"]:
    estado = "OK" if esperado in salida else "ERROR"
    print(estado, "debe aparecer", esperado)
estado = "OK" if "['ssh', 'http']" not in salida else "ERROR"
print(estado, "no debe aparecer ['ssh', 'http']")
