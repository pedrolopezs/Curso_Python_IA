"""Conjuntos: unicidad y operaciones (Tema 4)."""
marcas = ["HP", "Dell", "HP", "Lenovo", "Dell"]
unicas = set(marcas)
print(len(marcas), len(unicas))
print(sorted(unicas))

unicas.add("Acer")
unicas.discard("Asus")
print(sorted(unicas))
print("HP" in unicas)

# Operaciones entre conjuntos
almacen_a = {"SRV01", "SRV02", "SW01"}
almacen_b = {"SRV02", "SW01", "AP01"}
print(sorted(almacen_a | almacen_b))
print(sorted(almacen_a & almacen_b))
print(sorted(almacen_a - almacen_b))
print(sorted(almacen_a ^ almacen_b))
print({"SRV01"} <= almacen_a)

# {} crea un diccionario vacío
print(type({}), type(set()))
