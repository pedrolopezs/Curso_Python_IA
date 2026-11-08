# Tema 5. Funciones y comprensiones

Ficheros de apoyo del laboratorio del Tema 5.

## Contenido

| Fichero | Descripción |
|---|---|
| `src/funciones_basicas.py` | Funciones, `return`, varios valores y varios `return` |
| `src/argumentos.py` | Argumentos posicionales, por nombre, por defecto, `*args`, `**kwargs` y `lambda` |
| `src/documentacion.py` | Docstrings, anotaciones de tipo y consulta de la documentación |
| `src/ambito.py` | Variables locales y globales, `global` y su alternativa |
| `src/alias_copias.py` | Listas como argumentos y valor por defecto mutable |
| `src/comprensiones.py` | Comprensiones de listas, diccionarios, conjuntos y generadoras |
| `src/informe_registro.py` | Informe de un registro de accesos con funciones y comprensiones |
| `src/registrar_eventos.py` | Script con un error de valor por defecto mutable |
| `src/comprobar_eventos.py` | Pruebas de `registrar_eventos.py` |
| `src/comprobar_niveles.py` | Pruebas del script que genera la IA local |
| `notebooks/05_funciones_y_comprensiones.ipynb` | Mismo código en un notebook |

## Ejecución

Desde la raíz del repositorio y con el entorno virtual activado.

```
python Tema05/src/funciones_basicas.py
python Tema05/src/argumentos.py
python Tema05/src/documentacion.py
python Tema05/src/ambito.py
python Tema05/src/alias_copias.py
python Tema05/src/comprensiones.py
python Tema05/src/informe_registro.py
python Tema05/src/comprobar_eventos.py
```

El script `comprobar_eventos.py` muestra un ERROR hasta que se corrige
`registrar_eventos.py` con `None` como valor por defecto. Para volver al
fichero original se ejecuta `git restore Tema05/src/registrar_eventos.py`.

El script `comprobar_niveles.py` comprueba el fichero `contar_niveles.py`,
que se genera con la IA local durante el laboratorio y se elimina al
terminar.

Los ejercicios propuestos se guardan en `Tema05/propuestos`.

El notebook se abre en VS Code y se ejecuta con el kernel del entorno
virtual `.venv`.
