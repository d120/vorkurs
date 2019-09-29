vector1 = []
print("vector1 Eingabe: ")
for i in range(3):
    n = input("")
    vector1.append(int(n))

vector2 = []
print("vector2 Eingabe: ")
for i in range(3):
    n = input("")
    vector2.append(int(n))

print("Vektoraddition")
for i in range(3):
    print(vector1[i] + vector2[i])

# INFO: Nun Zugriffsfehler zeigen, wenn man nur 2 Zahlen einliest.
