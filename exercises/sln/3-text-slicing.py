# effiziente Lösung (minimale vergleiche)
test = input("Gebe einen Text ein")

voll = len(test)
halb = int(voll / 2)
if test[:halb] == test[voll : voll - halb - 1 : -1]:
    print("Palindrom")
else:
    print("Kein Palindrom")
# Kurze Lösung
if test == test[::-1]:
    print("Palindrom")
else:
    print("Kein Palindrom")
