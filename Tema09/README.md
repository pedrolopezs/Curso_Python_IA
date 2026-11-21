# Tema 9. Pandas

Ficheros de apoyo del laboratorio del Tema 9.

## Contenido

| Fichero | Descripción |
|---|---|
| `datos/activos.csv` | 24 activos de TI: código, equipo, fabricante, ubicación, fecha, precio y estado |
| `datos/tickets.csv` | 30 tickets de soporte, con tres horas de resolución `N/D` |
| `datos/activos_sucio.csv` | Inventario con duplicados, texto desordenado, ausentes y fechas erróneas |
| `datos/inventario_excel.csv` | Inventario guardado por Excel (`;`, coma decimal, cp1252) |
| `src/series_dataframe.py` | Creación de `Series` y `DataFrame` |
| `src/explorar_activos.py` | Lectura y exploración con `head()`, `info()` y `describe()` |
| `src/leer_parametros.py` | Parámetros de `read_csv()` y `to_csv()` |
| `src/seleccionar.py` | Selección con `[]`, `loc` e `iloc` |
| `src/filtros.py` | Filtros con máscaras booleanas |
| `src/copias.py` | Copias y asignaciones |
| `src/ordenar_calcular.py` | Ordenación y columnas calculadas |
| `src/agregaciones.py` | Agregaciones y `groupby` |
| `src/ausentes_duplicados.py` | Valores ausentes y duplicados |
| `src/tipos_texto.py` | Conversión de tipos y limpieza de texto |
| `src/fechas.py` | Conversión de fechas y filtros por rango |
| `src/informe_tickets.py` | Informe completo de tickets |
| `src/iva_bucle.py` | Bucle `for`, para vectorizar con la IA local |
| `src/comprobar_iva.py` | Pruebas de `iva_bucle.py` |
| `src/comprobar_limpieza.py` | Pruebas de `limpiar_activos.py`, que se genera con la IA local |
| `src/explicar_cadena.py` | Cadena de métodos, para explicar con la IA local |
| `notebooks/09_pandas.ipynb` | Mismo código en un notebook |

## Ejecución

Desde la raíz del repositorio y con el entorno virtual activado. Pandas se
instala en el primer ejercicio del laboratorio.

```
python Tema09/src/series_dataframe.py
python Tema09/src/explorar_activos.py
python Tema09/src/leer_parametros.py
python Tema09/src/seleccionar.py
python Tema09/src/filtros.py
python Tema09/src/copias.py
python Tema09/src/ordenar_calcular.py
python Tema09/src/agregaciones.py
python Tema09/src/ausentes_duplicados.py
python Tema09/src/tipos_texto.py
python Tema09/src/fechas.py
python Tema09/src/informe_tickets.py
python Tema09/src/explicar_cadena.py
```

Los scripts que leen datos usan la ruta `Tema09/datos/...`, por lo que hay
que ejecutarlos desde la raíz del repositorio.

Los scripts de comprobación ejecutan el script correspondiente y muestran OK
o ERROR en cada prueba. Antes de aplicar la propuesta de la IA local
muestran algún ERROR.

```
python Tema09/src/comprobar_iva.py
python Tema09/src/comprobar_limpieza.py
```

El script `limpiar_activos.py` no está en el repositorio. Se genera con la IA
local durante el laboratorio y se elimina al terminar. Para volver al fichero
original después de probar la propuesta de la IA local en `iva_bucle.py`, se
restaura con `git restore`.

```
git restore Tema09/src/iva_bucle.py
```

Los ficheros `Tema09/requirements.txt`, `Tema09/inventario_utf8.csv`,
`Tema09/inventario_indice.csv` y `Tema09/informe_tickets.csv` se generan
durante el laboratorio.

Los ejercicios propuestos se guardan en `Tema09/propuestos`.

El notebook se abre en VS Code y se ejecuta con el kernel del entorno
virtual `.venv`.
