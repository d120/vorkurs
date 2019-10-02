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
