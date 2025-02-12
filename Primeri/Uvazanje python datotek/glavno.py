"""
V tem primeru bomo naredili program, ki bo uvozil našo drugo python datoteko, ter klical njeno glavno funkcijo.

Uvazanje nam omogoča, da izvedemo kodo, ki je v drugi datoteki, tudi če je ta datoteka uvozila našo glavno datoteko.
Zelo uporabno je pri večjih programih, ki jih želimo razdeliti na več datotek za lažjo preglednost in razumevanje.
"""

# Uvozimo našo drugo python datoteko
from knjiznica import glavna_funkcija
# Uvozimo tako, da uporabimo ime datoteke in funkcijo, ki je v njej.

# Izvedemo našo glavno funkcijo
glavna_funkcija()