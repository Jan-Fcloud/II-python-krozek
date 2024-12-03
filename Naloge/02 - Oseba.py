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


class Oseba: # Ustvarimo razred z imenom Oseba
    def __init__(self, ime, starost, denar): # __init__ funkcija, se zažene vedno ob kreiranju funkcije (npr: oseba = Oseba("Miha", 23, 2000) -> po tem, se avtomatsko kliče __init__)
        self.ime = ime # razred ima spremenljivko "ime"
        self.starost = int(starost) # razred ima spremenljivko "starost", ki se pretvori v integer/stevilko
        self.denar = int(denar) # razred ima spremenljivko "denar", ki se pretvori v integer/stevilko
        self.prijatelji_list = [] # razred ima spremenljivko "prijatelji_list", ki je prazen list

    def dodaj_prijatelja(self, prijatelj): # Ustvarimo svojo poljubno funkcijo znotraj razreda, z imenom "dodaj_prijatelja", ki od nas sprejme eno vrednost, ki se shrani pod "prijatelj". Vsaka funkcija znotraj razreda MORA imeti kot prvi parameter "self".
        self.prijatelji_list.append(prijatelj) # V list "prijatelji_list" dodamo vrednost, ki smo jo prejeli kot parameter

    def preveri_starost(self): # Ustvarimo svojo poljubno funkcijo znotraj razreda, z imenom "preveri_starost", ki od nas ne sprejme ničesar. Vsaka funkcija znotraj razreda MORA imeti kot prvi parameter "self".
        if self.starost > 21: # Če je starost večja od 21, se izpiše spodnje.
            print(f"{self.ime} je star/a več kot 21.")
        else: # Če pa ni, se izpiše spodnje.
            print(f"{self.ime} ni star/a več kot 21.")

    def __str__(self): # Podritev __str__ funkcije, ki se kliče, ko želimo izpisati naš razred. Vsaka funkcija znotraj razreda MORA imeti kot prvi parameter "self".
        return f"{self.ime}, je star/a {self.starost}, ima {self.denar}€ in ima {self.prijatelji_list.__len__()} prijatelja/ev."

Ime = input("Vpiši ime: ") # Vnos imena
Starost = input("Vpiši starost: ") # Vnos starosti
Denar = input("Vpiši denar: ") # Vnos denarja

moja_oseba = Oseba(Ime, Starost, Denar) # Iz zgornjega razreda, kreiramo novo kopijo razreda Oseba, z vrednostmi, ki smo jih podali znotraj oklepajev.
print(moja_oseba) # Izpis vseh vrednosti, ki jih ima naša kopija razreda

Prijatelj = input("Vpiši ime prijatelja: ") # Vnos imena prijatelja
moja_oseba.dodaj_prijatelja(Prijatelj) # Kličemo funkcijo "dodaj_prijatelja", ki ji podamo zahtevano vrednost. Kliče se seveda na isti način, kot zgornja razredna funkcija z edino razliko, da funkcija od nas zahteva vrednost.

print(moja_oseba) # Ponovni izpis vseh vrednosti, ki jih ima naša kopija razreda