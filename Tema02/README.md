# Tema 2. IA local con Ollama

Ficheros de apoyo del laboratorio del Tema 2.

## Contenido

| Fichero | Descripción |
|---|---|
| `Modelfile` | Definición del modelo `asistente-python` |
| `src/inventario_error.py` | Script con un error para consultar a la IA |
| `src/consulta_ollama.py` | Consulta al modelo mediante la API de Ollama |
| `src/comprobar_total_equipos.py` | Pruebas de la función generada por la IA |
| `notebooks/02_ia_local_ollama.ipynb` | Mismo código en un notebook |

## Ejecución

Desde la raíz del repositorio y con el entorno virtual activado. Ollama
debe estar instalado, como se explica en el laboratorio.

```
ollama create asistente-python -f Tema02/Modelfile
python Tema02/src/inventario_error.py
python Tema02/src/consulta_ollama.py
```

La función `total_equipos` propuesta por el modelo se guarda en
`Tema02/src/total_equipos.py`, y después se ejecuta
`python Tema02/src/comprobar_total_equipos.py`.

El notebook se abre en VS Code y se ejecuta con el kernel del entorno
virtual `.venv`.
