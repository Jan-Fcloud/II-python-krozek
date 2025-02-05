# ------------------------------------------------------------------------------
# split() funkcija:
# ------------------------------------------------------------------------------

"""
Do zdaj, smo dobivali vrednosti iz konzole eno po eno, ter jih shranjevali v spremenljivke.
V tem primeru, si bomo pogledali, kako lahko iz konzole dobimo več vrednosti hkrati.
"""

ime, starost = input("Vpiši ime in starost: ").split() # Primer vpisa: Ana 22
# Ime = Ana
# Starost = 22

print(ime, starost) # Izpis: Ana 22

"""
Kaj pa če bo naš vnos vseboval vrednosti s presledki in bi jih radi ločili?
V tem primeru, lahko podamo split() funkciji parameter z katerim funkciji povemo po čem želimo ločiti vrednosti.
"""

kraj, leto = input("Vpiši Kraj in leto: ").split(",") # Primer vpisa: Novo Mesto,2025
# Kraj = Novo Mesto
# Leto = 2025

print(kraj, leto) # Izpis: Novo Mesto 2025

"""
Poglejmo si še en primer split() funkcije. Tokrat z več vrednostmi, ki jih želimo ločiti.
"""

celoten_text = "ENA;DVA;TRI;ŠTIRI" # Ločimo vrednosti po ";"

print(celoten_text.split(";")) # Izpis: ['ENA', 'DVA', 'TRI', 'ŠTIRI']

# ------------------------------------------------------------------------------
# join() funkcija:
# ------------------------------------------------------------------------------

"""
Do zdaj smo videli, kako lahko iz konzole dobimo več vrednosti hkrati.
Zdaj pa si bomo ogledali, kako lahko več vrednosti, ki jih imamo v listu, združimo v en niz.
"""

seznam = ["ENA", "DVA", "TRI", "ŠTIRI"]

print(";".join(seznam)) # Izpis: ENA;DVA;TRI;ŠTIRI
# V niz smo združili vrednosti iz seznama, ločene z ";".

# ------------------------------------------------------------------------------
# replace() funkcija:
# ------------------------------------------------------------------------------

"""
Kaj pa če bi želeli v nizu spremeniti nekaj znakov?
V tem primeru, lahko uporabimo replace() funkcijo.
"""

niz = "ENA;DVA;TRI;ŠTIRI"

print(niz.replace(";", " ")) # Izpis: ENA DVA TRI ŠTIRI
# V nizu smo zamenjali ";" z " ".

# ------------------------------------------------------------------------------
# strip() funkcija:
# ------------------------------------------------------------------------------

"""
Kaj pa če bi želeli izbrisati presledke na začetku in na koncu niza?
V tem primeru, lahko uporabimo strip() funkcijo.
"""

niz = "   ENA   "

print(niz.strip()) # Izpis: "ENA"
# Izbrisali smo presledke na začetku in na koncu niza.

# ------------------------------------------------------------------------------
# find() funkcija:
# ------------------------------------------------------------------------------

"""
Kaj pa če bi želeli iz niza izluščiti nekaj posebnega?
V tem primeru, lahko uporabimo find() funkcijo.
"""

niz = "ENA;DVA;TRI;ŠTIRI"

print(niz.find("TRI")) # Izpis: 8
# V nizu smo poiskali prvo pojavitev "TRI" in dobili njegovo pozicijo (indeks).
# niz[8] = 'T'

# ------------------------------------------------------------------------------
# count() funkcija:
# ------------------------------------------------------------------------------

"""
Kaj pa če bi želeli prešteti kolikokrat se pojavi nekaj v nizu?
V tem primeru, lahko uporabimo count() funkcijo.
"""

niz = "ENA;DVA;TRI;ŠTIRI"

print(niz.count("TRI")) # Izpis: 1
# V nizu smo prešteli kolikokrat se pojavi "TRI".

# ------------------------------------------------------------------------------
# isalpha() funkcija:
# ------------------------------------------------------------------------------

"""
Kaj pa če bi želeli preveriti, če je niz sestavljen samo iz črk?
V tem primeru, lahko uporabimo isalpha() funkcijo.
"""

niz = "ENA"

print(niz.isalpha()) # Izpis: True
# Niz je sestavljen samo iz črk.

# ------------------------------------------------------------------------------
# isdigit() funkcija:
# ------------------------------------------------------------------------------

"""
Kaj pa če bi želeli preveriti, če je niz sestavljen samo iz številk?
V tem primeru, lahko uporabimo isdigit() funkcijo.
"""

niz = "123"

print(niz.isdigit()) # Izpis: True
# Niz je sestavljen samo iz številk.

# ------------------------------------------------------------------------------
# isalnum() funkcija:
# ------------------------------------------------------------------------------

"""
Kaj pa če bi želeli preveriti, če je niz alfanumeričen?
V tem primeru, lahko uporabimo isalnum() funkcijo.
"""

niz = "ENA123"

print(niz.isalnum()) # Izpis: True
# Niz je sestavljen samo iz črk in številk.

# Alfanumeričen niz:
# - sestavljen je iz črk in številk
# - niz ne sme imeti presledkov
# - niz ne sme imeti posebnih znakov

# ------------------------------------------------------------------------------
# islower() funkcija:
# ------------------------------------------------------------------------------

"""
Kaj pa če bi želeli preveriti, če je niz sestavljen samo iz malih črk?
V tem primeru, lahko uporabimo islower() funkcijo.
"""

niz = "ena"

print(niz.islower()) # Izpis: True
# Niz je sestavljen samo iz malih črk.

# ------------------------------------------------------------------------------
# isupper() funkcija:
# ------------------------------------------------------------------------------

"""
Kaj pa če bi želeli preveriti, če je niz sestavljen samo iz velikih črk?
V tem primeru, lahko uporabimo isupper() funkcijo.
"""

niz = "ENA"

print(niz.isupper()) # Izpis: True
# Niz je sestavljen samo iz velikih črk.

# ------------------------------------------------------------------------------
# isspace() funkcija:
# ------------------------------------------------------------------------------

"""
Kaj pa če bi želeli preveriti, če je niz sestavljen samo iz presledkov?
V tem primeru, lahko uporabimo isspace() funkcijo.
"""

niz = "   "

print(niz.isspace()) # Izpis: True
# Niz je sestavljen samo iz presledkov.


"""
String/tekst vsebuje ogromno funkcij, ki jih lahko uporabimo za manipulacijo z nizi.
Za več informacij o funkcijah, ki jih lahko uporabimo za manipulacijo z nizi, si lahko pogledate dokumentacijo python-a.

Link do dokumentacije: https://docs.python.org/3/library/stdtypes.html#string-methods
"""