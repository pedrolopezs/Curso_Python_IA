"""Códigos de estado y errores de red con requests (Tema 6)."""
import requests


def listar_modelos(url):
    try:
        respuesta = requests.get(url, timeout=5)
        respuesta.raise_for_status()
    except requests.HTTPError as error:
        print("Error HTTP:", error)
        return []
    except requests.RequestException as error:
        print("No se puede conectar:", type(error).__name__)
        return []
    return respuesta.json()["models"]


base = "http://127.0.0.1:11434"
print(len(listar_modelos(base + "/api/tags")))
print(listar_modelos(base + "/api/noexiste"))
