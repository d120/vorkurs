def kreis_flaeche(r):
    return r * r * math.pi

// Hauptprogramm
radius: float = 20.5
print(
    "Der Flächeninhalt eines Kreises mit Radius $radius" +
    " cm ist {} cm^2".format(kreis_flaeche(radius))
)
