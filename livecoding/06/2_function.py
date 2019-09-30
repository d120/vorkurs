def lies_zahl(n):
    print("Zahl eingeben: ")
    zahl = float(input(""))
    print("Zahl eingelesen!")
    return zahl

n_zahlen = int(input("Wie viele Zahlen sollen gelesen werden? "))
zahlen = []  # Speichert alle Zahlen

if n_zahlen > 0::
    for i in range(n_zahlen):
        zahlen.append(lies_zahl(n_elemente))
        
    print("Fertig!")
    
    # Berechne summe
    summe = 0
    for zahl in zahlen:
        summe += zahl
        
    print("Summe: " + str(summe))
else:
    print("Ungültige Eingabe!")
