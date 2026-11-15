"""Traceback de una excepción no tratada (Tema 6)."""


def calcular_media(peticiones, minutos):
    return peticiones / minutos


def mostrar_media(peticiones, minutos):
    media = calcular_media(peticiones, minutos)
    print(f"{media} peticiones por minuto")


mostrar_media(1200, 60)
mostrar_media(900, 0)
