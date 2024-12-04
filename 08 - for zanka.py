"""
Do sedaj smo delali z while zanko, ki pa ni edina.

While je v redu, če nismo prepričani koliko časa se bo nekaj izvajalo.
V primeru, da smo pa hoteli izvajat zanko X-krat, smo pa morali določit posebej spremenljivko v naprej.

V tem primeru, si bomo pogledali FOR zanko, ki je narejena natanko zato, da se izvede X-krat.

Sintaksa for zanke, je naslednje:

    for <poljubno_ime> in <list/array/itd.>:
        <koda>...

    <poljubno_ime> v zgornjem primeru, je ime spremenljivke, ki jo smatramo kot enojno vrednost.
    Vsaka iteracija zanke, vzeme naslednji element našega lista.

    Npr, da imamo naslednji list:
        moj_list = ["ena", "dva", "tri", "stiri"]

    v for zanki se zgodi naslednje:
    - Prva iteracija vzeme prvi element. To pomeni, da bo i = "ena"
    - Druga iteracija vzeme drugi element. To pomeni, da bo i = "dva"
    - Tretja iteracija vzeme tretji element. To pomeni, da bo i = "tri"
    - Četrta iteracija vzeme četrti element. To pomeni, da bo i = "stiri"

    Po četrtem, se zanka koča, saj je šla skozi vse elemente lista, ki obstajajo.

"""

moj_list = ["ena", "dva", "tri", "stiri"] # definiramo list, s štirimi elementi

for i in moj_list: # Uporabimo zgornjo pravilo zapisa
    print(i) # Izpišemo vsaki element posebej

# Izpis:
#   ena
#   dva
#   tri
#   stiri

"""
Lahko pa tudi sami določimo kolikokrat se bo zanka izvedla brez, da podamo svoj list:

To naredimo z funkcijo range(), ki deluje tako:
    - Parameter je lahko en, ali pa dva.
    
    1. V primeru, da damo funkciji samo eno število, nam vrne skupek števil od 0 do X-1 (X = naše vneseno število)
    2. V primeru, da damo funkciji dve števili, nam vrne skupek števil od X do Y-1 (X in Y = naši vneseni števili)
    
    Kot vidite, vrne vedno eno manj od našega največjega števila!
"""

for i in range(1,9): # Podamo števili 1 in 9. Dobimo nazaj: [1,2,3,4,5,6,7,8]
    print(i) # Vsaka iteracija, izpiše naslednji element skupka števil. Izpis:
        # 1
        # 2
        # 3
        # 4
        # 5
        # 6
        # 7
        # 8

for i in range(9): # Podamo samo število 9. Dobimo nazaj: [0,1,2,3,4,5,6,7,8]
    print(i) # Vsaka iteracija, izpiše naslednji element skupka števil. Izpis:
        # 0
        # 1
        # 2
        # 3
        # 4
        # 5
        # 6
        # 7
        # 8

"""
Seveda for zanka ni samo za iteriranje listov in izvajanju s števili.
Lahko tudi uporabimo zanko, da gremo skozi črke v besedi:
"""

text = "Beseda"

for i in text: # Naš skupek vrednosti je string/tekst
    print(i) # Izpis:
    # B
    # e
    # s
    # e
    # d
    # a
