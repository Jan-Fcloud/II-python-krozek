"""
Govorili smo že o funkcijah, kako jih definiramo, kako jim dodajamo parametre, kako jih nastavimo tako, da vračajo vrednosti, itd.

Poglejmo si klicanje funkcij malo bolj podrobno.
"""

# --------------------------------------------------------------------
# 1. Funkcija, ki nič ne sprejema in nič ne vrača:

def test_funkcija(): # Funkciji je ime "test_funkcija", ki nima nobenih parametrov, saj ima prazne oklepaje.
    print("TEST") # Funkcija samo izpiše "TEST"

test_funkcija() # Pokličemo funkcijo tako, da znova napišemo njeno ime, ter dodamo oklepaje po imenu. (Izpis: TEST)
# --------------------------------------------------------------------


# --------------------------------------------------------------------
# 2. Funkcija, ki nekaj sprejme, ampak nič ne vrača:

def spr_funkcija(vnos): # Funkciji je ime "spr_funkcija", ki ima en parameter z imenom "vnos".
    print(vnos) # Funkcija izpiše to, kar ji podamo

spr_funkcija("IZPISAL BI RAD TA TEXT") # Vrednost, ki je znotraj oklepajev, se prenese v funkcijo, pod imenom "vnos" (Izpis: IZPISAL BI RAD TA TEXT)

# --------------------------------------------------------------------


# --------------------------------------------------------------------
# 3. Funkcija, ki nekaj sprejme in nekaj vrne:

def mat_funkcija(ena, dva): # Funkciji je ime "mat_funkcija", ki ima dva parametra z imeni "ena" in "dva"
    return ena + dva # tokrat ne izpisujemo, ampak vračamo neko vrednost, z besedo "return"

rezultat = mat_funkcija(1,2) # Tokrat prenesemo v funkcijo dve vrednosti. Ločimo jih z vejico. Rezultat, ki ga dobimo od funkcije, shranimo v spremenljivko "rezultat".
print(rezultat) # Izpis: 3

# --------------------------------------------------------------------

"""
Vse zgornje funkcije, obstajajo v našem glavnem programu in jih lahko kličemo vsepovsod.

Zdaj pa še poglejmo funkcije znotraj razredov:
"""

# --------------------------------------------------------------------
# 3. Funkcije znotraj razredov:

class Avto: # Ustvarimo razred "Avto"
    def __init__(self, ime, prevozeno): # __init__ funkcija, se zažene vedno ob kreiranju funkcije (npr: avto = Avto("BMW", 10000000) -> po tem, se avtomatsko kliče __init__)
        self.ime = ime # razred ima spremenljivko "ime"
        self.prevozeno = prevozeno # razred ima spremenljivko "prevozeno"

    def dosti_prevozeno(self): # Ustvarimo svojo poljubno funkcijo znotraj razreda, z imenom "dosti_prevozeno", ki od nas ne sprejme ničesar. Vsaka funkcija znotraj razreda MORA imeti kot prvi parameter "self".
        if self.prevozeno > 200000: # Če je prevoženo več kot 200.000, se izpiše spodnje.
            print("Dosti prevoženo!")

    def dodaj_prevozeno(self, km): # Ustvarimo novo poljubno funkcijo "dodaj_prevozeno", ki od nas sprejme eno vrednost, ki se shrani pod "km". Tako kot prej, MORA funkcija znotraj razreda imeti prvi parameter "self".
        self.prevozeno += km # K prevoženemu dodamo vrednost, ki je shranjena znotraj parametra "km"

moj_avto = Avto("BMW", 300200) # Iz zgornjega razreda, kreiramo novo kopijo razreda Avto, z vrednostmi, ki smo jih podali znotraj oklepajev.

moj_avto.dosti_prevozeno() # Kličemo funkcijo "dosti_prevozeno", ki samo obstaja znotraj našega razreda. Pokliče se z imenom spremenljivke, ki hiši našo kopijo razreda, ter s piko in imenom naše funkcije.

moj_avto.dodaj_prevozeno(2000) # Kličemo funkcijo "dodaj_prevozeno", ki ji podamo zahtevano vrednost. Kliče se seveda na isti način, kot zgornja razredna funkcija z edino razliko, da funkcija od nas zahteva vrednost.

# --------------------------------------------------------------------