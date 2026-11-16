# Tema 7. Introducción a la programación orientada a objetos

Ficheros de apoyo del laboratorio del Tema 7.

## Contenido

| Fichero | Descripción |
|---|---|
| `datos/incidencias.txt` | Registro de 15 incidencias, con una de prioridad no válida |
| `src/equipo_basico.py` | Primera clase con `__init__()` y atributos |
| `src/equipo_estado.py` | Métodos, `self` y cambio de estado |
| `src/representacion.py` | Objetos sin `__str__()` ni `__eq__()` |
| `src/atributos_clase.py` | Atributos de clase y lista compartida |
| `src/encapsulacion.py` | Atributo interno con guion bajo y validación |
| `src/inventario.py` | Composición con `Inventario` y `Equipo` |
| `src/herencia.py` | Herencia, `super()` y polimorfismo |
| `src/equipos.py` | Módulo propio con la clase `Equipo` y bloque `__main__` |
| `src/principal.py` | Script que importa `equipos.py` |
| `src/excepciones.py` | Excepción propia `IncidenciaError` |
| `src/informe_incidencias.py` | Script completo con clases y excepción propia |
| `src/revisar_servidores.py` | Script con una lista compartida, para revisar con la IA |
| `src/comprobar_revision.py` | Pruebas de `revisar_servidores.py` |
| `src/refactorizar_incidencia.py` | Diccionario y función, para refactorizar con la IA |
| `src/comprobar_refactor.py` | Pruebas de `refactorizar_incidencia.py` |
| `src/optimizar_inventario.py` | Búsqueda lineal, para optimizar con la IA |
| `src/comprobar_optimizacion.py` | Pruebas de `optimizar_inventario.py` |
| `src/documentar_equipo.py` | Clase sin documentar, para documentar con la IA |
| `src/comprobar_documentacion.py` | Pruebas de `documentar_equipo.py` |
| `notebooks/07_poo.ipynb` | Mismo código en un notebook |

## Ejecución

Desde la raíz del repositorio y con el entorno virtual activado.

```
python Tema07/src/equipo_basico.py
python Tema07/src/equipo_estado.py
python Tema07/src/representacion.py
python Tema07/src/atributos_clase.py
python Tema07/src/encapsulacion.py
python Tema07/src/inventario.py
python Tema07/src/herencia.py
python Tema07/src/equipos.py
python Tema07/src/principal.py
python Tema07/src/excepciones.py
python Tema07/src/informe_incidencias.py
```

El script `principal.py` importa el módulo `equipos`, por lo que se ejecuta
con la ruta indicada y Python busca el módulo en el directorio del script.

Los scripts de comprobación ejecutan el script correspondiente y muestran OK
o ERROR en cada prueba. Antes de aplicar la propuesta de la IA local
muestran algún ERROR, salvo `comprobar_optimizacion.py`, que solo verifica
que el resultado no ha cambiado.

```
python Tema07/src/comprobar_revision.py
python Tema07/src/comprobar_refactor.py
python Tema07/src/comprobar_optimizacion.py
python Tema07/src/comprobar_documentacion.py
```

Para volver a los ficheros originales después de probar una propuesta de la
IA local, se restaura cada uno con `git restore`.

```
git restore Tema07/src/revisar_servidores.py
git restore Tema07/src/refactorizar_incidencia.py
git restore Tema07/src/optimizar_inventario.py
git restore Tema07/src/documentar_equipo.py
```

Los ejercicios propuestos se guardan en `Tema07/propuestos`.

El notebook se abre en VS Code y se ejecuta con el kernel del entorno
virtual `.venv`.
