# Volumen eines Zylinders berechnen
def zylinder_vol(r, h, pi):
    return kreis_flaeche(r, pi) * h


# Oberfläche einer Kugel berechen
def kugel_oberfl(r, pi):
    return 4 * kreis_flaeche(r, pi)


# Oberfläche einer Halbkugel berechnen
def hemisp_oberfl(r, h, pi):
    return kugel_oberfl(r, pi) / 2 + kreis_flaeche(r, pi)
