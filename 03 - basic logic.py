"""
Pri pregledu spremenljivk smo omenjali Boolean, ampak do zdaj še ga nismo nikjer prav uporabili.

Boolean / bool, se uporablja pri povpraševanjih v kodi.

Sintaksa za povpraševanje/logiko je naslednja:
"""

spr1 = True # določimo spremenljivko kero bomo obravnavali

if spr1: # če je spr1 True, se izvede koda znotraj if
    print("spr1 je True!")
else:    # v primeru da je spr1 False, se ignorira zgornje in se izvede spodnja kofa znotraj esle
    print("spr1 je False!")

"""
Seveda logika ni samo za sam Boolean. Lahko uporabljamo za primerjanje:
"""

spr1 = 200
spr2 = 500

if spr1 == spr2: # Primerjamo spr1 in spr2 z sintakso ==
    print("Stevili sta enaki")
else:
    print("Stevili nista enaki")

"""
V zgornjem primeru smo primerjali dve stevili z posebno sintakso ==.
Katere še obstajajo?

== -> Vrne True če sta leva in desna spremenljivka enaki in False če nista.
!= -> Vrne False če sta leva in desna spremenljivka enaki in True če nista.
<  -> Primerja če je leva vrednost manjša od desne. Vrne True če je in False če ni.
>  -> Primerja če je leva vrednost večja od desne. Vrne True če je in False če ni.
<= -> Primerja če je leva vrednost manjša ALI ENAKA od desne. Vrne True če je in False če ni.
>= -> Primerja če je leva vrednost večja ALI ENAKA od desne. Vrne True če je in False če ni.

Poglejmo si kot primere:
"""

print(10 == 10) # True
print(21 == 31) # False

print(10 != 20) # True
print(35 != 35) # False

print(10 < 15) # True
print(55 < 10) # False

print(100 > 15) # True
print(22 > 100) # False

print(10 <= 10) # True
print(11 <= 10) # False

print(10 >= 10) # True
print(9 >= 33) # False

# Seveda ni samo primerjava za števila.

print("Ena" == "Ena") # True
print("Kruh" == "Burek") # False
# itd...

"""
if in else nista edina. Povpraševanje lahko ima več pogojev. To naredimo z:
- and -> in
- or  -> ali
"""

spr1 = 150

if spr1 < 200 and spr1> 100:
    print("Stevilo je manjse od 200 in vecje od 100")

# Zgornji primer lahko tudi poenostavimo tako:
if 200 > spr1 > 100:
    print("Stevilo je manjse od 200 in vecje od 100")

"""
And in or lahko uporabimo kolikokrat zelimo.
Zdaj pa si še poglejmo več izidov povpraševanja.

Tukaj pa še dodamo zraven sintakso elif
"""

spr1 = 500

if spr1 < 400:
    print("spr1 je manjša od 400")
elif spr1 < 600:
    print("spr1 je manjša od 600")
else:
    print("spr1 ni manša od 400 ali 600")

"""
Logiko si je včasih najlažje pobesedit.

ČE je 20 manjše od 10, skočim.
DRUGAČE ČE je 10 večje od 5, se vsedem
DRUGAČE pa se vležem

Zgornji primer pretvorjen v kodo:
"""

if 20 < 10:
    print("skočim")
elif 10 > 5:
    print("se vsedem")
else:
    print("se vležem")

"""
Pri logiki lahko tudi uporabimo matematične izraze. Recimo MODULO (10 % 10 = 0)
(modulo nam da ostanek deljenja)
"""

spr1 = 11

if spr1 % 10 == 0:
    print("Ni ostanka")
else:
    print("je ostanek")