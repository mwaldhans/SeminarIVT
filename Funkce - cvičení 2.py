cena_bez_dph = 1000
dph_procento = 21
vysledna_cena = 0

def spocitej_dph():
    global vysledna_cena
    vysledna_cena = cena_bez_dph * (1 + dph_procento / 100)

spocitej_dph()
print(f"Konec: {vysledna_cena} Kč")