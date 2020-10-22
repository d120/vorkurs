fak = int(input("Welche Fakultaet soll berechnet werden: "))
erg = 1

for i in range(1, fak + 1):
    erg *= i

print("Die {0}. Fakultaet ist {1}".format(fak, erg))
