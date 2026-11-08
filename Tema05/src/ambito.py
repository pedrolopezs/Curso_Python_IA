"""Variables locales y globales, global y su alternativa (Tema 5)."""

limite = 100
conexiones_activas = 0


# Asignar dentro de la función crea una variable local
def comprobar(valor):
    limite = 50
    return valor > limite


print(comprobar(70), limite)


# global hace que la función use la variable global
def registrar_conexion():
    global conexiones_activas
    conexiones_activas += 1


registrar_conexion()
registrar_conexion()
print(conexiones_activas)


# Alternativa recomendada: recibir el valor y devolver el resultado
def sumar_conexion(conexiones):
    return conexiones + 1


total = 0
total = sumar_conexion(total)
total = sumar_conexion(total)
print(total)
