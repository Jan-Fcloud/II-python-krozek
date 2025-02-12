
def glavna_funkcija():
    """Glavna funkcija, ki se izvede, ko je program izveden direktno."""
    print("Pozdravljeni v naši knjiznici!")
    print(__name__)


if __name__ == "__main__": # V primeru, da je program izveden direktno, se izvede ta klic. Drugače pa se ne izvede, če je program uvozil našo knjiznico.
    glavna_funkcija()
    
""" 
Vrednost __name__ je ime datoteke, ki je bila izvedena.
Če pa je program direktno izveden, potem je __name__ "__main__".
"""