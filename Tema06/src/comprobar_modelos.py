# Comprueba modelos_ollama.py (Tema 6)
import os
import subprocess
import sys

script = os.path.join(os.path.dirname(__file__), "modelos_ollama.py")
resultado = subprocess.run(
    [sys.executable, script], capture_output=True, text=True
)
salida = resultado.stdout
for esperado in ["qwen2.5-coder:3b", "GB"]:
    estado = "OK" if esperado in salida else "ERROR"
    print(estado, "debe aparecer", esperado)
