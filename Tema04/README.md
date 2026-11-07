# Tema 4. Estructuras de datos

Ficheros de apoyo del laboratorio del Tema 4.

## Contenido

| Fichero | Descripción |
|---|---|
| `src/indices_slicing.py` | Índices, slicing, salto e inversión de cadenas |
| `src/listas.py` | Listas: acceso, métodos, orden y recorrido |
| `src/identidad_copias.py` | Igualdad, identidad, alias y copias |
| `src/tuplas.py` | Tuplas y desempaquetado |
| `src/conjuntos.py` | Conjuntos y operaciones entre conjuntos |
| `src/diccionarios.py` | Diccionarios: consulta, modificación y recorrido |
| `src/inventario.py` | Inventario como lista de diccionarios |
| `src/copia_inventario.py` | Script con un error de copia superficial |
| `src/comprobar_copia.py` | Pruebas de `copia_inventario.py` |
| `src/comprobar_resumen.py` | Pruebas del script que genera la IA local |
| `notebooks/04_estructuras_de_datos.ipynb` | Mismo código en un notebook |

## Ejecución

Desde la raíz del repositorio y con el entorno virtual activado.

```
python Tema04/src/indices_slicing.py
python Tema04/src/listas.py
python Tema04/src/identidad_copias.py
python Tema04/src/tuplas.py
python Tema04/src/conjuntos.py
python Tema04/src/diccionarios.py
python Tema04/src/inventario.py
python Tema04/src/comprobar_copia.py
```

El script `comprobar_copia.py` muestra un ERROR con `Original: 0` hasta
que se corrige `copia_inventario.py` con `copy.deepcopy()`. Para volver
al fichero original se ejecuta
`git restore Tema04/src/copia_inventario.py`.

El script `comprobar_resumen.py` comprueba el fichero `resumen_tipos.py`,
que se genera con la IA local durante el laboratorio y se elimina al
terminar.

El notebook se abre en VS Code y se ejecuta con el kernel del entorno
virtual `.venv`.
