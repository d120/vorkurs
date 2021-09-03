lst = [1, 2, 3, 4, 5, 6, 7]

sum = 0
product = 1
quadrate = []

for zahl in lst:
    sum += zahl
    product *= zahl
    quadrate.append(zahl * zahl)

print(sum)
print(product)
print(sum / len(list) if lst else "Leere Liste!")
print(quadrate)
