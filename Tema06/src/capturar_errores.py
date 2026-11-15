"""Captura de excepciones con try, except, else y finally (Tema 6)."""

# Un try con un except de tipo concreto
texto = "80a"
try:
    puerto = int(texto)
    print("Puerto válido:", puerto)
except ValueError:
    print("El puerto debe ser un número")
print("El script continúa")

# Con as se guarda la excepción para mostrar su mensaje
try:
    puerto = int(texto)
except ValueError as error:
    print(error)

# Varios tipos de excepción agrupados en una tupla
for valor in ["22", None, "x"]:
    try:
        print(int(valor))
    except (ValueError, TypeError) as error:
        print(type(error).__name__)

# Un except sin tipo oculta el nombre mal escrito textoo
texto = "80"
try:
    puerto = int(textoo)
except:
    print("Puerto no válido")

# Los bloques else y finally
for texto in ["443", "https"]:
    try:
        puerto = int(texto)
    except ValueError:
        print(texto, "no es un puerto")
    else:
        print("Puerto", puerto, "correcto")
    finally:
        print("Revisado:", texto)
