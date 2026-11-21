# Informe de tickets (Tema 9)
import pandas as pd

# N/D se lee como valor ausente
tickets = pd.read_csv("Tema09/datos/tickets.csv", na_values=["N/D"])
print(len(tickets), "tickets")
print("Sin resolver:", tickets["horas_resolucion"].isna().sum())
print("Media global:", round(tickets["horas_resolucion"].mean(), 2), "h")

# Resumen por técnico: número de tickets y horas medias
por_tecnico = tickets.groupby("tecnico")["horas_resolucion"].agg(
    ["count", "mean"]
)
por_tecnico = por_tecnico.round(1).sort_values("mean", ascending=False)
print(por_tecnico)

# Resumen por prioridad
print(tickets.groupby("prioridad")["horas_resolucion"].mean().round(1))

# Guardar el informe sin el índice numérico
por_tecnico.reset_index().to_csv("Tema09/informe_tickets.csv", index=False)
