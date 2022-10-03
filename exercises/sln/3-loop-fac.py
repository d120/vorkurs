fak = int(input("Welche Fakultät soll berechnet werden: "))
erg = 1

for i in range(1, fak + 1):
    erg *= i

print(f"Die {fak}. Fakultät ist {erg}")
