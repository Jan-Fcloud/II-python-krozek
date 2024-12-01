"""
Naredite razred "Oseba", ki vsebuje naslednje vrednosti:
- ime
- starost
- denar,
- list, ki bo hranil imena prijateljev osebe (naj bo prvotno prazen).

1. Parametri inicializacije razreda (__init__), so naj brez lista, znotraj funkcije pa vseeno definirajte prazen list.

2. V razredu napišite funkcijo, ki kot parameter dobi text, ki predstavlja ime prijatelja, ter se doda v list prijateljev razreda (za vnos je input()).

3. V glavnem programu ustvarite osebo z pomočjo vnosa (input()) in jo na koncu izpišite

4. Razredu dodajte funkcijo, ki izpiše "<ime> je star/a več kot 21" ali pa, da ni. To se zve z atributom starost vašega razreda.

5. Razredu podrite __str__ funkcijo, ter jo napišite tako, da izpiše naslednje:
    <ime>, je star/a <starost>, ima <denar>€ in ima <list.__len__()> prijatelja/ev

    P.S:
        - Če napišemo ime lista, ter dodamo zraven .__len__(), nam python vrne število elementov v listu.
"""

# ---
# TODO: RAZLAGA!!
# ---

class Oseba:
    def __init__(self, ime, starost, denar):
        self.ime = ime
        self.starost = int(starost)
        self.denar = int(denar)
        self.prijatelji_list = []

    def dodaj_prijatelja(self, prijatelj):
        self.prijatelji_list.append(prijatelj)

    def preveri_starost(self):
        if self.starost > 21:
            print(f"{self.ime} je star/a več kot 21.")
        else:
            print(f"{self.ime} ni star/a več kot 21.")

    def __str__(self):
        return f"{self.ime}, je star/a {str(self.starost)}, ima {str(self.denar)}€ in ima {str(self.prijatelji_list.__len__())} prijatelja/ev."

Ime = input("Vpiši ime: ")
Starost = input("Vpiši starost: ")
Denar = input("Vpiši denar: ")

moja_oseba = Oseba(Ime, Starost, Denar)
print(moja_oseba)

Prijatelj = input("Vpiši ime prijatelja: ")
moja_oseba.dodaj_prijatelja(Prijatelj)

print(moja_oseba)