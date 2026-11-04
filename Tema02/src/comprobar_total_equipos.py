# Comprueba la función total_equipos generada por la IA (Tema 2)
from total_equipos import total_equipos

pruebas = [
    ([3, 5, 4], 12),
    ([], 0),
    ([7], 7),
]

for entrada, esperado in pruebas:
    obtenido = total_equipos(entrada)
    estado = "OK" if obtenido == esperado else "ERROR"
    print(estado, entrada, "esperado", esperado, "obtenido", obtenido)
