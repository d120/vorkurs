prim = int(input("Gib bitte eine Zahl ein: "))
isPrim = True

for i in range(2, prim):
    if(prim % i == 0):
        isPrim = False
        break

if isPrim:
    print("{prim} ist eine Primzahl!")
else:
    print("{prim} ist keine Primzahl!")
