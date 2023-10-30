import os
os.system("cls")

from pathlib import Path

base = Path.home()
guia = Path(base, "Europa", "Barcelona",Path("Sagrada Familia.txt"))
guia2 = guia.with_name("La_Pedrera")
print(guia.parent.parent)
print(guia2)

