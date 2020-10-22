zahl = 42


def f1():
    print(zahl)
    zahl = 1337
    print(zahl)


f1()
print(zahl)

# Info: Nächstes Beispiel
liste = []


def f2():
    print(liste)
    liste.append(15)
    print(liste)


f2()
print(liste)
# Frage: Warum das?
