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
else:
    if temperatur > 24:
        freibad = True
    else:
        if wettervorhersage == "sonnig":
            if temperatur < 18 and windig:
                freibad = False
            else:
                freibad = True
        else:
            if temperatur >= 18 and not windig:
                freibad = True
            else:
                freibad = False

if freibad:
    print("Geh ins Freibad")
else:
    print("Bleib zu Hause")
