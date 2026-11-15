"""Lanzar excepciones con raise (Tema 6)."""


def validar_puerto(puerto):
    if not 1 <= puerto <= 65535:
        raise ValueError(f"Puerto fuera de rango: {puerto}")
    return puerto


# La función lanza la excepción y el código que la llama la trata
try:
    validar_puerto(70000)
except ValueError as error:
    print("Error:", error)

print(validar_puerto(443))

# Un raise sin argumentos vuelve a lanzar la misma excepción
try:
    validar_puerto(-1)
except ValueError:
    print("Registrando el fallo")
    raise
