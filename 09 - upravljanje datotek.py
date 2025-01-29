"""
Python nam omogoča zelo enostavno upravljanje z datotekami.

Za začetek si bomo poglejali, kako lahko iz datoteke beremo vrednosti.

Ustvaril sem datoteko z imenom "vrednosti.txt", v kateri je nekaj teksta (datoteka je v isti mapi kot naš program).
"""

file = open("vrednosti.txt", "r") # Funkcija "open" od nas sprejme dve vrednosti: ime datoteke ter način, v katerem jo bomo odprli.

print(file.read()) # Funkcija "read" nam omogoča, da iz datoteke preberemo vsebino.

file.close() # Funkcija "close" nam omogoča, da zaključimo delo z datoteko.

"""
V zgornjem primeru smo datoteko odprli v načinu "r", kar pomeni, da smo jo odprli za branje.

Imamo pa še druge načine:
    - "r" - branje (read)
    - "w" - pisanje (write)
    - "a" - dodajanje (append)
    - "r+" - branje in pisanje (read + write)

Poglejmo si primer, kjer bomo datoteko odprli v načinu "w", kar pomeni, da bomo datoteko odprli za pisanje.
V primeru, da datoteka ne obstaja, bo ustvarjena. Če pa obstaja, bo njena vsebina izbrisana.

V tem primeru, bomo uporabili ime datoteke, ki ne obstaja, zato bo ustvarjena.
"""

file = open("vrednosti.txt", "w") # Odprli smo datoteko v načinu "w", kar pomeni, da bomo datoteko odprli za pisanje.

file.write("Novo vsebina") # Funkcija "write" nam omogoča, da v datoteko zapišemo novo vsebino.

file.close() # Zaključili smo delo z datoteko.

# Če datoteko odpremo v načinu za branje tak kot prej, nam vsebina vrne "Novo vsebina", saj smo zapisali v datoteko.

"""
Zdaj pa si poglejmo, kako lahko datoteko odpremo v načinu "a", kar pomeni, da bomo datoteko odprli za dodajanje.

V tem primeru, bomo datoteko odprli v isti mapi kot naš program.
"""

file = open("vrednosti.txt", "a") # Odprli smo datoteko v načinu "a", kar pomeni, da bomo datoteko odprli za dodajanje.

file.write("Novo vsebina") # Funkcija "write" nam omogoča, da v datoteko zapišemo novo vsebino.

file.close() # Zaključili smo delo z datoteko.

# Če datoteko odpremo v načinu za branje tak kot prej, nam vsebina vrne vse tak kot je bilo prvotno, + "Novo vsebina", saj smo zapisali v datoteko v načinu dodajanja, kar pomeni, da se vsebina ni izbrisala.






