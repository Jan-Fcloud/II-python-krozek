"""
Do zdaj poznamo osnovne spremenljivke. Zdaj si pa poglejmo nekaj naprednejših.

Pogledali si bomo:
- Array      / niz
- List       / list
- Dictionary / slovar

-----------------------------------------------------------------
!!  V Python-u lahko sklepamo Array in List kot ista stvar   !!
!! (Po vseh nalogah bomo od zdaj naprej ta dva klicali List) !!
-----------------------------------------------------------------

Do sedaj, smo spremenljivke shranjevali eno po eno. Kot npr:
ena = 1
dva = 2

itd...

Z naslednjimi primeri pa lahko shranjujemo več vrednosti (istih ali različnih tipov) v eno spremenljivko.
Začnimo z Listo:
"""

# Prazen List:
moj_list = [] # List se kreira z [ in ]

# List z vrednostmi:
drugi_list = [25, 15, 8, 7, 3, 3, 2] # list z int
tretji_list = [True, False, False, True, True] # list z bool
cetrti_list = ["ja", "ne", "avto", "voznik"] # list z string

peti_list = [15, "dfsd", True] # mešan list

"""
Listi imajo možnost neskončno število vrednosti.
Kako pa sploh do stopamo do naših vrednosti?

Do vrednosti, do stopamo z indeksi (mesti vrednosti):
"""

nov_list = ["vr", "ed", "nost", "python"]
print(nov_list[3]) # "python"

"""
V zgornjem primeru smo do stopali do zadnje (četrte) vrednosti tako, da smo napisali ime liste, ter v oglatih oklepajih podali naš indeks/mesto vrednosti.

Ampak če so štiri vrednosti, zakaj smo podali število 3, da smo izpisali četrto?
To je zato, ker se indeks začne z 0 in ne z 1.

Poglejmo zgornji list in izpišimo indekse:

nov_list = ["vr", "ed", "nost", "python"]:
--------------------
| INDEX - VREDNOST |
|   0   -    vr    |
|   1   -    ed    |
|   2   -   nost   |
|   3   -  python  |
--------------------

V primeru, da do stopamo z indeksom, ki ne obstaja, nam python vrne error!

Listi nam tudi omogočajo dodajanje in odvzemanje vrednosti. To pomeni, da so listi dinamični:
"""
za_dodat = [1,2]

print(za_dodat) # [ 1, 2 ]

za_dodat.append(3) # append / dodajanje vrednosti
za_dodat.append(55)

print(za_dodat) # [ 1, 2, 3, 55 ]

za_dodat.remove(55) # remove / odstranjevanje vrednosti

print(za_dodat) # [ 1, 2, 3 ]

za_dodat.__delitem__(0) # __delitem__ nam omogoči odstranjevanje vrednosti na nekem indeksu namesto, da mu povemo točno vrednost

print(za_dodat) # [ 2, 3 ]

"""
                       !!!
         Obstaja še več funkcij pri listih.
        Če želite imeti razlage vseh, povejte.
                       !!!
                       
                       
Zdaj pa si še poglejmo slovarje. Predstavljamo si jih lahko podobno kot liste, samo z večjo funkcionalnostjo.
Med seboj imata nekaj razlik pri inicializaciji:
"""

# List ima indekse
pr_list = [15, 65, 78] # List se inicializacija z []
print(pr_list[0]) # 15 -> List ima indekse

# Slovar ima ključe
pr_slovar = {15, 65, 75} # Slovar se inicializacija z {}
print(pr_slovar) # 15 -> Slovar ima ključe (v tem primeru jih nismo določili, zato ne gre direktno do stopat do vrednosti. Če poskusimo, dobimo ERROR)

pr_slovar2 = { # Definiramo vrednost: <ključ> : <vrednost>
    1 : 15, # dodamo vejico, če želimo več vrednosti
    2 : "vrednost",
    3: True,
    "ključ" : 55, # ključi so lahko katerekoli vrednosti
    False: 3
}

print(pr_slovar2[2]) # "vrednost"
print(pr_slovar2["ključ"]) # 55
print(pr_slovar2[False]) # 3

"""
Tako kot rečeno, obnašanje slovarja je podobno listu samo, da namesto indeksov, imamo ključe.
Če želimo dodati ključ in vrednost v slovar, naredimo naslednje:
"""

pr_slovar2["dodano"] = 100 # Enostavno znotraj oglatih oklepajev napišemo nov ključ, katerega bo Python dodal, če ne obstaja. Če pa obstaja, pa se vrednost samo spremeni.
print(pr_slovar2["dodano"]) # 100

"""
Ključi so UNIKATNI. To pomeni, da se v enem slovarju ključ ne sme podvajati. Če se, dobimo ERROR.

Slovarji imajo tudi svoje funkcije, kot listi, kot npr __delitem__:
"""

test_slovar = {
    "ena" : True,
    "dva" : True,
    "tri" : True,
    "zbrisi" : False,
}

print(test_slovar) # {'ena': True, 'dva': True, 'tri': True, 'zbrisi': False}

test_slovar.__delitem__("zbrisi")

print(test_slovar) # {'ena': True, 'dva': True, 'tri': True}

"""
                       !!!
        Obstaja še več funkcij pri slovarjih.
        Če želite imeti razlage vseh, povejte.
                       !!!
"""