"""
Napake so del programiranja, ki jih programerji poznajo in jih obravnavajo.

Napake se delijo na:
- Syntax errors - Napake v kodi, ki preprečijo programu, da se izvede.
- Runtime errors - Napake, ki se pojavijo, ko se program izvaja.
- Semantic errors - Napake v logiki programa.
"""

# Primer syntax error:
print("Hello, world!) 
      # V kodi manjka narekovaj.

# Primer runtime error:
print(1 / 0) 
    # V kodi se deli z 0, kar je napaka.

# Primer semantic error:
x = 1

if x == 1:
    print("x je 1") 
elif x == 2:
    print("x je 2")
else:
    print("x ni 1 ali 2")
    # V kodi je logična napaka, saj je x vedno enak 1.

"""
Napake se obravnavajo z try in except stavki.

try:
    # Koda, ki se izvede.
except:
    # Koda, ki se izvede, če pride do napake.
finally:
    # Koda, ki se izvede, če pride do napake ali ne.

Poglejmo si primer z napako pri deljenju z 0.
Drugih ni mogoče izvesti, saj je napaka v kodi.
"""

try: # Poskusimo izvesti kodo.
    print(1 / 0)
except: # Če pride do napake, izvedi kodo.
    print("Napaka pri deljenju z 0")
finally: # Če pride do napake ali ne, izvedi kodo.
    print("Koda je bila izvedena")


