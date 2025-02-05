"""
V prejšnji lekciji, smo si ogledali, kako lahko beremo iz JSON datotek in v njih tudi pišemo.

Zdaj pa si bomo pogledali, kako lahko dobimo podatke iz spletnih strani.
Za to bomo uporabili requests modul.

Podatki, ki jih dobimo iz spletnih strani, so lahko v JSON formatu, HTML formatu, XML formatu, itd.

V tem primeru, bomo si pogledali, kako lahko dobimo podatke iz JSON formatnega APIja.

API je spletni programski vmesnik, ki omogoča, da dobimo podatke iz spletnih strani.

"""

import requests # uvozimo requests modul

response = requests.get("https://jsonplaceholder.typicode.com/posts/1") # dobimo podatke iz spletnih strani

print(response.json()) # izpišemo podatke iz spletnih strani v JSON formatu

# Uporabljanje dobljenih podatkov, je enako kot pri JSON datotekah, ki smo jih obravnavali v prejšnji lekciji.


