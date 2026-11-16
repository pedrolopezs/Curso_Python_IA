"""Incidencia con un diccionario y una función (Tema 7)."""


def describir(incidencia):
    return (incidencia["codigo"] + " " + incidencia["equipo"]
            + " (" + incidencia["prioridad"] + ")")


incidencia = {"codigo": "INC-001", "equipo": "srv-web01",
              "prioridad": "alta"}
print(describir(incidencia))
