# Comprueba umbral_stock.py con valores límite (Tema 3)
import os
import subprocess
import sys

script = os.path.join(os.path.dirname(__file__), "umbral_stock.py")

pruebas = [
    (0, "Sin existencias"),
    (9, "Stock bajo"),
    (10, "Stock correcto"),
    (11, "Stock correcto"),
]

for unidades, esperado in pruebas:
    resultado = subprocess.run(
        [sys.executable, script],
        input=str(unidades),
        capture_output=True,
        text=True,
    )
    obtenido = resultado.stdout.strip()
    estado = "OK" if obtenido == esperado else "ERROR"
    print(estado, unidades, "esperado", esperado, "obtenido", obtenido)
