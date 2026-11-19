"""Informe de latencias por servidor y por hora (Tema 8)."""
import numpy as np

datos = np.genfromtxt("Tema08/datos/latencias_ausentes.csv",
                      delimiter=",", skip_header=1)
servidores = np.array(["web01", "web02", "db01", "app01", "dns01"])
horas = datos[:, 0]
latencias = datos[:, 1:]
umbral = 20.0

# Media de cada servidor, sin contar los valores ausentes
medias = np.nanmean(latencias, axis=0)

# Horas en que cada servidor supera el umbral. Un nan nunca lo supera
superan = (latencias > umbral).sum(axis=0)

print("Horas registradas:", len(horas))
orden = np.argsort(medias)[::-1]
for posicion in orden:
    print(servidores[posicion], round(medias[posicion], 1),
          superan[posicion])

# Hora más cargada, según la media de todos los servidores
medias_hora = np.nanmean(latencias, axis=1)
posicion_pico = medias_hora.argmax()
print("Hora más cargada:", int(horas[posicion_pico]),
      f"({medias_hora[posicion_pico]:.1f} ms)")

np.savetxt("Tema08/informe_medias.csv", medias, fmt="%.1f")
