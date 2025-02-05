"""
Tukaj si bomo kako lahko beremo iz JSON datotek.

JSON datoteke so podobne Pythonovim slovarjem, saj imajo ključe in vrednosti.

"""

import json # prvo je vedno treba uvoziti json modul, ki nam omogoča, da lahko pravilno beremo in pišemo JSON datoteke.

# Naša JSON datoteka, je bila vzeta iz https://www.geeksforgeeks.org/read-json-file-using-python/

with open("sample.json", "r") as datoteka: # odpremo datoteko, ki jo želimo brati.
    podatki = json.load(datoteka) # datoteko preberemo in jo shranimo v spremenljivko "podatki".

print(podatki) # Izpis:
# {'emp_details': [{'emp_name': 'Shubham', 'email': 'ksingh.shubh@gmail.com', 'job_profile': 'intern'}, {'emp_name': 'Gaurav', 'email': 'gaurav.singh@gmail.com', 'job_profile': 'developer'}, {'emp_name': 'Nikhil', 'email': 'nikhil@geeksforgeeks.org', 'job_profile': 'Full Time'}]}

"""
Vidimo, da je podatki shranjeni v slovarju, kjer ima ključ "emp_details" in vrednost list, kjer imajo posamezni elementi v listu še svoje ključe in vrednosti.

Če želimo izpisati vse vrednosti iz datoteke, lahko to naredimo tako, da izpišemo vse vrednosti iz slovarja:
"""

for podatek in podatki["emp_details"]: # gremo po vseh elementih v listu "emp_details"
    print(podatek) # izpišemo posamezni element v listu
# Izpis:
# {'emp_name': 'Shubham', 'email': 'ksingh.shubh@gmail.com', 'job_profile': 'intern'}
# {'emp_name': 'Gaurav', 'email': 'gaurav.singh@gmail.com', 'job_profile': 'developer'}
# {'emp_name': 'Nikhil', 'email': 'nikhil@geeksforgeeks.org', 'job_profile': 'Full Time'}

"""
Vidimo, da smo dobili vse vrednosti iz datoteke.

Do zdaj, smo videli, kako lahko beremo iz JSON datotek.
Zdaj pa si bomo ogledali, kako lahko slovar pretvorimo v JSON datoteko:
"""

slovar = { # glavni slovar
    "osebe": [ # kljuc slovarja je "osebe", vrednost je list
        { # prvi element v listu
            "ime": "Ana", # kljuc je "ime", vrednost je "Ana"
            "starost": 20, # kljuc je "starost", vrednost je 20
            "mesto": "Ljubljana" # kljuc je "mesto", vrednost je "Ljubljana"
        },
        {
            "ime": "Marko", 
            "starost": 25,
            "mesto": "Maribor"
        },
        {
            "ime": "Maja",
            "starost": 30, 
            "mesto": "Celje"
        }
    ]
}

with open("osebe.json", "w") as datoteka: # odpremo datoteko, ki jo želimo pisati.
    json.dump(slovar, datoteka) # shranimo slovar v datoteko.





