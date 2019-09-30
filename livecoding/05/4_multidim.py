matrix = []
for zeile in range(10):
    spaltenliste = []
    for spalte in range(10):
        spaltenliste.append(spalte * reihe)
    matrix.append(spaltenliste)
print(matrix)

# Ausgabe
for reihe in matrix:
    reihenstring = ""
    for spaltenelement in reihe:
        reihenstring += str(spaltenelement) + " "
        
    print(reihenstring)

        
