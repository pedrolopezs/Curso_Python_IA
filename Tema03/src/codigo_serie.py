"""Normalización de un código de serie (Tema 3)."""

bruto = "  srv-01-a "
print(f"[{bruto}]")

limpio = bruto.strip().upper()
print(f"[{limpio}]")

partes = limpio.split("-")
print(partes)
print("-".join(partes))
print(limpio.replace("-", ""))

print(len(limpio))
print(limpio.find("01"))
print("SRV" in limpio)
print("Código:\n" + limpio)
