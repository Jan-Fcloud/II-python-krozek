"""
Imamo razred "Knjiga", ki ima tri atribute: "naslov", "avtor" in "leto_izdaje".

Naredili bomo zanka, ki bo v loopu vprašala po naslovu, avtorju in letu izdaje knjige.

Nato pa bomo v loopu kreirali novo kopijo razreda "Knjiga" z vrednostmi, ki smo jih podali znotraj loopa.

Vpisovanje knjig se bo zaključilo, ko bomo vpisali "KONEC".
"""

knjige = [] # Ustvarimo list, ki bo vseboval vse kopije razreda "Knjiga".

def check_input(prompt): # Funkcija, ki preveri, če je vpisana vrednost "KONEC". Če je, se vrne None, sicer pa se vrne vrednost.
        value = input(prompt)
        if value == "KONEC":
            return None
        return value

class Knjiga:
    def __init__(self, naslov, avtor, leto_izdaje): # Funkcija, ki kreira novo kopijo razreda "Knjiga" z vrednostmi, ki smo jih podali znotraj loopa.
        self.naslov = naslov
        self.avtor = avtor
        self.leto_izdaje = leto_izdaje

    def __str__(self): # Funkcija, ki vrne vrednosti razreda "Knjiga" v obliki stringa.
        return f"{self.naslov} ({self.leto_izdaje}) - {self.avtor}"


while True:
    knjiga = ["", "", ""] # Ustvarimo list, ki bo vseboval vrednosti, ki jih bomo podali znotraj loopa.
    vrednosti = ["naslov", "avtor", "leto_izdaje"]
    
    for i in range(3): # Loop, ki se izvede 3-krat, saj imamo 3 vrednosti, ki jih bomo podali.
        knjiga[i] = check_input(f"Vnesi {vrednosti[i]} knjige: ") # V loopu kličemo funkcijo "check_input", ki preveri, če je vpisana vrednost "KONEC". Če je, se vrne None, sicer pa se vrne vrednost.
        if knjiga[i] is None: # Če je vrednost "KONEC", se iz loopa izlomi.
            break

    if None in knjiga: # Če je vrednost None v listu "knjiga", se iz loopa izlomi.
        break

    knjiga = Knjiga(knjiga[0], knjiga[1], knjiga[2]) # Ustvarimo novo kopijo razreda "Knjiga" z vrednostmi, ki smo jih podali znotraj loopa.
    knjige.append(knjiga) # Dodamo novo kopijo razreda "Knjiga" v list "knjige".

print("Vse vpisane knjige:")

for knjiga in knjige: # Loop, ki se izvede za vsako kopijo razreda "Knjiga" v listu "knjige".
    print(knjiga)
