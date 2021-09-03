matrix = []
for zeile in range(10):
    spaltenliste = []
    for spalte in range(10):
        spaltenliste.append(spalte * zeile)
    matrix.append(spaltenliste)
print(matrix)

# Ausgabe
for zeile in matrix:
    reihenstring = ""
    for spaltenelement in zeile:
        reihenstring += str(spaltenelement) + " "

    print(reihenstring)
