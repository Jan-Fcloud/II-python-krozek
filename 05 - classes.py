"""
Class/razred, si lahko predstavljamo kot načrt za hišo.
Hiša ima en načrt, ampak lahko naredimo več hiš iz enega načrta in vsaka hiša ima svoje specifične manjše spremembe.

Podobno gre za razrede v programiranju.

Razred se definira z naslednjo sintakso:

class <ime_razreda>:
    def __init__(self):
        <spremenljivke>

Naredimo razred Avto, ter si poglejmo glavne stvari razredov:
"""

class Avto: # Definiramo nov razred Avto
    def __init__(self): # funkcija __init__ se zažene vedno, ko inicializiramo instancno razreda (več v naslednji točki)
        # Spremenljivke definiramo s sintakso: self.<ime_spremenljivke> = <vrednost>
        self.znamka = ""
        self.prevozeno = 0
        self.letnik = 0

"""
V zgornjem primeru, smo definirali razred, nove spremenljivke znotraj __init__(), ter jim dali prvotne vrednosti.

Kako pa uporabimo razrede? Poglejmo kako razred inicializirati:
"""

instanca_razreda = Avto() # Inicializiramo instanco Avta v spremenljivko instanca_razreda

"""
Do vseh spremenljivk v razredu, lahko dostopamo z piko. Npr:
nas_avto.ime = "Audi"
"""

instanca_razreda.prevozeno = 100000 # Dostopamo do spremenljivke, ki je v naši spremenljivki znotraj razreda

"""
V zgornjem primeru razreda, smo določili spremenljivke, itd.
Kaj pa če želimo že ob inicializaciji vstaviti vrednosti?
To se naredi na podoben način kot da bi poljubni funkciji določali parametre ki jih sprejme.

Poglejmo si kako:
"""

class Oseba: # Definiramo nov razred Oseba
    def __init__(self, ime, starost): # dodamo ime in starost znotraj init funkcije
        self.ime = ime # vrednost se takoj zapise ob inicializaciji
        self.starost = starost # vrednost se takoj zapise ob inicializaciji

nova_instanca = Oseba("Jan", 21) # Inicializiramo novo instanco s podatki, namesto da so oklepaji prazni, saj __init__ pričakuje, da mu podamo vrednosti

"""
Pri obeh razredih ki smo jih ustvarili, vidimo besedo self v vsaki funkciji. Kaj pa sploh je self?

Sintaksa self, je potrebna biti napisana kot prvi parameter vsake funkcije razreda, saj pomeni da razred naslavlja samega sebe v svoji instanci.

Vzemimo si kot primer razred Oseba od zgoraj:
"""

oseba_1 = Oseba("Jan", 21)
oseba_2 = Oseba("Marko", 22)

print(oseba_1.ime) # Jan
print(oseba_2.ime) # Marko

"""
Beseda self, v obeh primerih deluje vsak na svojo instanco.

oseba_1 z self, pogleda vrednost v sebi in vidi da ima vrednost "Jan" v spremenljivki ime.
oseba_2, pa vidi da ima v isti spremenljivki vrednost "Marko".
"""

"""
Zdaj pa še poglejmo funkcijo __str__(), ki je kot __init__() že v naprej določena za razrede, ampak imamo možnost, da jo povozimo.

Kaj pa je naloga __str__? Funkcija je namenjena vračanju teksta takrat, ko razred obravnavamo kot tekst npr. print(oseba_1)
Za zdaj če želimo naš razred izpisat z print ukazom, nam ne vrne izpisa kot bi si ga želeli.

V naslednjem primeru bomo to spremenili tako, da se bo izpisalo <ime> - <starost>
"""

class OsebaNew:
    def __init__(self, ime, starost):
        self.ime = ime
        self.starost = starost

    def __str__(self): # definiramo funkcijo, ki ne dobi nobenih parametrov
        return self.ime + " - " + str(self.starost) # vrnemo ime, s pomišljajem, ter starostjo, ki smo jo mogli pretvorit iz int v string

oseba = OsebaNew("Jan", 21)

print(oseba) # Jan - 21

"""
V razrede lahko tudi dodamo svoje funkcije, ki bodo delovale za naš razred.

Dajmo definirat nov razred, ki preveri starost osebe in izpiše če je oseba polnoletna ali ne:
"""

class Osebe:
    def __init__(self, ime, starost):
        self.ime = ime
        self.starost = starost

    def __str__(self):
        return self.ime + " - " + str(self.starost)

    def polnoletnost(self): # Edino pomembno je, da mora self bit vedno parameter funkcije, da lahko dostopamo do naših vrednosti
        if self.starost >= 18:
            print("Oseba je stara nad 18 let")
        else:
            print("Oseba je stara pod 18 let")

test_oseba = Osebe("Majk", 30)

test_oseba.polnoletnost() # Oseba je stara nad 18 let"

test_oseba2 = Osebe("Miha", 17)

test_oseba2.polnoletnost() # Oseba je stara pod 18 let