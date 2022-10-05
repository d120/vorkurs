# hier die Werte eintragen
wettervorhersage = "regen"
temperatur = 27
luftfeuchtigkeit = "hoch"
windig = True
# Die Zahlenwerte, gegen die verglichen wird,
# können von den hier eingetragenen abweichen.
# Eure Lösung kann auch anders vorgehen, wenn die Testdaten
# korrekt erkannt werden, stimmt sie wahrscheinlich trotzdem.
if wettervorhersage == "regen":
    freibad = False
elif temperatur > 24:
    freibad = True
elif wettervorhersage == "sonnig":
    freibad = not (temperatur < 18 and windig)
else:
    freibad = temperatur >= 18 and not windig

if freibad:
    print("Geh ins Freibad")
else:
    print("Bleib zu Hause")
