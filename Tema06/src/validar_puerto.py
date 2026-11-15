"""Validación de un puerto escrito por el usuario (Tema 6)."""

while True:
    texto = input("Puerto: ")
    try:
        puerto = int(texto)
    except ValueError:
        print("Debe ser un número entero")
        continue
    if 1 <= puerto <= 65535:
        break
    print("El puerto debe estar entre 1 y 65535")
print("Puerto elegido:", puerto)
