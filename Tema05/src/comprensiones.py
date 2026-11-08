"""Comprensiones de listas, diccionarios, conjuntos y generadoras (Tema 5)."""

latencias = [23, 145, 12, 230, 67]

# Lista con transformación
segundos = [latencia / 1000 for latencia in latencias]
print(segundos)

# Lista con filtro
lentas = [latencia for latencia in latencias if latencia > 100]
print(lentas)

# Expresión condicional: un valor distinto según la condición
estados = ["lenta" if latencia > 100 else "normal" for latencia in latencias]
print(estados)

# Diccionario a partir de un diccionario, con filtro
servicios = {"ssh": 22, "http": 80, "mysql": 3306}
reservados = {nombre: puerto for nombre, puerto in servicios.items()
              if puerto < 1024}
print(reservados)

# Conjunto: los duplicados desaparecen
direcciones = ["10.0.0.5", "10.0.0.7", "10.0.0.5"]
unicas = {direccion for direccion in direcciones}
print(sorted(unicas))

# Expresión generadora: un único resultado sin crear una lista intermedia
total_ms = sum(latencia for latencia in latencias)
print(total_ms)

# Una expresión generadora se recorre una sola vez
rapidas = (latencia for latencia in latencias if latencia < 50)
print(list(rapidas))
print(list(rapidas))
