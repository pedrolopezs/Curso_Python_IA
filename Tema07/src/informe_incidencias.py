"""Informe de incidencias con clases y excepción propia (Tema 7)."""


class IncidenciaError(Exception):
    """Error al crear una incidencia."""


class Incidencia:
    PRIORIDADES = ("critica", "alta", "media", "baja")

    def __init__(self, codigo, equipo, prioridad, horas):
        if prioridad not in self.PRIORIDADES:
            raise IncidenciaError(f"Prioridad no válida: {prioridad}")
        self.codigo = codigo
        self.equipo = equipo
        self.prioridad = prioridad
        self.horas = horas


class Registro:
    def __init__(self):
        self.incidencias = []
        self.descartadas = 0

    def agregar_linea(self, linea):
        try:
            codigo, equipo, prioridad, horas = linea.split()
            incidencia = Incidencia(codigo, equipo, prioridad, int(horas))
        except (ValueError, IncidenciaError):
            self.descartadas += 1
        else:
            self.incidencias.append(incidencia)


if __name__ == "__main__":
    registro = Registro()
    with open("Tema07/datos/incidencias.txt", encoding="utf-8") as fichero:
        for linea in fichero:
            registro.agregar_linea(linea)
    print(len(registro.incidencias), registro.descartadas)
