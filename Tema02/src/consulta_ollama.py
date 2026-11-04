# Consulta a Ollama desde Python mediante su API (Tema 2)
import json
import sys
import urllib.request

modelo = "asistente-python"
prompt = "Explica en una frase qué es una variable en Python."
if len(sys.argv) > 1:
    prompt = " ".join(sys.argv[1:])

datos = {"model": modelo, "prompt": prompt, "stream": False}
peticion = urllib.request.Request(
    "http://127.0.0.1:11434/api/generate",
    data=json.dumps(datos).encode("utf-8"),
    headers={"Content-Type": "application/json"},
)

with urllib.request.urlopen(peticion) as respuesta:
    resultado = json.load(respuesta)

print(resultado["response"])
tokens = resultado["eval_count"]
segundos = resultado["eval_duration"] / 1e9
print(f"\n{tokens} tokens en {segundos:.1f} s")
