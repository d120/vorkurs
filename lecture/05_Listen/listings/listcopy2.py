meine_liste = [5, 7, 8, 42]
kopie = meine_liste.copy()

print(meine_liste[0])  # 5
print(meine_liste[1])  # 7

kopie[1] = 2
print(meine_liste[1])  # 7
print(kopie[1])        # 2
