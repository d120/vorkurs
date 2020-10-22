list_ = [1, 2, 3, 4, 5, 6, 7]

sum_ = 0
product = 1
quadrate = []

for item in list_:
    sum_ += item
    product *= item
    quadrate.append(item * item)

print(sum_)
print(product)
print(sum_ / len(list) if list_ else "Leere Liste!")
print(quadrate)
