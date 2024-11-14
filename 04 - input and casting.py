"""
Do zdaj smo podatke vpisovali direktno v našo kodo, kar pomeni, da nima uporabnik nobene kontrole o izvajanju rezultatov programa.
Pogledali bomo, kako lahko program sprejme input/vnos podatkov od uporabnika pri zagnanem programu.

Python ima za to funkcijo input().

V spodnjem primeru, bomo uporabili funkcijo za vnos podatkov, shranili uporabnikov vnos v spremenljivko, ter rezultat izpisali.
"""

podatek = input() # Uporabnik vnese npr. "ABC"

print(podatek) # ABC

"""
Težava v zgornjem primeru je, da uporabnik ne ve kdaj naj vnese podatke, saj se v konzoli nič ne izpiše.
To lahko zlahka popravimo tako, da znotraj input() funkcije, podamo kot parameter text ki se izpiše pred čakanjem na vnos.
"""

podatek = input("Vnesi podatek: ") # V konzoli vidimo zdaj -> Vnesi podatek:

print(podatek)

"""
Podatki ki so dobljeni z inputom, se lahko uporabijo kot vsaka druga spremenljivka, ki smo jih do zdaj obravnavali.

Kaj pa če bi radi dobili input od uporabnika, ki je število, da ga lahko pomnožimo 2 krat?
V takem primeru pa ne gre samo z input(), saj vse kar je dobljeno tako, je zgolj string/text.
Zato je treba podatek pretvorit v drugi tip.

To se naredi tako, da se napiše kratica vrste tipa ki ga želimo, dodamo oklepaje, in znotraj oklepajev damo naš podatek ki ga želimo pretrovit.
Takšnemu pretvarjanju se tudi reče Casting.

Imamo sledeče:
- str(<podatek>) -> podatek se pretvori v string/text
- int(<podatek>) -> podatek se pretvori v integer/število
- float(<podatek) -> podatek se pretvori v float/decimalko
- bool(<podatek>) -> podatek se pretvori v boolean/logiko

Poglejmo si nekaj primerov pretvarjanja:
"""

print(str(12)) # "12"

print(int(3.14)) # 3

print(float("2.12")) # 2.12

print(bool(1)) # True

"""
Zdaj pa združimo znanje inputa in castinga, da ustvarimo program, ki sprejme število, ter ga množi z 2:
"""

vnos = input("Vnesi stevilo: ") # Dobimo vnos stevilo od uporabnika

pretvorba = int(vnos) # Pretvorimo vnos v stevilo

print(pretvorba * 2) # izpisemo nas pretvorjen vnos podvojen z 2



