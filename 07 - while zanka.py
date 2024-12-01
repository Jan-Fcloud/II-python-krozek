"""
Do zdaj, smo programe pisali linearne. To pomeni, da je potek od zgoraj navzdol, brez ponavljanja in točno tako kot je napisano po zaporedju.

Recimo, da želimo izpisati števila od 1 do 10 v konzolo.
Do zdaj bi to naredili tako, da bi napisali print() 10x krat.

Zdaj si pa lahko olajšamo takšno delo z zankami.
V tem primeru, si bomo ogledali zanko "while"

ANG: while
SLO: dokler

While zanka se izvaja, dokler ne dosežemo nekega pogoja, ki smo ga zastavili.
Poglejmo si, kako bi zgornji primer z print() stavki pospešili z zanko:
"""

i = 1 # definiramo spremenljivko, ki se bo po vsaki iteraciji zanke večala za +1

while i<11: # inicializacija: while <pogoj>:
    print(i)
    i += 1 # vsaka iteracija prišteje naši spremenljivki 1

print("KONEC") # "KONEC" se izpiše, po zaključku zanke.

"""
Izpis zgornjega programa je takšen:

1
2
3
4
5
6
7
8
9
10
KONEC

Logika za tem, pa je takšna:

1. Inicializiramo i, ki ima prvotno vrednost 1

2. Program preide v zanko, katera ima zahtevo, da se izvaja dokler je i manjši od 11 in program teče tako:
    2.1. i = 1, zanka se sproži, izpiše 1, ter prišteje zraven 1
    2.2. i = 2, zanka se sproži, izpiše 2, ter prišteje zraven 1
    2.3. i = 3, zanka se sproži, izpiše 3, ter prišteje zraven 1
    2.4. i = 4, zanka se sproži, izpiše 4, ter prišteje zraven 1
    2.5. i = 5, zanka se sproži, izpiše 5, ter prišteje zraven 1
    2.6. i = 6, zanka se sproži, izpiše 6, ter prišteje zraven 1
    2.7. i = 7, zanka se sproži, izpiše 7, ter prišteje zraven 1
    2.8. i = 8, zanka se sproži, izpiše 8, ter prišteje zraven 1
    2.9. i = 9, zanka se sproži, izpiše 9, ter prišteje zraven 1
    2.10. i = 10, zanka se sproži, izpiše 10, ter prišteje zraven 1
    2.11. i = 11, zanka se NE sproži, saj i ni več manjši od 11
    
3. Zanka je zaključena, program preide naprej na print stavek in izpiše "KONEC".

"""