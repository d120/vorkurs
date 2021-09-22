liste = [1, 2, 3, 4, 5, 6, 7]

summe = 0
produkt = 1
quadrate = []

for zahl in liste:
    summe += zahl
    produkt *= zahl
    quadrate.append(zahl * zahl)

print(summe)
print(produkt)
print(summe / len(list) if liste else "Leere Liste!")
print(quadrate)
