"""
V tem primeru bom naredil prazen Array/List, v katerega bomo nenehno vpisovali vrednosti, dokler naš vnos nebo "STOP"
"""

moj_list = []

while True: # while True, deluje neskončno in je lahko samo prekinjen s sintakso/besedo "break"
    vnos = input("Vnos: ") # Zahtevamo vnos uporabnika.
    if vnos == "STOP": # Če je naš vnos enak "STOP" se program konča
        break
    moj_list.append(vnos) # Z .append, dodamo vrednost v list
    print(moj_list) # Po vsakem vnosu izpišemo list, da vidimo vse vrednosti, ki so bile dodane do zdaj.

print("Konec programa") # Naslednje se izvede izključno takrat, ko se while zanka konča.