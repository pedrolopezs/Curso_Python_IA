"""Consulta un modelo de Ollama con requests.post() (Tema 6)."""
import requests

url = "http://127.0.0.1:11434/api/generate"
datos = {"model": "asistente-python",
         "stream": False,
         "prompt": "Qué es una variable en una frase"}
respuesta = requests.post(url, json=datos, timeout=120)
print(respuesta.json()["response"])
