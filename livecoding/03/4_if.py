a = int(input("a: "))
b = int(input("b: "))

if a > b:
    print(str(a) + " ist größer als " + str(b))

# INFO: nächster Schritt
else:
    print(str(a) + " ist kleiner als " + str(b))
# Frage: Stimmt das?

# INFO: ersetzen durch
if a > b:
    print(str(a) + " ist größer als " + str(b))
elif b < a:
    print(str(a) + " ist kleiner als " + str(b))
else:
    print("Beide Zahlen sind gleich groß!")
