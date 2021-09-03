def kreis_flaeche(radius, pi):
    return radius * radius * pi


# Hauptprogram:
pi = 3.14159265359
radius = 20.5
# A=pi*r^2
print(
    "Der Flächeninhalt eines Kreises mit Radius "
    + str(radius) + " cm ist "
    + str(kreis_flaeche(radius, pi)) + " cm^2"
)
