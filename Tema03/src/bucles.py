"""Bucles for y while (Tema 3)."""

codigo = "SRV-01-A"
serie = "SRV01"

# for con range
for n in range(1, 4):
    print("Equipo", n)

# for con una cadena y enumerate
for pos, car in enumerate(serie, start=1):
    print(pos, car)

# continue: ignora los guiones
limpio = ""
for car in codigo:
    if car == "-":
        continue
    limpio += car
print(limpio)

# break: se detiene en el primer dígito
for car in codigo:
    if car.isdigit():
        print("Primer dígito:", car)
        break

# while con contador
intentos = 0
while intentos < 3:
    intentos += 1
    print("Intento", intentos)
