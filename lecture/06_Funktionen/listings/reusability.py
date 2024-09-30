def kreis_flaeche(r):
    return r * r * math.pi
def zylinder_vol(r, h):  # Volumen eines Zylinders
    return kreis_flaeche(r) * h
def kugel_oberflaeche(r):  # Oberfläche einer Kugel
    return 4 * kreis_flaeche(r)
def hemisphere_oberflaeche(r):  # Oberfläche einer Halbkugel
    return kugel_oberflaeche(r) / 2 + kreis_flaeche(r)
