"""Lista los modelos de Ollama con la biblioteca requests (Tema 6)."""
import requests

# API de Ollama: esta máquina, puerto 11434
url = "http://127.0.0.1:11434/api/tags"
respuesta = requests.get(url, timeout=5)
print(respuesta.status_code, respuesta.ok)
datos = respuesta.json()
print(type(datos))
for modelo in datos["models"]:
    print(modelo["name"], round(modelo["size"] / 1e9, 1), "GB")
