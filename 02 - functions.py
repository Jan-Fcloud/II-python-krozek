"""
Poglejmo si osnove funkcij.

Funkcije so skupki navodil/kode, ki se lahko uporabijo večkrat, da preprečimo copy/paste pisanja zaporedne kode.

V prejšni datoteki smo uporabili že eno funkcijo, ki se imenuje print.
Ta funkcija je namenjena izpisovanju vrednosti v konzolo:
"""

print("Rad bi ta tekst izpisal")  # Rad bi ta tekst izpisal
print(232323)  # 232323

spr_za_izpis = 3.14
print(spr_za_izpis)  # 3.14

"""
Kaj pa če bi radi ustvarili svojo funkcijo, ki jo bomo lahko klicali v svojem programu?

To naredimo z ključno besedo (oz. sintakso) def
def -> ang. define, si. definiranje nečesar

Postopek je naslednji:
"""


def moja_funkcija():  # def <poljubno_ime>():
    return 2  # return vrne poljubno vrednost, ki jo lahko ob klicu funkcije shranimo v spremenljivko


"""
In tako smo že določili svojo funckijo, ki se imenuje moja_funkcija.

Zraven tega pa še imamo () in :

 ()      - oklepaji so OBVEZNI. Tukaj so da znotraj njih definiramo če bo naša funkcija kaj dobila. V primeru da ne, pustimo oklepaje prazne.
 :       - dvopičje pove Pythonu da bodo naslednje vrstice (ki so zamaknjene za eno v desno), predstavljale celotno dogajanje znotraj naše funkcije.
 return  - sintaksta return, pomeni da funkcija nekaj vrne, kar lahko naprej uporabimo v glavnem programu.
 
Za vajo bomo ustvarili funkcijo ki sešteje in vrne 2+2, nakar bomo rezultat izpisali:
"""


def sestej():
    return 2 + 2 # vrnemo rezultat 2+2


sestevek = sestej() # ker funkcija nekaj vrne, lahko shranimo v spremenljivko -> <ime_spr> = <ime_funkcije>()

print(sestevek)  # 4


"""
Zdaj pa še dodajmo funkcionalnost, ki nam omogoča seštevanje dveh poljubnih števil:
"""

def sestej_poljubno(st1, st2): # st1 in st2 predtavljata imena stevil ki jih bomo funkciji podali
    return st1 + st2

sestevek = sestej_poljubno(15, 200) # poklicemo funkcijo in ji podamo stevilo 15 (ki se shrani v st1) in stevilo 200 (ki se shrani v st2). Funkcija vrne sestevek teh dveh stevil.

print(sestevek) # 215