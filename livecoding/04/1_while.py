zahl = int(input("Eine Zahl bitte: "))

rest = zahl - 1
while rest > 0:
    zahl *= rest
    rest -= 1
print(zahl)

# INFO: nächster Schritt für break
while True:
    zahl *= rest
    rest -= 1
    if rest == 1:
        break


# INFO: Zweites Beispiel
vorbei = False
while not vorbei:
    antwort = input("Vorbei?")
    if antwort == "j":
        vorbei = True

    print("Nicht vorbei!")
    
# INFO: Ersetzung
while True:
    antwort = input("Vorbei?")
    if antwort == "j":
        vorbei = True

    # INFO: Spiele beides durch
    if not vorbei:
        continue
    if vorbei:
        break
    
    print("Nicht vorbei!")
