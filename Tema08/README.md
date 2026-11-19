# Tema 8. NumPy

Ficheros de apoyo del laboratorio del Tema 8.

## Contenido

| Fichero | Descripción |
|---|---|
| `datos/latencias.csv` | Latencias en ms de cinco servidores, una fila por hora (24 filas) |
| `datos/latencias_ausentes.csv` | Los mismos datos con tres celdas `N/D` |
| `src/listas_y_arrays.py` | Listas frente a arrays |
| `src/crear_arrays.py` | Creación de arrays, atributos, conversión de tipo y cambio de forma |
| `src/indexacion.py` | Indexación y slicing en una y dos dimensiones |
| `src/vistas_copias.py` | Vistas y copias |
| `src/vectorizacion.py` | Operaciones vectorizadas y broadcasting |
| `src/mascaras.py` | Máscaras booleanas, condiciones compuestas y `np.where()` |
| `src/agregaciones.py` | Agregaciones, `axis`, orden y unión de arrays |
| `src/cargar_guardar.py` | Carga y guardado de datos con `np.loadtxt()` y `np.savetxt()` |
| `src/valores_ausentes.py` | Valores ausentes con `np.genfromtxt()` y `np.isnan()` |
| `src/informe_latencias.py` | Script completo con el informe de latencias |
| `src/vectorizar_margen.py` | Bucle `for`, para vectorizar con la IA local |
| `src/comprobar_vectorizacion.py` | Pruebas de `vectorizar_margen.py` |
| `src/comprobar_hora_pico.py` | Pruebas de `hora_pico.py`, que se genera con la IA local |
| `src/explicar_slice.py` | Slice sobre una matriz, para explicar con la IA local |
| `notebooks/08_numpy.ipynb` | Mismo código en un notebook |

## Ejecución

Desde la raíz del repositorio y con el entorno virtual activado. NumPy se
instala en el primer ejercicio del laboratorio.

```
python Tema08/src/listas_y_arrays.py
python Tema08/src/crear_arrays.py
python Tema08/src/indexacion.py
python Tema08/src/vistas_copias.py
python Tema08/src/vectorizacion.py
python Tema08/src/mascaras.py
python Tema08/src/agregaciones.py
python Tema08/src/cargar_guardar.py
python Tema08/src/valores_ausentes.py
python Tema08/src/informe_latencias.py
python Tema08/src/explicar_slice.py
```

Los scripts que leen datos usan la ruta `Tema08/datos/...`, por lo que hay
que ejecutarlos desde la raíz del repositorio.

Los scripts de comprobación ejecutan el script correspondiente y muestran OK
o ERROR en cada prueba. Antes de aplicar la propuesta de la IA local
muestran algún ERROR.

```
python Tema08/src/comprobar_vectorizacion.py
python Tema08/src/comprobar_hora_pico.py
```

El script `hora_pico.py` no está en el repositorio. Se genera con la IA local
durante el laboratorio y se elimina al terminar. Para volver al fichero
original después de probar la propuesta de la IA local en
`vectorizar_margen.py`, se restaura con `git restore`.

```
git restore Tema08/src/vectorizar_margen.py
```

Los ficheros `Tema08/requirements.txt`, `Tema08/medias.csv` y
`Tema08/informe_medias.csv` se generan durante el laboratorio.

Los ejercicios propuestos se guardan en `Tema08/propuestos`.

El notebook se abre en VS Code y se ejecuta con el kernel del entorno
virtual `.venv`.
