"""
Naredite razred "Oseba", ki vsebuje naslednje vrednosti:
- ime
- starost
- denar,
- list, ki bo hranil imena prijateljev osebe (naj bo prvotno prazen).

1. Parametri inicializacije razreda (__init__), so naj brez lista, znotraj funkcije pa vseeno definirajte prazen list.

2. V razredu napišite funkcijo, ki kot parameter dobi text, ki predstavlja ime prijatelja, ter se doda v list prijateljev razreda (za vnos je input()).

3. V glavnem programu (izven razreda) naredite while zanko, ki nenehno kliče funkcijo za vpis prijatelja in neha samo če bo vaš vpis STOP.

4. Razredu dodajte funkcijo, ki izpiše "<ime> je star/a več kot 21" ali pa, da ni. To se zve z atributom starost vašega razreda.

5. Razredu podrite __str__ funkcijo, ter jo napišite tako, da izpiše naslednje:
    <ime>, je star/a <starost>, ima <denar>€ in ima <list.count()> prijateljev

    P.S:
        - Če napišemo ime lista, ter dodamo zraven .count(), nam python vrne število elementov v listu.
"""