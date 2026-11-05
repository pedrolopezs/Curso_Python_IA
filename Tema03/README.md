# Tema 3. Sintaxis básica de Python

Ficheros de apoyo del laboratorio del Tema 3.

## Contenido

| Fichero | Descripción |
|---|---|
| `src/tipos_y_objetos.py` | Tipos, conversiones e identidad de objetos |
| `src/ficha_equipo.py` | Entrada de datos y formato con f-strings |
| `src/codigo_serie.py` | Operaciones y métodos de cadenas |
| `src/estado_stock.py` | Condicionales y condición compuesta |
| `src/bucles.py` | Bucles `for` y `while`, `break` y `continue` |
| `src/registro_equipos.py` | Script que reúne los elementos del tema |
| `src/umbral_stock.py` | Script con un error en un valor límite |
| `src/comprobar_umbral.py` | Pruebas con valores límite de `umbral_stock.py` |
| `notebooks/03_sintaxis_basica.ipynb` | Mismo código en un notebook |

## Ejecución

Desde la raíz del repositorio y con el entorno virtual activado.

```
python Tema03/src/tipos_y_objetos.py
python Tema03/src/ficha_equipo.py
python Tema03/src/codigo_serie.py
python Tema03/src/estado_stock.py
python Tema03/src/bucles.py
python Tema03/src/registro_equipos.py
python Tema03/src/comprobar_umbral.py
```

El script `comprobar_umbral.py` muestra un ERROR con 10 unidades hasta
que se corrige la condición de `umbral_stock.py`. Para volver al fichero
original se ejecuta `git restore Tema03/src/umbral_stock.py`.

El notebook se abre en VS Code y se ejecuta con el kernel del entorno
virtual `.venv`.
