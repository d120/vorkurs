lst = [1,2,3,4,5,6,7]

sum = 0
product = 1
quadrate = []

for l in lst:
    sum += l
    product *= l
    quadrate.append(l * l)

print(sum)
print(product)
print(sum / len(list) if lst else "Leere Liste!")
print(quadrate)
