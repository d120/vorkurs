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
zutatenliste = (
    "Zutatenliste: \n"
    + " Mehl: {0} g \n"
    + " Wasser: {1} ml \n"
    + " Salz: {2} TL, gestrichen \n"
    + " Olivenöl: {3} EL \n"
    + " Backpulver: {4} TL \n"
    + " passierte Tomaten: {5} g \n"
    + " Oregano {6} EL \n"
    + " Knoblauch {7} Zehe(n)"
)
if z == "Mehl":
    factor = m / mehl
    print(
        zutatenliste.format(
            m,
            factor * wasser,
            factor * salz,
            factor * oliven,
            factor * backpulver,
            factor * tomaten,
            factor * oregano,
            factor * knoblauch,
        )
    )
elif z == "Wasser":
    factor = m / wasser
    print(
        zutatenliste.format(
            factor * mehl,
            m,
            factor * salz,
            factor * oliven,
            factor * backpulver,
            factor * tomaten,
            factor * oregano,
            factor * knoblauch,
        )
    )
elif z == "Salz":
    factor = m / salz
    print(
        zutatenliste.format(
            factor * mehl,
            factor * wasser,
            m,
            factor * oliven,
            factor * backpulver,
            factor * tomaten,
            factor * oregano,
            factor * knoblauch,
        )
    )
elif z == "Olivenöl":
    factor = m / oliven
    print(
        zutatenliste.format(
            factor * mehl,
            factor * wasser,
            factor * salz,
            m,
            factor * backpulver,
            factor * tomaten,
            factor * oregano,
            factor * knoblauch,
        )
    )
elif z == "Backpulver":
    factor = m / backpulver
    print(
        zutatenliste.format(
            factor * mehl,
            factor * wasser,
            factor * salz,
            factor * oliven,
            m,
            factor * tomaten,
            factor * oregano,
            factor * knoblauch,
        )
    )
elif z == "Tomaten":
    factor = m / tomaten
    print(
        zutatenliste.format(
            factor * mehl,
            factor * wasser,
            factor * salz,
            factor * oliven,
            factor * backpulver,
            m,
            factor * oregano,
            factor * knoblauch,
        )
    )
elif z == "Oregano":
    factor = m / oregano
    print(
        zutatenliste.format(
            factor * mehl,
            factor * wasser,
            factor * salz,
            factor * oliven,
            factor * backpulver,
            factor * tomaten,
            m,
            factor * knoblauch,
        )
    )
elif z == "Knoblauch":
    factor = m / knoblauch
    print(
        zutatenliste.format(
            factor * mehl,
            factor * wasser,
            factor * salz,
            factor * oliven,
            factor * backpulver,
            factor * tomaten,
            factor * oregano,
            m,
        )
    )
else:
    print("Eingabe nicht erkannt")
