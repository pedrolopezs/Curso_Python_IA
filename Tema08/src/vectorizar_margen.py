"""Margen sobre las latencias con un bucle for (Tema 8)."""
latencias = [12.4, 14.1, 18.7, 21.3, 35.8, 29.4]
con_margen = []
for latencia in latencias:
    con_margen.append(latencia + 5.0)
print(con_margen)
