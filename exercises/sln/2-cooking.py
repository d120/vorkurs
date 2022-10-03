mehl = 450
wasser = 250
salz = 1
oliven = 4
backpulver = 2
tomaten = 400
oregano = 1
knoblauch = 1
z = input("Zutat eingeben: ")
m = float(input("Menge eingeben (ohne Einheit): "))
factor = 0
if z == "Mehl":
    factor = m / mehl
elif z == "Wasser":
    factor = m / wasser
elif z == "Salz":
    factor = m / salz
elif z == "Olivenöl":
    factor = m / oliven
elif z == "Backpulver":
    factor = m / backpulver
elif z == "Tomaten":
    factor = m / tomaten
elif z == "Oregano":
    factor = m / oregano
elif z == "Knoblauch":
    factor = m / knoblauch
else:
    print("Eingabe nicht erkannt")

if factor:
    mehl *= factor
    wasser *= factor
    salz *= factor
    oliven *= factor
    backpulver *= factor
    tomaten *= factor
    oregano *= factor
    knoblauch *= factor
    print(f"""Zutatenliste:
        Mehl: {mehl} g
        Wasser: {wasser} ml
        Salz: {salz} TL, gestrichen
        Olivenöl: {oliven} EL
        Backpulver: {backpulver} TL
        passierte Tomaten: {tomaten} g
        Oregano {oregano} EL
        Knoblauch {knoblauch} Zehe(n)""")
