# Tema 6. Gestión de errores, tratamiento de ficheros y módulos

Ficheros de apoyo del laboratorio del Tema 6.

## Contenido

| Fichero | Descripción |
|---|---|
| `datos/accesos.log` | Registro de accesos de ejemplo, con una línea dañada y una vacía |
| `datos/puertos.txt` | Lista de puertos, uno por línea |
| `src/traceback_media.py` | Traceback de una excepción no tratada |
| `src/capturar_errores.py` | `try`, `except`, `else` y `finally` |
| `src/validar_puerto.py` | Validación de una entrada con `input()` |
| `src/lanzar_excepciones.py` | Excepciones con `raise` |
| `src/leer_registro.py` | Lectura de un fichero con `open()` y `with` |
| `src/escribir_resumen.py` | Escritura y modos `"w"` y `"a"` |
| `src/errores_ficheros.py` | Excepciones al abrir un fichero |
| `src/modulos_estandar.py` | Módulos de la biblioteca estándar y `functools` |
| `src/registro.py` | Módulo propio con bloque `__main__` |
| `src/informe.py` | Script que importa `registro.py` |
| `src/herramientas/` | Paquete con los módulos `registro.py` e `informes.py` |
| `src/informe_paquete.py` | Script que importa el paquete `herramientas` |
| `src/rutas.py` | Rutas, directorios y variables de entorno con `os` y `pathlib` |
| `src/args.py` | Argumentos de la línea de comandos con `sys` |
| `src/consulta_modelos.py` | Lista de modelos de Ollama con `requests` |
| `src/consulta_generate.py` | Consulta a un modelo de Ollama con `requests.post()` |
| `src/listar_modelos.py` | Códigos de estado y errores de red |
| `src/informe_peticiones.py` | Informe de un registro con errores, ficheros y módulos |
| `src/leer_puerto.py` | Script con un error sin tratar |
| `src/comprobar_puerto.py` | Pruebas de `leer_puerto.py` |
| `src/comprobar_modelos.py` | Pruebas del script que genera la IA local |
| `notebooks/06_gestion_de_errores_ficheros_y_modulos.ipynb` | Mismo código en un notebook |

## Ejecución

Desde la raíz del repositorio y con el entorno virtual activado.

```
python Tema06/src/traceback_media.py
python Tema06/src/capturar_errores.py
python Tema06/src/validar_puerto.py
python Tema06/src/lanzar_excepciones.py
python Tema06/src/leer_registro.py
python Tema06/src/escribir_resumen.py
python Tema06/src/errores_ficheros.py
python Tema06/src/modulos_estandar.py
python Tema06/src/informe.py
python Tema06/src/informe_paquete.py
python Tema06/src/rutas.py
python Tema06/src/args.py Tema06/datos/accesos.log
python Tema06/src/consulta_modelos.py
python Tema06/src/informe_peticiones.py
python Tema06/src/comprobar_puerto.py
```

Los scripts `consulta_modelos.py`, `consulta_generate.py` y
`listar_modelos.py` necesitan el paquete `requests` y el servicio de Ollama
activo.

El script `comprobar_puerto.py` muestra un ERROR hasta que se corrige
`leer_puerto.py`. Para volver al fichero original se ejecuta
`git restore Tema06/src/leer_puerto.py`.

El script `comprobar_modelos.py` comprueba el fichero `modelos_ollama.py`,
que se genera con la IA local durante el laboratorio y se elimina al
terminar.

Los ficheros `Tema06/resumen.txt`, `Tema06/requirements.txt` y el directorio
`Tema06/informes` se generan durante el laboratorio.

Los ejercicios propuestos se guardan en `Tema06/propuestos`.

El notebook se abre en VS Code y se ejecuta con el kernel del entorno
virtual `.venv`.
