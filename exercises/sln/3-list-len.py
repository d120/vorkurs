liste = [1, 2, 3, 4, 5]
# Da die Indices bei 0 anfangen ist len(liste) - 1 der letzte gültige Index.
# ------------------------
index = 0
while index < len(liste):
    print(liste[index])
    index += 1
# ------------------------
for i in range(len(liste)):
    print(liste[i])
