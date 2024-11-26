"""
Z spremenljivkami se bomo obadali v bistvu konstantno, saj so del vsakega projekta da se podatki lahko shranjujejo, zamenjujejo, itd.

Imamo naslednje splošne tipe podatkov:

- String                / str: "Tekst", 'Še več teksta', '2', ... (vedno se začne z nekakšnimi narekovaji in je vse znotraj obravnavano kot znak ali skupek znakov)
- Integer               / int: 1, 50, 21684, 1212 (cela števila)
- Floating point number / float: 3.14, 1.1, 1.00005 (decimalna števila)
- Boolean               / bool: True, False (ja ali ne. Drugega ni. Pomembne so velike črke. To pomeni da ne obstaja true ali false, ampak samo True in False)

Spremenljivke kreiramo tako, da določimo ime, ter po = določimo prvotno vrednost (če jo vemo):
"""

# Izpisali bomo vrednost z funkcijo print()

spr_1 = "Tekst v spremenljivki" # str
spr_2 = 2024 # int
spr_3 = 3.14 # float
spr_4 = True # bool

print(spr_1) # Tekst v spremenljivki
print(spr_2) # 2024
print(spr_3) # 3.14
print(spr_4) # True

"""
Vrednosti lahko seveda tudi sproti spreminjamo tako, da samo napišemo ime spremenljivke ki še obstaja in ji določimo nekaj drugega:
"""

spr_za_spremenit = 5
print(spr_za_spremenit) # 5

spr_za_spremenit = 555
print(spr_za_spremenit) # 555

"""
Težava pri spremenljivkah je, da sprejmejo vse tipe podatkov, kar pomeni da lahko prvo določimo število, nato pa zamenjamo z tekstom v isti spremenljivki,
kar ni dobro v praksi. Zato imamo tudi opcijo določiti tipe v naprej preden nastavimo prvotno vrednost.

To naredimo tako, da prvo spet napišemo poljubno ime spremenljivke, ampak namesto =, uporabimo :, ter za tem napišemo kratico željenega tipa:
"""

spr_stevilo : int # spremenljivka še nima vrednosti, ampak smo ji določili, da sprejema samo cela števila.

spr_stevilo = 100
print(spr_stevilo) # 100

# Dobro je za vedet, da nam to ne prepreči ničesar, temveč nam pomaga v smislu, da nas naše orodje opozori, da to nebo v redu z našim planom.