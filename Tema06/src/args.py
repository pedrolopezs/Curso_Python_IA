"""Argumentos de la línea de comandos con el módulo sys (Tema 6)."""
import sys

print(sys.argv)
# Sin argumento, sys.argv[1] provoca IndexError
try:
    ruta = sys.argv[1]
except IndexError:
    print("Uso: python args.py RUTA", file=sys.stderr)
    sys.exit(1)
print("Fichero:", ruta)
print("Sistema:", sys.platform)
print("Intérprete:", sys.executable)
