def kreis_flaeche(r):
    return r * r * math.pi

// Volumen eines Zylinders berechnen
def zylinder_vol(r, h):
    return kreis_flaeche(r) * h

// Oberfläche einer Kugel berechen
def kugel_oberflaeche(r):
    return 4 * kreis_flaeche(r)

// Oberfläche einer Halbkugel berechnen
def hemisphere_oberflaeche(r):
    return kugel_oberflaeche(r) / 2 + kreis_flaeche(r)
