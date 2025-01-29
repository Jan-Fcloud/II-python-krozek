"""
Python ima zelo zanimivo funkcijo, ki se imenuje "match".

Ta funkcija služi za primerjavo vrednosti, kot na primer "if" statement.

Primer z "if" povpraševanjem:

if x == 1:
    print("x je 1")
elif x == 2:
    print("x je 2")
elif x == 3:
    print("x je 3")
else:
    print("x ni 1, 2 ali 3")

Poglejmo si primer z "match" funkcijo:
"""

x = 1 # V spremenljivko "x" shranimo vrednost 1.

match x: # match deluje z vsemi vrednostmi tako, kot "if" statement.
    case 1: # Če je vrednost spremenljivke "x" enaka 1, se izvede ta blok kode.
        print("x je 1")
    case 2: # Če je vrednost spremenljivke "x" enaka 2, se izvede ta blok kode.
        print("x je 2")
    case 3: # Če je vrednost spremenljivke "x" enaka 3, se izvede ta blok kode.
        print("x je 3")
    case _: # Če ni enaka nobeni od teh vrednosti, se izvede ta blok kode.
        print("x ni 1, 2 ali 3")


"""
V zgornjem primeru smo primerjali vrednost spremenljivke "x" z vrednostmi 1, 2 in 3.

Če je vrednost spremenljivke "x" enaka 1, se izpiše "x je 1".
Če je vrednost spremenljivke "x" enaka 2, se izpiše "x je 2".
Če je vrednost spremenljivke "x" enaka 3, se izpiše "x je 3".
Če ni enaka nobeni od teh vrednosti, se izpiše "x ni 1, 2 ali 3".

"""


