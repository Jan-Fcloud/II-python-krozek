"""
Naredite razred "Oseba", ki vsebuje naslednje vrednosti:
- ime
- starost
- denar

1. Inicializirajte 3 spremenljivke z razredom.

2. Spremenite vrednost ene spremenljivke (DIREKTNO -> spr.ime = "Matej").

3. Razredu dodajte funkcijo, ki izpiše "ime" in "starost" osebe (za to uporabite __str__).

4. Napišite funkcijo, ki preveri denar osebe in vrne True ali False, glede na to, če ima oseba več kot 100 denarja.
"""


class Oseba: # Ustvarimo razred z imenom Oseba
    def __init__(self, ime, starost, denar): # __init__ se zažene vedno ob inicializaciji razreda. Funkcija od nas zahteva ime, starost in denar
        self.ime = ime # shranimo ime, ki smo ga podali, v ime, ki je znotraj razreda
        self.starost = starost # shranimo starost
        self.denar = denar # shranimo denar

    def __str__(self): # __str__ se zažene vedno, ko želimo naš razred obravnavat kot text. Npr, da želimo razred izpisati z print()
        return self.ime + " - " + str(self.starost) # vrnemo <ime> - <starost>

    def preveriDenar(self): # preveriDenar smo določili sami, ki preveri, če ima oseba več kot 100 denarja.
        if self.denar > 100:
            return True # V primeru, da ima oseba več kot 100, nam funkcija vrne True
        else:
            return False # V primeru, da oseba nima več kot 100, nam funkcija vrne False


oseba1 = Oseba("Miha", 22, 100)   # Inicializiramo 1. Osebo
oseba2 = Oseba("Luka", 33, 160)   # Inicializiramo 2. Osebo
oseba3 = Oseba("Mojca", 18, 100)  # Inicializiramo 3. Osebo

print("Pred spremembami: ")
print(oseba1)
print(oseba2)
print(oseba3)

oseba1.ime = "Spremenjeno" # Direktno spremenimo ime za oseba1

print()
print("Po spremembah:")
print(oseba1)
print(oseba2)
print(oseba3)

print()
print("Vec kot sto denarja?")
print(oseba1.preveriDenar()) # Pokličemo funkcijo, ki preveri denar za oseba1
print(oseba2.preveriDenar()) # Pokličemo funkcijo, ki preveri denar za oseba2
print(oseba3.preveriDenar()) # Pokličemo funkcijo, ki preveri denar za oseba3