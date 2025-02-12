"""
V tem primeru bomo naredili preprosto igro "Križci in krožci" v Pythonu.
"""

# Ustvarimo igralno polje kot seznam seznamov
polje = [[" " for _ in range(3)] for _ in range(3)] # Polje vsebuje 3 vrstice in 3 stolpce, vse napolnjene z " " (prosto polje)
# Vizualizacija polja:
#       0      1      2       
# 0 [0][0] [0][1] [0][2]
#  
# 1 [1][0] [1][1] [1][2]
#    
# 2 [2][0] [2][1] [2][2]

# Polje zgoraj, se zgenerira samodejno. Lahko pa bi ga naredili tudi ročno:
# polje = [
#     [" ", " ", " "],
#     [" ", " ", " "],
#     [" ", " ", " "]
# ]


def izpisi_polje():
    """Funkcija za izpis igralnega polja"""
    print("\n     0   1   2") # Presledki v VSEH izpisih, so namnjeni preglednosti.
    print("   +---+---+---+")
    for i in range(3):
        print(f" {i} | {polje[i][0]} | {polje[i][1]} | {polje[i][2]} |") # Izpis polja, kjer je i vrstica, polje[i][0] je prvi stolpec, polje[i][1] je drugi stolpec, polje[i][2] je tretji stolpec.
        print("   +---+---+---+")


def preveri_zmago():
    """Preveri ali je kdo zmagal"""
    # Preveri vrstice
    for i in range(3): # gremo po vseh vrsticah, in preverimo, če je v vrstici enaka vrednost v vseh treh poljih.
        if polje[i][0] == polje[i][1] == polje[i][2] != " ": # Če je vrstica enaka, in vrednost v poljih ni " ", potem je igralec zmagal.
            return True
    
    # Preveri stolpce
    for i in range(3): # gremo po vseh stolpcih, in preverimo, če je v stolpcu enaka vrednost v vseh treh poljih.
        if polje[0][i] == polje[1][i] == polje[2][i] != " ": # Če je stolpec enak, in vrednost v poljih ni " ", potem je igralec zmagal.
            return True
    
    # Preveri diagonale
    if polje[0][0] == polje[1][1] == polje[2][2] != " ":
        return True
    if polje[0][2] == polje[1][1] == polje[2][0] != " ":
        return True
    
    return False


def je_polje_polno(): # Funkcija pomaga pri preverjanju, če ni zmage ampak je polje polno.
    """Preveri ali je polje polno"""
    for vrsta in polje:
        if " " in vrsta: # Če je v polju še kakšno prosto polje, potem je polje še ni polno.
            return False
    return True


def igraj():
    """Glavna funkcija igre"""
    igralec = "X" # Prvi igralec je "X"
    
    while True: # Zanka se izvaja, dokler igralec ne zmaga ali dokler polje ni polno.
        print("\n" + "="*40)
        izpisi_polje()
        print(f"\nNa vrsti je igralec {igralec}")
        
        try: # Uporabljamo try, v primeru, da igralec vpiše nekaj neveljavnega.
            vrstica = int(input("Vpiši številko vrstice (0-2): "))
            stolpec = int(input("Vpiši številko stolpca (0-2): "))
            
            if vrstica < 0 or vrstica > 2 or stolpec < 0 or stolpec > 2: # Če igralec vpiše številko, ki ni med 0 in 2, potem je neveljavna pozicija.
                print("\n❌ Neveljavna pozicija! Izberi številke med 0 in 2.")
                continue # continue nas vrne na začetek zanke, da igralec lahko izbere novo pozicijo. To pomeni, da se koda od spodaj ne izvede ob tem klicu.
                
            if polje[vrstica][stolpec] != " ": # Če igralec vpiše pozicijo, ki je že zasedena, potem je neveljavna pozicija.
                print("\n❌ To polje je že zasedeno! Izberi drugo.")
                continue
                
            polje[vrstica][stolpec] = igralec # V primeru, da pridemo na ta klic, skelpamo, da so vse podatki pravilni in ni napak. Za to lahko vpišemo igralca v polje.
            
            if preveri_zmago(): # Vedno preverimo, če je igralec zmagal.
                print("\n" + "="*40)
                izpisi_polje()
                print(f"\n🎉 Igralec {igralec} je zmagal! 🎉")
                break
                
            if je_polje_polno(): # Vedno preverimo, če je polje polno.
                print("\n" + "="*40)
                izpisi_polje()
                print("\n🤝 Igra je neodločena! 🤝")
                break
                
            igralec = "O" if igralec == "X" else "X" # V naslednji zanki bo igralec drugi igralec. (Če je igralec X, potem je drugi igralec O in obratno.)
            
        except ValueError: # V primeru, da igralec vpiše nekaj neveljavnega, se izvede ta klic.
            print("\n❌ Prosim vpiši številko!")
            continue # vrnemo se na začetek zanke, da igralec lahko izbere novo pozicijo.

# Začni igro
if __name__ == "__main__": # if __name__ == "__main__": se izvede samo, če je program izveden direktno, ne pa če je importiran.
    # Izpisovanje naslova igre in igre.
    print("\n" + "="*40)
    print("🎮 Dobrodošli v igri Križci in krožci! 🎮")
    print("="*40)
    igraj()
