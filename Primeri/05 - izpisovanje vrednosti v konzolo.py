"""
Do zdaj smo izpisovali vrednosti spremenljivk in jih ločevali s presledkom tako:
"""

sp1 = "text"
sp2 = 10
sp3 = True

print(sp1 + " " + str(sp2) + " " + str(sp3)) # Vse kar ni text, je bilo treba pretvoriti v text.

"""
V Pythonu obstaja več načinov, kako izpisati vrednosti spremenljivk v konzolo.
"""

# 1. način:
print(sp1, sp2, sp3) # Vse vrednosti, ki želimo izpisati, ločimo s vejico. Ker ne kombiniramo vrednosti v en string, ne potrebujemo funkcij za pretvarjanje v text.


# 2. način:
print(sp1 + " " + str(sp2) + " " + str(sp3)) # Vse vrednosti, ki želimo izpisati, ločimo s presledkom, ter jih pretvorimo v text. če še ni. Na koncu se združi vse v en string.


# 3. način:
print(f"{sp1} {sp2} {sp3}") # 3. način je podoben 2. načinu, le da je zapis malo drugačen, bolj pregleden in lažji.
# Pred narekovajem stavka pišemo f, kar pomeni formatiran tekst. V narekovaju stavka pišemo vrednosti spremenljivk, ki jih želimo izpisati, z znakom {}.


# 4. način:
print("{} {} {}".format(sp1, sp2, sp3)) # 4. način deluje isto, kot 3. Razlika je v tem, da spremenljivke niso napisane znotraj samega izpisa, ki ga želimo prikazati, temveč postavimo znak {} na mesto, kjer želimo izpisati našo spremenljivko. Na koncu pa z funkcijo format() povežemo vse vrednosti.
