"""
Recimo, da želimo, da uporabnik določi kolikokrat se zanka izvede.

V tem primeru, bo treba dobit vnos uporabnika, vnos pretvorit v število, ter dat v range() funkcijo.

Poglejmo si, kako:
"""

stevilo = int(input("Vnesi število: ")) # v spremenljivko stevilo, se shrani pretvorjen vnos uporabnika.

for i in range(stevilo):
    print(i)

    # Izpis (v primeru, da uporabnik vpiše število 5):
    # 0
    # 1
    # 2
    # 3
    # 4